Test task for Iconicchain job interview

* [Getting started](#getting-started)
    * [Building the project](#building-the-project)
    * [Fill database ](#fill-database-)
    * [Usage](#usage)
  * [Project Features](#project-features)
    * [Authorization](#authorization)
    * [Swagger](#swagger)


## Getting started
### Building the project
After cloning git repo is is needed to call init command
which creates env files with default data and install's pre-commit.
```
make init
```
If pre-commit installation is not wanted, it is possible to use
```
make init-envs
```
The following commands are needed to build project:
```
make build
make full-migrate
```

### Fill database 
As the CRUD for users and organizations were not required in task description,
this instances can be created manually in shell or using manage.py command:

command to enter shell_plus (ptpython implementation)
```
make shell
```
command to create database fixtures (transfers users and organizations data
from config dataclass to database models)
```
make fixtures
```

### Usage
Absolute swagger link is based on allowed hosts from config file
and django expose port from env file.WW

Defaults to http://localhost:8000/api/v1/swagger/

To access API with access restriction "IsAuthenticated" through swagger,
it is possible to add auth token from /users/login/ response into the "Authorization" modal with "Token" prefix

So, correct input shall look like: "Token 5d5274a4c1fcb3db9d252cfca2326b02a595a40ff54dd9492056d770831d010c"


## Project Features

### Authorization
Authorization is implemented using "Django-Rest-Knox" library as it has some advantages
comparing to the basic django rest auth:
1) Allows login for a single user from multiple devices at once using different auth tokens
2) Encrypts auth tokens in the database, so they can't be compromised
3) Has inbuilt mechanism for token expiry

### Swagger
As the task description didn't require UI, project is dedicated to swagger usage, as is:
1) Possibility to Authorize using auth token.
2) Specifying all input data and file upload widget using drf parsers and drf_yasg.
3) Preserving file download response similar to the default reponse from "static"
media urls to trigger file download features on the browser side.