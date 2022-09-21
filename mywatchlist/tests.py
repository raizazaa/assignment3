import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        responseHTML = self.client.get('/mywatchlist/html/')
        responseXML = self.client.get('/mywatchlist/xml/')
        responseJSON = self.client.get('/mywatchlist/json/')

        # Check that the response is 200 OK.
        self.assertEqual(responseHTML.status_code, 200)
        self.assertEqual(responseXML.status_code, 200)
        self.assertEqual(responseJSON.status_code, 200)