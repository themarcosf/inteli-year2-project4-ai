const express = require("express");
const app = express();
const port = 3080;

app.use(express.static('../front'));

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});