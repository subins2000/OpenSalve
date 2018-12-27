FROM kennethreitz/pipenv as build

ADD . /app
WORKDIR /app

RUN pipenv install -r requirements.txt 
