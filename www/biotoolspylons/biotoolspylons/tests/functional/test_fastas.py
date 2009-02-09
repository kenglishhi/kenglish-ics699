from biotoolspylons.tests import *

class TestFastasController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='fastas'))
        # Test response...
