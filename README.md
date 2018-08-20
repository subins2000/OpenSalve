# OpenSalve

## Setup

After cloning the repo,

* Install `pip` and [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/) :
  ```
  sudo apt-get install python3-pip
  pip3 install virtualenvwrapper
  ```
* Clone repo
* With the repo folder as the present working directory, setup the environment :
  ```bash
  VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 source ~/.local/bin/virtualenvwrapper.sh
  WORKON_HOME=. mkvirtualenv env
  ```
* Activate environment :
  ```bash
  source env/bin/activate
  ```
* Install dependencies :
  ```bash
  pip install -r requirements.txt
  ```
* Start server :
  ```bash
  python3 manage.py runserver
  ```

## Contributing

* Follow the [PEP 8 Coding Standards](https://www.python.org/dev/peps/pep-0008/)
* Use meaningful commit messages
* Document things as necessary
