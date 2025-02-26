import unittest
from unittest.mock import patch
from src.geolocation import get_geolocation_by_city, get_geolocation_by_zip

class TestGeolocation(unittest.TestCase):

    def setUp(self):
        # Common setup for all tests
        self.mock_response = unittest.mock.Mock()
        self.mock_response.status_code = 200

    @patch("src.geolocation.requests.get")
    def test_get_geolocation_by_city(self, mock_get):
        # Setup
        self.mock_response.json.return_value = [{
            "name": "Madison",
            "lat": 43.0731,
            "lon": -89.4012,
            "state": "WI"
        }]
        mock_get.return_value = self.mock_response

        # Execute
        result = get_geolocation_by_city("Madison", "WI")

        # Assert
        self.assertEqual(result["city"], "Madison")

    @patch("src.geolocation.requests.get")
    def test_get_geolocation_by_zip(self, mock_get):
        # Setup
        self.mock_response.json.return_value = {
            "name": "New York",
            "lat": 40.7128,
            "lon": -74.0060
        }
        mock_get.return_value = self.mock_response

        # Execute
        result = get_geolocation_by_zip("10001")

        # Assert
        self.assertEqual(result["city"], "New York")

if __name__ == "__main__":
    unittest.main()
