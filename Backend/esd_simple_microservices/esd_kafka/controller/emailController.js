const email = require("../models/emailModel");



const sendEmail = async (req, res) => {
    const { recipients, subject, text } = req.body;
    console.log(recipients, subject, text)

    email.sendMail(req, res, recipients, subject, text);

    res.status(200).json({
        message: "Email sent!",
    });
    
}

module.exports = {
    sendEmail
};
