const { validationResult } = require("express-validator");
require("express-async-errors");

const service = require("../services/classification_system");

const handleErrors = (res, error) => {
  console.error(error);
  res.status(500).json({ message: error.message });
};

const classifierInvoice = async (req, res) => {
  const { invoiceInfo: invoiceInfo } = req.body;

  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    return res.status(400).json({
      error: errors.errors[0].msg,
    });
  }

  try {
    const result = await service.circuitClassifier(invoiceInfo);
    res.send(result);
  } catch (err) {
    handleErrors(res, err);
  }
};

const processDescription = async (req, res) => {
  const { desc: invoiceDesc } = req.body;

  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    return res.status(400).json({
      error: errors.errors[0].msg,
    });
  }

  try {
    const result = await service.circuitProcessDescription(invoiceDesc);
    res.send(result);
  } catch (err) {
    handleErrors(res, err);
  }
};

const removeInvoice = async (req, res) => {
  const { invoice: invoiceInput } = req.params;

  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    return res.status(400).json({
      error: errors.errors[0].msg,
    });
  }

  try {
    const result = await service.removeInvoice(invoiceInput);
    res.send(result);
  } catch (err) {
    handleErrors(res, err);
  }
};

const getAll = async (req, res) => {

    try {
        const result = await service.getAllInvoices();
        res.send(result);
    } catch (err) {
        handleErrors(res, err);
    }
};

module.exports = {
    classifierInvoice,
    removeInvoice,
    getAll,
    processDescription,
};