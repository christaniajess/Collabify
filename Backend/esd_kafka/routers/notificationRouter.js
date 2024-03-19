const express=require("express");
const {  publish_notification, consume_notification } = require("../controller/notificationController");

const router=express.Router();


router.post("/",(req, res) => {
    res.status(200).json({
        message: "notification running!",
    });
});

router.post("/publish",publish_notification);
router.get("/consume",consume_notification);


module.exports=router; 