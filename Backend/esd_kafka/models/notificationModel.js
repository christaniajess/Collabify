const { Kafka } = require("kafkajs");

const kafka = new Kafka({
    clientId: "myapp",
    brokers: ["kafka:9092"]
});

module.exports = kafka;
