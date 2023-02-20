# DevOps Labs

### Web python application

##### Overview

This application is developed for devOps labs purposes only and tries to demonstrate the power of devOps engineering.
This app shows the current Moscow time 

This application is developed using flask framevork, because it is the simplest web framework for python that I know.
Despite the simplisity, this framevork allows to develop flexible complicated web applications and very sutable for this labs :)

##### Build

To build this app you need

- Download [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/)
- To run this application, you need to install dependencies: [Flask](https://flask.palletsprojects.com/en/2.2.x/) and [pytz](https://pypi.org/project/pytz/)
 -- run ```pip install Flask```
 -- run ```pip install pytz```

##### Usage

- Now you can run this application by `python server.py` console command
- To see the results go browser and open ``127.0.0.1:port`` where `port` is show after running in the previous step
- Try to reload page and see that time is updated

##### Docker
- You can run this application using docker
- type `docker build app_python -tag lab2` to the CLI
- after all the process completes, type `docker run lab2`
- you can see the result in the console from docker image: `curl http://localhost:5000`

##### Tests

This app contains several unit tests for checking reliability
That tests are located in the server_test.py file

##### Contact
[a.smolyakov@innopolis.university](mailto:a.smolyakov@innopolis.university)