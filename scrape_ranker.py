"""
Module to scrape Ranker.com.

Consult README.md for instructions.

Based on https://github.com/johnwmillr/trucks-and-beer
"""

import argparse
import datetime
import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from dotenv import load_dotenv, find_dotenv


ERROR: str = "ERROR:\n\t'-> %s is None"
URL: str = "https://www.ranker.com/crowdranked-list/"


def get_list(url: str, class_id: str, sleep: int, scroll: int) -> list:
    """Scrape from ranker.com.

    Parameters
    ----------
    url : str
        url to scrape from
    class_id : str
        html class identifier to extract text from
    sleep : int
        amount of time to pause the scroll
    scroll : int
        amount of total scrolls

    Returns
    -------
    ranks : list
        list of properties scraped from the ranked.com
    """
    browser: any = webdriver.Chrome()

    browser.get(url)
    time.sleep(1)

    elem: any = browser.find_element(By.TAG_NAME, "body")
    counter: int = scroll

    # Scroll
    while counter > 0:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(sleep)
        counter -= 1

    # Extract
    post_elems: list = browser.find_elements(By.CLASS_NAME, class_id)
    ranks: list = [p.text for p in post_elems[:-1]]
    browser.quit()

    return ranks


if __name__ == "__main__":

    # Load environment
    load_dotenv(find_dotenv())

    class_identifier: str = os.environ.get("CLASS_IDENTIFIER", None)
    assert class_identifier is not None, ERROR % "CLASS_IDENTIFIER"
    dest: str = os.environ.get("DEST", None)
    assert dest is not None, ERROR % "DEST"

    # Handle optional arguments
    description: str = (
        'Scrape rankings from ranker.com. '
        'Provide optional arguments for sleep '
        'interval and amount of scrolls.')
    parser: any = argparse.ArgumentParser(
        description=description)
    parser.add_argument(
        '--sleep',
        dest='sleep',
        type=int,
        default=1,
        help='Sleep interval')
    parser.add_argument(
        '--scroll',
        dest='scroll',
        type=int,
        default=100,
        help='Amount of scrolls until end of scrape')
    args: dict = parser.parse_args()

    # Default config
    sleep: int = args.sleep
    scroll: int = args.scroll
    url: str = URL + dest

    # Scrape
    scraped_list: list = get_list(
        url=url,
        class_id=class_identifier,
        sleep=sleep,
        scroll=scroll)

    # Write to file
    filename: str = dest + '_' + str(datetime.datetime.now()) + '.text'
    f = open(filename, "w")
    for element in scraped_list:
        f.write(element + "\n")
    f.close()
