"""
Test suite for scrapetools.py
"""

#imports
import unittest
from scrapetools import ScrapeTool


#classes
class ScrapeToolsTests(unittest.TestCase):

    def setUp(self):
        self.scraper = ScrapeTool()


    def test_open_flag_exists(self):

        self.assertFalse(self.scraper.is_open)


    def test_open_bad_url(self):

        next_url = ''
        self.response = self.scraper.open(next_url)

        self.assertEqual(self.response, None)
        self.assertFalse(self.scraper.is_open)


    def test_open_good_url(self):

        next_url = 'http://www.python.org'
        self.response = self.scraper.open(next_url)

        expected_title = 'Welcome to Python.org'
        scraped_title = self.response.title

        self.assertEqual(scraped_title, expected_title)
        self.assertTrue(self.scraper.is_open)


    def test_close_browser(self):

        next_url = 'http://www.python.org'
        self.response = self.scraper.open(next_url)
        result = self.scraper.cleanup(self.response)

        self.assertTrue(result)
        self.assertFalse(self.scraper.is_open)


    def tearDown(self):
        if self.scraper.is_open:
            self.scraper.cleanup(self.response)


if __name__ == '__main__':
    unittest.main()
        

