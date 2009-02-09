from biotoolspylons.tests import *

class TestFastaController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='fasta'))
        # Test response...
