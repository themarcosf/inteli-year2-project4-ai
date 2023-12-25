const express = require("express");
const router = express.Router();
const { body, param } = require("express-validator");

const InvoiceController = require("../controllers/classification_system");

router.post(
    "/classinvoice",
    [body("invoiceInfo", "invoiceInfo is required to proceed").exists({ checkFalsy: true })],
    InvoiceController.classifierInvoice
);

router.post(
    "/processdesc",
    [body("desc", "desc is required to proceed").exists({ checkFalsy: true })],
    InvoiceController.processDescription
);

router.get(
    "/getall",
    InvoiceController.getAll
);

router.delete(
    "/delete/:invoice",
    [param("url", "url is required to proceed").exists({ checkFalsy: true })],
    InvoiceController.removeInvoice
);

module.exports = router;