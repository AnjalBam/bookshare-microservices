const redis = require("redis");
const { promisify } = require("util");

let client;

(async () => {
  client = redis.createClient({ url: "redis://redis" });
  await client.connect();
})();

client.on("ready", () => {
  console.log("connected");
});

client.on("error", (err) => {
  console.log("Failed to connect to redis: ", err);
});

module.exports = client;
