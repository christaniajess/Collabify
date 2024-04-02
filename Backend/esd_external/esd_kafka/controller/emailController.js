const email = require("../models/emailModel");
const http = require("http");

const sendEmail = async (recipients, subject, text) => {

    console.log(recipients, subject, text);

  email.sendMail(recipients, subject, text);
};

const email_notification = async (sender, subject, message, receiver) => {
  const options = {
    // hostname: 'host.docker.internal',
    hostname: "host.docker.internal",
    port: 3000,
    path: `/users?user_id=${receiver}`,
    method: "GET",
    params: {
      user_id: receiver,
    },
  };

  const request = http.request(options, (response) => {
    let data = "";

    response.on("data", (chunk) => {
      data += chunk;
    });

    response.on("end", () => {
      sendEmail(JSON.parse(data)["data"]["email"], subject, message);
    });
  });

  request.on("error", (error) => {
    console.error(error);
  });

  request.end();
};

module.exports = {
  email_notification,
};
