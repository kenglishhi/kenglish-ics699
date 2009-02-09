from biotoolspylons.tests import *

class TestMiniblastController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='miniblast'))
        # Test response...
