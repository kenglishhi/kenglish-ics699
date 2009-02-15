from bio1.tests import *

class TestBioController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='bio'))
        # Test response...
