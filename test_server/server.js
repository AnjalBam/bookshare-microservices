const express = require("express");
const morgan = require("morgan");

const app = express();
const port = 4001;

app.use(morgan("dev"));

app.get("/", (req, res) => {
  res.send({
    message: "This is working",
  });
});

app.get("*", (req, res) => {
  res.send({
    url: req.url,
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
