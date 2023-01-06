from service.storage.storage_client import IStorageClient
from mongoengine import connect, disconnect


class MongoClient(IStorageClient):
    """Implementation of a storage client for Mongo database server"""
    
    @staticmethod
    def connect(drive: str, host: str, port: int, user: str, pwd: str, db: str) -> None:
        host_connection_string = f'{drive}://{user}:{pwd}@{host}:{port}/{db}'
        connect(host=host_connection_string, authentication_source='admin')
    
    @staticmethod
    def close() -> None:
        disconnect()
