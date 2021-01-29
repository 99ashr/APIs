const Twilio = require("twilio");

const client = new Twilio(
  "AC0b57db73de30c7a002c67af0b8c9713e",
  "7a0a36a632e761de7e9ab6245e7d7039"
);

client.messages
  .list()
  .then(message =>
    console.log(`The most recent message is: ${message[0].body}`)
  )
  .catch(err => console.error(err));

console.log("Gathering your message log!");
