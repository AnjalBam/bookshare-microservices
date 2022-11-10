// const redis = require("redis");
// const { promisify } = require("util");

// const client = redis.createClient({
//   host: "localhost",
//   port: 6379,
// });

// client.on("error", (err) => {
//   console.log("Failed to connect to redis: " + err);
// });

// const setAsync = promisify(client.set).bind(client);
// const getAsync = promisify(client.get).bind(client);

// module.exports = { setAsync, getAsync };
