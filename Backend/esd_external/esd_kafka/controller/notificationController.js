const kafka = require("../models/notificationModel");
const { v4: uuidv4 } = require('uuid');



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

const publish_notification = async (sender, message, receiver) => {

    try {
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

const consume_notification = async (req, res) => {
    try{
        const { topic } = req.query;
        console.log(topic)
        const messages = []; // Array to store messages
        const consumer = kafka.consumer({ "groupId": uuidv4() });
        console.log("Consumer created with unique group id!")
        console.log("Connecting...")
        await consumer.connect()
        console.log("Connected!")
        
        consumer.subscribe({"topic":topic,"fromBeginning":true})
    
        await consumer.run({
          "eachMessage": async result => {
            console.log(`RVD Msg ${result.message.value} on partition ${result.partition}`)
            messages.unshift(JSON.parse(result.message.value.toString())); // Add message to array at the beginning
          }
        })

        // Consume for 1 second
        await new Promise(resolve => setTimeout(resolve, 500));

        messages.reverse();
        await consumer.disconnect()
        console.log("Consumer disconnected!")
        res.status(200).json({
            message: messages, 
        });
    
      }
    
      catch (ex){
        console.error(`Something bad happened ${ex}`)
      }
    }

    


module.exports = { publish_notification,consume_notification };
