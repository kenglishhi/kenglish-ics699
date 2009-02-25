from biotoolspylons.tests import *

class TestFlexfastasController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='flexfastas'))
        # Test response...
