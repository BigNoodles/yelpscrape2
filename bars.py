"""
Module to hold the Bar class
"""

#imports
import csv


#logger
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#classes
class Bar():
    """
    A single drinking establishment
    """

    def __init__(self, name, address, url):
        self.name = name
        self.address = address
        self.url = url
        self.rank = 1   #how divey is this bar
        self.dive_tag = False   #is it tagged with keyword dive on review site
        self.rating = 5.0   #average rating out of five stars on review site
        self.reviews = []   #list of strings, each string is one user review


    def write_to_csv(self, csv_filename):
        """
        Write information about the bar out to csv file

        Returns True if successful, False for IOError
        """

        try:
            with open(csv_filename, mode='w') as file_handle:
                bar_writer = csv.writer(file_handle, delimiter=',')

                bar_row = [self.name, self.address, self.url, self.rank, self.dive_tag, self.rating]
                blob_reviews = ''
                for review in self.reviews:
                    blob_reviews.join(review)
                bar_row.append(blob_reviews)
                bar_writer.writerow(bar_row)

                return True

        except OSError as ex:
            logger.error('Error writing to %s: %s', csv_filename, ex)

            return False
