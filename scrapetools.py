"""
Tools for webscraping using Selenium
"""

#imports
import logging

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

#setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#classes
class ScrapeTool():
    """
    An object with scraping methods and members
    """

    def __init__(self):
        self.is_open = False


    def open(self, next_url):
        """
        Opens next_url with a Selenium webdriver (Firefox) or returns None
        """

        logger.info(f' Opening page: {next_url} ...')

        opts = Options()
        #opts.headless = True #toggle for headless / visible
        browser = Firefox(options=opts)

        try:
            browser.get(next_url)
            self.is_open = True
            return browser
        except WebDriverException as ex:
            logger.error(f' Error retrieving {next_url}: {ex}')
            return None



    def cleanup(self, browser):
        """
        Closes and cleans up data from the webdriver
        """

        logger.info(f' Cleaning up webdriver ...')

        try:
            browser.close()
            browser.quit()
            self.is_open = False
            return True
        except WebDriverException as ex:
            logger.error(f' Error closing webdriver: {ex}')
            return False
