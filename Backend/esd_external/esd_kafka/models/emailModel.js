const formData = require('form-data');
const Mailgun = require('mailgun.js');
const mailgun = new Mailgun(formData);
const mailgunDomain = process.env.mailgunDomain;
const mailgunAPIKeyID = process.env.mailgunAPIKeyID;
const mailgunAPIKey = process.env.mailgunAPIKey;

const mg = mailgun.client({username: mailgunAPIKeyID, key: mailgunAPIKey});

const sendMail = (recipients, subject, text) => {
	mg.messages.create(mailgunDomain, {
		from: "Collabify <mailgun@sandbox-123.mailgun.org>",
		to: recipients,
		subject: subject,
		text: text
	})
	.then(msg => console.log(msg)) // logs response data
	.catch(err => console.log(err)); // logs any error
}

module.exports = { sendMail }
