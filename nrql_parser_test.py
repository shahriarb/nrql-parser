import unittest

class TestNRQLParser(unittest.TestCase):
    def test_parse_valid_query(self):
        parser = NRQLParser()
        query = "SELECT count(distinct user) FROM PageView WHERE userAgent.os = 'Mac' FACET countryCode LIMIT 20 SINCE 2023-04-28T00:00:00"
        result = parser.parse(query)
        self.assertEqual(result, {
            "select": ["count(distinct user)"],
            "from": "PageView",
            "where": "userAgent.os = 'Mac'",
            "facet": ["countryCode"],
            "limit": 20,
            "since": "2023-04-28T00:00:00",
        })

    def test_parse_invalid_query(self):
        parser = NRQLParser()
        query = "SELECT count(distinct user) FROM PageView WHERE userAgent.os = 'Mac' FACET countryCode LIMIT 20 SINCE 1d"
        with self.assertRaises(ValueError):
            parser.parse(query)

if __name__ == "__main__":
    unittest.main()
