from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log

class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        # self.client = MongoClient("mongodb://localhost:27017/")  # When only Mongo DB is running on Docker.
        self.client = MongoClient("mongodb://192.168.0.238:27017/")     # When both Mongo and This application is running on
                                                                    # Docker and we are using Docker Compose

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        log.info('Reading All Data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    
    def readAll(self, query):
        log.info('Reading All Data')
        documents = self.collection.find(query)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def readOne(self, query):
        log.info('Reading One Data')
        documents = self.collection.find_one(query)
        
        # print("documents",documents)
        # output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return documents        

    def  write(self, data):
        log.info('Writing Data')
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self, data):
        log.info('Updating Data')
        filt = data['Filter']
        updated_data = {"$set": data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        log.info('Deleting Data')
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
