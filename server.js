/**
 * Copyright(c) 2018 Subin Siby
 * GPL-3.0 Licensed
 */

/**
 * OpenSalve config
 * @private
 */
var config = require('./config.js')

/**
 * Port to listen
 * @private
 */
var port = process.env.PORT || 8080

var express = require('express')
var app = express()
var bodyParser = require('body-parser')

if (config.db.client === 'pg') {
  var connectionString = 'postgres://' + config.db.username + ':' + config.db.password + '@' + config.db.host + ':' + config.db.port + '/' + config.db.database

  var knex = require('knex')({
    client: config.db.client,
    connection: connectionString
  })
} else {
  var knex = require('knex')({
    client: config.db.client,
    connection: {
      host: config.db.host,
      port: config.db.port,
      user: config.db.username,
      password: config.db.password,
      database: config.db.database
    }
  })
}

var apiIndexRouter = require('./app/api/index.js')(config, knex)
var helpRouter = require('./app/api/help.js')(config, knex)

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

app.use('/api', apiIndexRouter)
app.use('/api/help', helpRouter)

app.listen(port)
console.log('Server started on http://localhost:' + port + '/')
