# OpenSalve

## Setup

After cloning the repo,

* Setup [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/)
* With the repo folder as the present working directory, setup the environment :
  ```bash
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
  source ~/.local/bin/virtualenvwrapper.sh # Better add this to .bashrc
  mkvirtualenv opensalve
  rm $VIRTUAL_ENV/bin/postactivate
  ln -s `realpath .env/postactivate` $VIRTUAL_ENV/bin/postactivate
  ```
* Edit file `.env/postactivate` and set `SECRET_KEY`, database config
* Activate environment :
  ```bash
  source ~/.local/bin/virtualenvwrapper.sh # Better add this to .bashrc
  workon opensalve
  ```
* Install dependencies (`pip install Django djangorestframework drf-yasg flex swagger_spec_validator`) :
  ```bash
  pip install -r requirements.txt
  ```
* Open file `.env/bin/postactivate` and set secret key :
  ```bash
  export DJANGO_SECRET_KEY='a_random_key_here'
  ```
* Migrate :
  ```bash
  python3 manage.py makemigrations && python3 manage.py migrate
  ```
* Start server :
  ```bash
  python3 manage.py runserver
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
