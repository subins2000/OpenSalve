/**
 * Copyright(c) 2018 Subin Siby
 * GPL-3.0 Licensed
 */

/**
 * OpenSalve config
 * @private
 */
var config = require('./config.json')

/**
 * Port to listen
 * @private
 */
var port = process.env.PORT || 8080

var express = require('express')
var app = express()
var bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

var router = express.Router()

// return name and API version
router.get('/', function (req, res) {
  res.json({
    'name': config.name,
    'version': config.version
  })
})

app.use('/api', router)

app.listen(port)
console.log('Server started on http://localhost:' + port + '/')
