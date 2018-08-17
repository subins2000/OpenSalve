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

var apiIndexRouter = require('./app/api/index.js')(config)
var helpRouter = require('./app/api/help.js')(config)

app.use('/api', apiIndexRouter)
app.use('/api/help', helpRouter)

app.listen(port)
console.log('Server started on http://localhost:' + port + '/')
