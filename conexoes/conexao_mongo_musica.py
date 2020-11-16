from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def connect():
    conn = MongoClient("mongodb://localhost:27017/")

    try:
        conn.admin.command('ismaster')
        base = conn['prova']
        table = base['musica']
    except ConnectionFailure:
        print(ConnectionFailure)

    return table


def save(value):
    connect().insert_one(value)
