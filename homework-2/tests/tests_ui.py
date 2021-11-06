from base import BaseCase
from data import *
from ui.fixtures import *
import pytest
import random

@pytest.mark.UI
class TestAuthorization(BaseCase):
    
    # @pytest.mark.skip()
    authorize = False
    # @pytest.mark.skip()
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

# @pytest.mark.skip()
class TestSegment(BaseCase):
    authorize = True

    @pytest.mark.UI
    # @pytest.mark.skip()
    def test_add_segment(self):
        segments_page = self.dashboard_page.go_to_auditorium()
        segment_name = 'Dasha' + str(random.randint(0, 100))
        segments_page.add_segment(segment_name)

        assert segments_page.new_segment(segment_name)

    # @pytest.mark.skip()        
    @pytest.mark.UI
    def test_del_segment(self):
        segments_page = self.dashboard_page.go_to_auditorium()
        segment_name = 'Dasha' + str(random.randint(0, 100))
        segments_page.add_segment(segment_name)
        assert segments_page.new_segment(segment_name)

        segments_page.remove_segment()
        self.driver.refresh()

        assert segments_page.new_segment(segment_name) == False


class TestCampaigns(BaseCase):
    # @pytest.mark.skip()
    
    @pytest.mark.UI
    def test_add_campaign(self):
        
        campaign_name = 'Dasha' + str(random.randint(0, 100))
        campaign_page = self.dashboard_page.go_to_campaign()
        campaign_page.add_campaign(campaign_name)

        assert campaign_page.is_campaign_exists(campaign_name)