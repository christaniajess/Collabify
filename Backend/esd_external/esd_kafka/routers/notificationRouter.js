/**
 * @swagger
 * /notification/consume:
 *   get:
 *     summary: Retrieve a notification
 *     description: Retrieve a notification message from a specified topic.
 *     parameters:
 *       - in: query
 *         name: topic
 *         schema:
 *           type: string
 *         required: true
 *         description: The topic (follows user_id) from which the message will be retrieved.
 *     responses:
 *       200:
 *         description: Notification successfully retrieved from the topic.
 *       400:
 *         description: Error retrieving notification.
 */

const express=require("express");
const {  publish_notification, consume_notification } = require("../controller/notificationController");
const mailgunDomain = process.env.mailgunDomain;

const router=express.Router();


router.get("/",(req, res) => {
    res.status(200).json({
        message: "notification running!",
        test:mailgunDomain,
    });
});

router.post("/publish",publish_notification);
router.get("/consume",consume_notification);


module.exports=router; 