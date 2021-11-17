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
    
    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_segment_create(self):
        name = str(fake.bothify(text='???? ##?'))
        segment_id = self.client.create_segment(name)
        assert segment_id in self.client.get_all_segments()
        self.client.delete_segment(segment_id)

    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_segment_delete(self):
        name = str(fake.bothify(text='???? ##?'))
        segment_id = self.client.create_segment(name)
        self.client.delete_segment(segment_id)
        assert segment_id not in self.client.get_all_segments()

    @pytest.mark.API
    @pytest.mark.usefixtures('login')
    def test_campaign_create(self):
        name = str(fake.bothify(text='????##?'))
        campaign_id = self.client.create_campaign(name)
        assert campaign_id in self.client.get_all_campaign()
        self.client.delete_campaign(campaign_id)
        

