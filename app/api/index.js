/**
 * Copyright(c) 2018 Subin Siby
 * GPL-3.0 Licensed
 */

module.exports = function (config) {
  var express = require('express')
  var router = express.Router()

  // return name and API version
  router.get('/', function (req, res) {
    res.json({
      'name': config.manifest.name,
      'version': config.manifest.version
    })
  })

  return router
}
