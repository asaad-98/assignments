from life_expectancy.region import Region
import unittest


# Unit test for the actual_countries method
class TestRegion(unittest.TestCase):
    def test_actual_countries(self):
        """Test the actual_countries method."""
        expected_countries = [
            "AT",
            "BE",
            "BG",
            "CH",
            "CY",
            "CZ",
            "DK",
            "EE",
            "EL",
            "ES",
            "FI",
            "FR",
            "HR",
            "HU",
            "IS",
            "IT",
            "LI",
            "LT",
            "LU",
            "LV",
            "MT",
            "NL",
            "NO",
            "PL",
            "PT",
            "RO",
            "SE",
            "SI",
            "SK",
            "DE",
            "AL",
            "IE",
            "ME",
            "MK",
            "RS",
            "AM",
            "AZ",
            "GE",
            "TR",
            "UA",
            "BY",
            "UK",
            "XK",
            "FX",
            "MD",
            "SM",
            "RU",
        ]
        self.assertEqual(Region.actual_countries(), expected_countries)
