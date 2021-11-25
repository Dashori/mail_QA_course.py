import pytest
import faker

from api.client import ApiClient
from api.data import EMAIL, PASSWORD

fake = faker.Faker()

class TestApi:
    
    client = ApiClient()
    
    @pytest.fixture(scope='function')
    def login(self):
        self.client.post_login(EMAIL, PASSWORD)

    @pytest.fixture(scope='function')
    def do_segment(self):
        name = str(fake.bothify(text='???? ##?'))
        segment_id = self.client.create_segment(name)
        yield segment_id
        
    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_segment_create(self, do_segment):
        assert self.client.get_all_segments(do_segment) == 0
        self.client.delete_segment(do_segment)

    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_segment_delete(self, do_segment):
        self.client.delete_segment(do_segment)
        assert self.client.get_all_segments(do_segment)


    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_campaign_create(self):
        name = str(fake.bothify(text='????##?'))
        campaign_id = self.client.create_campaign(name)
        assert self.client.get_all_campaign(campaign_id) == 0
        self.client.delete_campaign(campaign_id)
        