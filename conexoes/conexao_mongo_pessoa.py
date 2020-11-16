from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def connect():
    conn = MongoClient("mongodb://localhost:27017/")

    try:
        conn.admin.command('ismaster')
        base = conn['provapessoa']
        table = base['pessoa']
    except ConnectionFailure:
        print(ConnectionFailure)

    return table


def save(value):
    connect().insert_one(value)


def search(value):
    return connect().find_one({"cpf": value})


def check_if_cpf_exists(value):
    return connect().find({"cpf": value}).count() > 0


def update(value, newvalue):
    connect().replace_one({"cpf": value}, newvalue)


def delete(value):
    connect().find_one_and_delete({"cpf": value})
