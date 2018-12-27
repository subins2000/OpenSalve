# OpenSalve

## Setup

After cloning the repo,

* Setup [`pipenv`](https://pipenv.readthedocs.io/en/latest/)
* With the repo folder as the present working directory, setup the environment :
  ```bash
  pipenv install
  ```
* Activate environment :
  ```bash
  pipenv shell
  ```
* Open file `.env` and set secret key :
  ```
  DJANGO_SECRET_KEY='random stuff here...'
  ```
  For this very purpose, one could use the following code.
  ```python
  import random
  "".join([random.SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(96)])
  ```
* Migrate :
  ```bash
  python manage.py makemigrations && python manage.py migrate
  ```
* Start server :
  ```bash
  python manage.py runserver
  ```

## Contributing

* Follow the [PEP 8 Coding Standards](https://www.python.org/dev/peps/pep-0008/)
* Use meaningful commit messages
* Document things as necessary

## TODO

- [ ] User Accounts
    - [x] Login/Register
    - [ ] User Roles
- [ ] Help Requests
    - [x] Register request
    - [x] Get request complete info
    - [x] Resolve request
    - [x] Status of request
    - [x] Comments on request
    - [ ] Visualize request in maps
    - [x] Editing requests
    - [ ] Prioritizing Requests
    - [ ] Live location with GPS
- [ ] Camps
    - [x] Add & List
    - [ ] Camp requirements
    - [ ] Inhabitants
        - [ ] Allow camp manager to add
- [ ] Collection Centres
    - [x] Add & List
    - [ ] Supplies required
        - [ ] List quantity, unit
    - [ ] Stock view

## API Docs

Use an interactive API documentation from [/docs](http://127.0.0.1:8000/docs) after setting up OpenSalve locally on `http://127.0.0.1:8000`.

Or use [the online API docs](https://lab.subinsb.com/OpenSalve/).

Steps to generate static API docs :

* Install `spectacle-docs` :
  ```bash
  npm install -g spectacle-docs
  ```
* Save the OpenAPI in JSON format to `api.json` file (where `http://127.0.0.1:8000` is where OpenSalve is running) :
  ```
  curl http://127.0.0.1:8000/docs/?format=openapi > api.json
  ```
* Generate docs :
  ```
  spectacle api.json -t docs
  ```
* Cleanup :
  ```
  rm api.json
  ```

Or use this one liner :

```bash
curl http://127.0.0.1:8000/docs/?format=openapi > api.json && spectacle api.json -t docs && rm api.json
```
