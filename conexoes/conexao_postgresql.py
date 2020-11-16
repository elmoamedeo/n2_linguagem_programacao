import psycopg2


def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="prova",
            user="postgres",
            password="admin"
        )
        conn.set_session(autocommit=True)
    except (Exception, psycopg2.Error) as error:
        return print("Error while connecting to PostgreSQL", error)

    return conn


def save(value):
    insert = "INSERT INTO prova.musica VALUES (DEFAULT, '{}', '{}', '{}')".format(value.nome, value.autor, value.genero)
    try:
        cursor = connect().cursor()
        cursor.execute(insert)
    except (Exception, psycopg2.Error) as error:
        return print("Error while executing query", insert, error)
    finally:
        if connect():
            connect().close()
