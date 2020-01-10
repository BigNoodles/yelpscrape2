"""
Class tools to parse Yelp for bar info
"""

#imports
import logging

from scrapetools import ScrapeTool


#logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#constants
BASE_URL_BEGIN = 'https://www.yelp.com/search?find_desc=bars&find_loc='
BASE_URL_END = '&ns=1&attrs=RestaurantsPriceRange2.1'

'San%20Francisco%2C%20CA'
#classes

class YelpParser():
    """
    Hold tools to parse Yelp pages for bars
    """

    def __init__(self):
        self.city = ''
        self.url_list = []

    def get_city_results(self):
        """
        Get all bar urls from self.city
        """

        logger.info(f'Looking for cheap bars in {self.city} ...')
        url_middle = 'San%20Francisco%2C%20CA'
        city_url = BASE_URL_BEGIN + url_middle + BASE_URL_END

        scraper = ScrapeTool()
        response = scraper.open(city_url)
