const express = require("express");
const http = require("http");
const cors = require("cors");
const amqp = require('amqplib/callback_api');

const { email_notification } = require("./controller/emailController");
const { publish_notification } = require("./controller/notificationController");

// express app
const app = express();
const PORT = 3000;

app.use(cors()); // Allows cross-origin requests

app.use(express.json());
app.use("/email", require("./routers/emailRouter"));
app.use("/notification", require("./routers/notificationRouter"));

const server = http.createServer(app);

app.get("/", (req, res) => {
    res.status(200).json({
        message: "server running!",
    });
});

// Start the server
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Connect to RabbitMQ server
amqp.connect('amqp://host.docker.internal', function(error0, connection) {
    if (error0) {
        throw error0;
    }

    // Create a channel
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        // Listen to the 'notification' queue
        var queue = 'notification';

        channel.assertQueue(queue, {
            durable: true
        });

        console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);

        channel.consume(queue, function(msg) {
            console.log(" [x] Received %s", msg.content.toString());
            const { sender, message, receiver } = JSON.parse(msg.content.toString());
            publish_notification(sender, message, receiver);
        }, {
            noAck: true
        });

        // Listen to the 'email' queue
        var queue = 'email';

        channel.assertQueue(queue, {
            durable: true
        });

        console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);

        channel.consume(queue, function(msg) {
            console.log(" [x] Received %s", msg.content.toString());
            const { sender, subject, message, receiver } = JSON.parse(msg.content.toString());
            email_notification(sender, subject, message, receiver);
        }, {
            noAck: true
        });
    });
});
