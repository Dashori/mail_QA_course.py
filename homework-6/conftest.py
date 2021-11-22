import pytest
from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def sql_client():
    sql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    sql_client.connect()
    yield sql_client
    sql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        sql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
        sql_client.recreate_db()
        sql_client.connect()
        sql_client.create_tables()
        sql_client.connection.close()