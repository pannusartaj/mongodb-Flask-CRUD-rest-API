import logging as log
from datetime import datetime
from os import times

from bson.objectid import ObjectId
from pymongo import MongoClient

from helper import validate_request_body


class MongoCRUD:
    def __init__(self,audio_type, data=None, id=None):
        log.basicConfig(level=log.DEBUG,
                        format='%(asctime)s %(levelname)s:\n%(message)s\n')
        # self.client = MongoClient("mongodb://localhost:27017/")
        # When only Mongo DB is running on Docker.
        # When both Mongo and This application is running on
        self.client = MongoClient("mongodb://mongodb:27017/")
        # Docker and we are using Docker Compose

        database = "audio_db"
        collection = audio_type
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.audio_type = audio_type
        if data:
            data["updated_on"] = datetime.now().isoformat()

        self.data = data if data else None
        self.filter_id = {'_id': ObjectId(id) } if id else None

    def read(self):
        log.info('Reading All Data')
        if self.filter_id:
            documents = self.collection.find(self.filter_id)
        else:
            documents = self.collection.find()

        output = [{item: data[item] for item in data if item != '_id'}
                  for data in documents]
        return output

    def create(self):
        log.info('Writing Data')
        validate_request_body(self.audio_type, self.data)
        response = self.collection.insert_one(self.data)
        output = {'Status': 'Successfully Created',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        log.info('Updating Data')
        validate_request_body(self.audio_type, self.data)
        updated_data = {"$set": self.data}
        response = self.collection.update_one(self.filter_id, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count >
                  0 else "Nothing was updated."}
        return output

    def delete(self):
        log.info('Deleting Data')
        response = self.collection.delete_one(self.filter_id)
        output = {'Status': 'Successfully Deleted' if response.deleted_count >
                  0 else "Document not found."}
        return output
