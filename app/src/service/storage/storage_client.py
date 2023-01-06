from abc import ABC, abstractstaticmethod


class IStorageClient(ABC):
    """Base representation of a storage client"""

    @staticmethod
    @abstractstaticmethod
    def connect(drive: str, host: str, port: int, user: str, pwd: str, db: str) -> None:
        """Connects to the strorage server"""

    @staticmethod
    @abstractstaticmethod
    def close() -> None:
        """Closes the conection to the server"""
