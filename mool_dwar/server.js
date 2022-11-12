const express = require("express");
const morgan = require("morgan");

const { setupProxies } = require("./proxy");
const { ROUTES } = require("./routes");

const client = require("./db/redis");

const app = express();
const port = 4000;

app.use(morgan("dev"));

app.get("/test-redis", async (req, res) => {
  client.set("name", "Anjal");
  return res.send({ message: "working" });
});
setupProxies(app, ROUTES);

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});

// const express = require("express");
// const app = express();
// const redis = require('redis')

// const {createClient} = redis;

// app.use(require("morgan")("dev"));
// // const redis = require("redis");
// async function nodeRedisDemo() {
//   try {
//     console.log('changed');
//     const client = createClient({
//         host: 'redis',
//     });
//     console.log('connecting')
//     await client.connect();

//     await client.set('mykey', 'Hello from node redis');
//     const myKeyValue = await client.get('mykey');
//     console.log(myKeyValue);

//     const numAdded = await client.zAdd('vehicles', [
//       {
//         score: 4,
//         value: 'car',
//       },
//       {
//         score: 2,
//         value: 'bike',
//       },
//     ]);
//     console.log(`Added ${numAdded} items.`);

//     for await (const { score, value } of client.zScanIterator('vehicles')) {
//       console.log(`${value} -> ${score}`);
//     }

//     await client.quit();
//   } catch (e) {
//     console.error(e);
//   }
// }

// nodeRedisDemo();

// app.get("/", function (req, res) {
//   // redisClient.get("numVisits", function (err, numVisits) {
//   //   numVisitsToDisplay = parseInt(numVisits) + 1;
//   //   if (isNaN(numVisitsToDisplay)) {
//   //     numVisitsToDisplay = 1;
//   //   }
//   //   res.send("web1: Total number of visits is: " + numVisitsToDisplay);
//   //   numVisits++;
//   //   redisClient.set("numVisits", numVisits);
//   // });
//   res.send('Hello')
// });

// app.listen(5000, function () {
//   console.log("Web app is listening on port 5000");
// });
