exports.up = function (knex, Promise) {
  return Promise.all([
    knex.schema.createTable('users', (table) => {
      table.increments('id')
      table.string('username').unique().notNullable()
      table.string('password').notNullable()
      table.string('email').unique().notNullable()
      table.string('name')
      table.string('role').defaultTo('user')
      table.timestamp('created_at').defaultTo(knex.fn.now())

      table.index('username')
    })
  ])
}

exports.down = function (knex, Promise) {
  return Promise.all([
    knex.schema.dropTable('user'),
  ])
}
