import unittest

from phishing_checker import check_url


class TestPhishingChecker(unittest.TestCase):

    def test_normal_example_url(self):
        warnings = check_url(
            "https://www.example.com/login"
        )
        self.assertEqual(warnings, [])

    def test_ip_address_and_http(self):
        warnings = check_url(
            "http://192.0.2.10/account"
        )
        self.assertTrue(
            any("IP address" in warning for warning in warnings)
        )
        self.assertTrue(
            any("Uses HTTP" in warning for warning in warnings)
        )

    def test_at_symbol_and_http(self):
        warnings = check_url(
            "http://example.com@sample.invalid/login"
        )
        self.assertTrue(
            any("@ symbol" in warning for warning in warnings)
        )
        self.assertTrue(
            any("Uses HTTP" in warning for warning in warnings)
        )

    def test_many_hostname_segments(self):
        warnings = check_url(
            "https://a.b.c.d.e.example.invalid/path"
        )
        self.assertTrue(
            any(
                "hostname segments" in warning
                for warning in warnings
            )
        )

    def test_punycode_hostname(self):
        warnings = check_url(
            "https://xn--example.invalid/"
        )
        self.assertTrue(
            any(
                "punycode-style hostname" in warning
                for warning in warnings
            )
        )

    def test_long_url(self):
        url = (
            "https://www.example.com/"
            + "a" * 110
        )
        warnings = check_url(url)
        self.assertTrue(
            any("unusually long" in warning for warning in warnings)
        )

    def test_malformed_url(self):
        with self.assertRaises(ValueError):
            check_url("http://[bad")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            check_url("")


if __name__ == "__main__":
    unittest.main()
