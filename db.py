from typing import Any, List, Dict, Union, Tuple
from pymongo import MongoClient
from db_rules import table_insert_rule, order_insert_rule
from pymongo.errors import (
    ConnectionFailure,
    PyMongoError,
    ServerSelectionTimeoutError,
    CollectionInvalid,
    ExecutionTimeout,
    OperationFailure,
)
# pylint: disable-all
class Base:
    def __init__(self, db: str, collection: str) -> Any:
        self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        self.db = self.client[db]
        self.collection_name = collection
        self.collection = self.db[self.collection_name]


    def execute_with_retry(self, func):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                live_db = func()
                return live_db
            except Exception as e:
                print(f"Execution failed: {e}")
                retries += 1
                print(f"Retrying... (Attempt {retries}/{max_retries})")
        else:
            print("Maximum retries exceeded. Giving up.")
            exit()


    def check_or_alive(self) -> None:
        try:
            self.client.server_info()
        except ServerSelectionTimeoutError as e:
            print("Connection failure:", str(e))
            raise Exception("Connection failure")
        
    def connect_validation_rule(self, rule) -> str:
        try:
            if rule == 'reserv':
                self.db.command("collMod", self.collection.name, **table_insert_rule())
            elif rule == 'order':
                self.db.command("collMod", self.collection.name, **order_insert_rule())
            else:
                return 'Nera taisykles i inserta tokios'    
        except OperationFailure as e:
            print(f"Failed to enable schema validation: {e}")

    def create_document(self, task: Dict[str, Any], rule) -> str:
        self.execute_with_retry(self.check_or_alive)
        self.connect_validation_rule(rule)
        result = self.collection.insert_one(task)
        return str(result.inserted_id)

    def get_document(self, value: str, field_name: str) -> Union[tuple[List[dict], int], str]:
        self.execute_with_retry(self.check_or_alive)
        try:
            query = {field_name: {"$eq": value}}
            result = self.collection.find(query)
            result_count = self.collection.count_documents(query)
            return result, result_count
        
        except ExecutionTimeout as e:
            return f"Query execution timeout:, {str(e)}"

        except PyMongoError as e:
            return f"An error occurred:, {str(e)}"

    def get_documents_where_time_more_value1_and_time_less_value2(
        self,
        field_name1: str,
        value1: str,
        value2: str,
        table_name: str,
        field_name2: str,
    ) -> List[dict]:
        self.execute_with_retry(self.check_or_alive)
        query = {
             field_name1:
             { '$gte': value1, 
               '$lte': value2 },
            field_name2: {'$eq': table_name} 
               
        }
        result = self.collection.find(query)
        return list(result)
