from base import BaseCase
from data import *
from ui.fixtures import *
import pytest
import random
import faker
fake = faker.Faker()

@pytest.mark.UI
class TestAuthorization(BaseCase):
    
    authorize = False
    @pytest.mark.parametrize(
        "email, password",
        [
            pytest.param(
                BAD_EMAIL, PASS
            ),
            pytest.param(
                EMAIL, BAD_PASS
            )
        ]
    )
    def test_badlogin(self, email, password):
        self.login_page.login(email, password)
        assert self.driver.current_url != DASHBOARD_URL

class TestSegment(BaseCase):
    authorize = True

    @pytest.mark.UI
    def test_add_segment(self):
        segments_page = self.dashboard_page.go_to_auditorium()
        segment_name = str(fake.bothify(text='#????##?'))
        segments_page.add_segment(segment_name)

        assert segments_page.new_segment(segment_name)
        segments_page.remove_segment()


    @pytest.mark.UI
    def test_del_segment(self):
        segments_page = self.dashboard_page.go_to_auditorium()
        segment_name = str(fake.bothify(text='#????##?'))
        segments_page.add_segment(segment_name)
        assert segments_page.new_segment(segment_name)

        segments_page.remove_segment()
        self.driver.refresh()

        assert segments_page.new_segment(segment_name) == False


class TestCampaigns(BaseCase):

    authorize = True
        
    @pytest.mark.UI
    def test_add_campaign(self):
        
        campaign_name = str(fake.bothify(text='????##?'))
        campaign_page = self.dashboard_page.go_to_campaign()
        campaign_page.add_campaign(campaign_name)

        assert campaign_page.is_campaign_exists(campaign_name)