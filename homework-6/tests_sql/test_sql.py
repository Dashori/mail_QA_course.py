import pytest
from mysql.builder import SQLBuilder
from mysql.models import TotalCount, CountByType, TopMostFrequent
from mysql.models import  TopBiggestClientError, TopFrequentServerError

import res_log

class SQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, sql_client):
        self.mysql = sql_client

    @pytest.fixture(scope='session', autouse=True)
    def setup_data(self, sql_client):
        self.mysql_builder = SQLBuilder(sql_client, path='access.log')
        self.prepare()


class TestMysql(SQLBase):

    def prepare(self):
        self.mysql_builder.run_all()

    def get_rows(self, query_type):
        rows = self.mysql.session.query(query_type).all()
        return rows

    def get_query(self, query_type):
        rows = self.mysql.session.query(query_type)
        return rows

    def test_count_total(self):
        result = self.get_rows(TotalCount)

        assert len(result) == 1
        assert result[0].count == res_log.total_count()

    def test_count_by_type(self):
        result = self.get_query(CountByType)

        assert len(result.all()) == 4
        assert result.filter_by(type_name='GET').first().count == res_log.total_get()
        assert result.filter_by(type_name='HEAD').first().count == res_log.total_head()
        assert result.filter_by(type_name='POST').first().count == res_log.total_post()
        assert result.filter_by(type_name='PUT').first().count == res_log.total_put()

    def test_top_10(self):
        result = self.get_query(TopMostFrequent)
        i = 1
        for value in res_log.top_10_request().values():
            assert result.filter_by(id=i).first().count == value
            i += 1

    def test_top_4xx_requests(self):
        result = self.get_query(TopBiggestClientError)
        print(result.all())
        arr = res_log.top_4xx_big()
        for i in range(5):
            assert result.filter_by(url=arr[i][3]).first().rc == arr[i][0]
            assert result.filter_by(url=arr[i][3]).first().size == arr[i][1]
            assert result.filter_by(url=arr[i][3]).first().ip == arr[i][2]

    def test_top_5xx_users(self):
        result = self.get_query(TopFrequentServerError)

        dict = res_log.top_5xx()
        i = 1
        for value in dict.values():
            assert result.filter_by(id=i).first().count == value
            i += 1