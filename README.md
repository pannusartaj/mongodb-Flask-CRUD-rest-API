# mongodb-Flask-CRUD-rest-API

An Flask REST API interface for MongoDB using following technologies

#### Docker
It is a containerizing technology that allows us to containerize our applications so that they are free from environmental drift and are isolated with only a few components exposed
for the world to view. A container is similar to a Virtual Machine but is much lighter than an actual VM.

#### REST API
Representational State Transfer is an architectural style design for Application Programming Interface which allows us to get the current state of an application.

#### CRUD Model
Whenever we are designing an API service, our model must include at least 4 basic types of functionalities — Create, Read, Update, Delete, or CRUD.

#### JSON SCHEMA VALIDATION
JSON Request payload is being validated against a given JSON schema

#### Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

#### MongoDB
MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas

## Usage
To run the program, first you should make sure Docker is running, start it using:

```sh
$ docker-compose up
```

You can test the API using postman at `localhost:2021/crud/<audioFileType>/<audioFileID>`
