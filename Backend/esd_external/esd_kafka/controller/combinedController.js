const email = require("../models/emailModel");
const http = require('http');
const kafka = require("../models/notificationModel");




const sendEmail = async (req, res,recipient) => {


    const subject = "Collabify Notification";
    const {message,sender}=req.body;
    const text = `You have a new message from ${sender}:\n\n ${message}`;
    console.log(recipient, subject, text)
    email.sendMail(req, res, recipient, subject, text);


    
}




const check_topic = async (topicName)=> {
  try {

    const admin = kafka.admin();
    console.log("Connecting...")
    await admin.connect()
    console.log("Connected!")

    const topics = await admin.listTopics();

    // Check if the topic exists
    if (!topics.includes(topicName)) {
      // If not, create it
      await admin.createTopics({
        "topics": [{
          "topic": topicName
        }]
      })
      console.log("Topic created successfully!")
    } else {
      console.log("Topic already exists!")
    }

    await admin.disconnect()

  } catch (ex) {
    console.error(`Something bad happened at topic check ${ex}`)
  }
}

const publish_notification = async (req, res) => {

    try {
        const { sender, message, receiver } = req.body;
        await check_topic(receiver)
        const producer = kafka.producer();

        console.log("topic checked!")
        console.log("Connecting...");
        await producer.connect();
        console.log("Connected!");
        console.log(sender,message);
 
        const result = await producer.send({
            topic: receiver,
            messages: [
                {
                    value: JSON.stringify({
                        sender: sender,
                        message: message
                    })
                }
            ]
        });
        console.log("send successfully! ", result);
        await producer.disconnect();

    } catch (ex) {
        console.error(`Something bad happened at publish notification ${ex}`);
    }
};


const notify = async (req, res) => {

    publish_notification(req, res);


    const { receiver } = req.body;
    const options = {
        // hostname: 'host.docker.internal',
        hostname: 'host.docker.internal',
        port: 3000,
        path: `/users?user_id=${receiver}`,
        method: 'GET',
        params : {
            user_id: receiver
        }
    };

    const request = http.request(options, response => {
        let data = '';

        response.on('data', chunk => {
            data += chunk;
        });

        response.on('end', () => {
            console.log(JSON.parse(data));

            sendEmail(req, res,JSON.parse(data)['data']['email'])

            res.status(200).json({
                message: "Notification sent!",
            });

        });
    });

    request.on('error', error => {
        console.error(error);
    });

    request.end();
    
}

module.exports = {
    notify
};
