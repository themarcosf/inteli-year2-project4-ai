const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");

app.use(bodyParser.json());

//Import Cors
app.use(cors());

//Import Routes
const invoiceRoute = require("./routes/classification_system");

//Use Routes
app.use("/v1/invoice", invoiceRoute);

app.get("/", (req, res) => {
  res.send({
    message: "Health check completed!",
    status: 200,
  });
});

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});