// Update with your config settings.

module.exports = {

  development: {
    /**
    // sqlite
    client: 'sqlite',
    connection: {
      filename: './dev.sqlite3'
    },*/
    client: 'postgresql',
    connection: {
      database: 'opensalve',
      user: 'username',
      password: 'password'
    },
  },

  staging: {
    client: 'postgresql',
    connection: {
      database: 'my_db',
      user: 'username',
      password: 'password'
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      tableName: 'knex_migrations'
    }
  },

  production: {
    client: 'postgresql',
    connection: {
      database: 'my_db',
      user: 'username',
      password: 'password'
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      tableName: 'knex_migrations'
    }
  }

}
