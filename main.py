# Sources: http://docs.python-requests.org/en/master/user/quickstart/
#          https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Author: Lim Heng
# Retrieve job listings from craigslist.com
# Only for educational and tutorial purposes only

import requests
from bs4 import BeautifulSoup
import sys


def con_url(url):
    """ Send a get request to specified url. """
    return requests.get(url)

def get_soup(html):
    """ Get all job categories and corresponding links. """
    soup = BeautifulSoup(html.content, 'lxml')
    return soup

def get_jobs(links, url):
    """ Get all job categories and corresponding links. """
    names = []
    urls = []

    jobs = links.find_all('ul', {'id': 'jjj0'})
    links = jobs[0].find_all('a')

    for link in links:
        names.append(link.text)
        urls.append(url + link.get('href'))

    return names, urls

def main():
    url ='https://austin.craigslist.org'

    link_names = []
    link_urls = []

    html = con_url(url)
    soup = get_soup(html)
    link_names, link_urls = get_jobs(soup, url)

    print(link_names)
    print(link_urls)

if __name__ == '__main__':
    main()
