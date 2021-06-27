# Import libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
import ast
import time
import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Start time
start_time = time.time()

# Read all categories from Trustpilot
file = open("dictionary_categories.txt", "r")

contents = file.read()
dictionary_categories = ast.literal_eval(contents)

file.close()


"""
Get details of companies including:
  1- path link for each company, for example: '/review/kapao.fr'
  2- name of company
  3- code postal
  4- number of reviews
  5- score number
and return them into a dictionary.
"""


def scraping_companies(soup):
    Dict_category = {}
    find_pages = soup.find_all('div', class_="styles_categoryBusinessListWrapper__2H2X5")
    # path link for each company
    for val in find_pages:
        for v in val:
            Dict_company = {}
            ln = v.get('href')
            if str(ln).startswith('/review'):

                # name of company
                name = v.find_all('div', class_="styles_businessTitle__1IANo")
                if len(name) != 0:
                    n = str(name[0]).split('1IANo">')
                    name_company = n[1].split('</')[0]
                    Dict_company['name_company'] = name_company

                # code postal
                zip = v.find_all('span', class_="styles_locationZipcodeAndCity__2RbYT")

                if len(zip) != 0:
                    z = str(zip[0]).split('<span>')
                    code_postal = z[1].split('<')[0]
                    Dict_company['code_postale'] = code_postal
                else:
                    Dict_company['code_postale'] = 0

                # number of reviews
                score = v.find_all('div', class_="styles_textRating__19_fv")
                if len(score) != 0:
                    s = str(score[0]).split('fv">')
                    number_reviews = s[1].split('avis')[0]
                    Dict_company['number_reviews'] = number_reviews

                    # score number
                    t = str(score[0]).split('TrustScore')
                    trust_score = t[1].split('</')[0]
                    Dict_company['score'] = trust_score
                else:
                    Dict_company['number_reviews'] = 0
                    Dict_company['score'] = 0
            Dict_category[ln] = Dict_company

    return Dict_category


"""
Use scraping_companies(soup) to get all details of each company for each category and
the number of pages you want to scrape, then stock them into Dict_categories.
"""


def list_category(category_name: str, number_page: int) -> dict:
    Dict_categories = {}
    url = "https://fr.trustpilot.com/categories/" + category_name

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    for p in np.arange(1, number_page, 1):
        print(p)
        if p == 1:
            page_source1 = driver.page_source
            soup1 = BeautifulSoup(page_source1, 'lxml')
            Dict_categories.update(scraping_companies(soup1))
        else:
            driver.find_element_by_xpath(f'//*[@href="/categories/beauty_wellbeing?page={p}"]').click()
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')

            Dict_categories.update(scraping_companies(soup))
    return Dict_categories


"""
Stock all elements into sub of lists
"""
account_c = []
dates_c = []
stars_c = []
headings_c = []
reviews_c = []
name_companies_c = []

"""
Scrape Beautifulsoup source for each page web
"""


def scraping(soup_source):
    review_div1 = soup_source.find_all('div', class_="review-content")

    # loop to iterate through each reviews
    for container in review_div1:
        # Get the body of the review
        nv = container.find_all('p', attrs={'class': 'review-content__text'})
        review = container.p.text if len(nv) == True else '-'
        reviews_c.append(review)

        # Get the title of the review
        nv1 = container.find_all('h2', attrs={'class': 'review-content__title'})
        heading = container.a.text if len(nv1) == True else '-'
        headings_c.append(heading)

        # Get the star rating review given
        star = container.find("div", {"class": "star-rating star-rating--medium"}).find('img').get('alt')
        stars_c.append(star)

        # Get the date
        date_json = json.loads(container.find('script').string)
        date = date_json['publishedDate']
        dates_c.append(date)


"""
This function performs all scraping of the selected category
"""


def scraping_trustpilot_category(category: str, number_pages: int):
    account_c.append(category)

    Dic = list_category(category, number_pages)

    for k, key in enumerate(list(Dic.keys())):
        print(key)
        name_companies_c.append(Dic[key]['name_company'])

        url = "https://fr.trustpilot.com" + key
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

        page_source2 = driver.page_source
        soup = BeautifulSoup(page_source2, 'lxml')
        time.sleep(5)

        scraping(soup)
        time.sleep(5)

        anchors = soup.find_all('a', {'class': 'button button--primary next-page', 'href': True})
        time.sleep(3)

        for anchor in anchors:
            href = anchor['href']
            driver.find_element_by_xpath(f'//*[@href="{href}"]').click()
            time.sleep(3)
            page0 = driver.page_source
            soup0 = BeautifulSoup(page0, 'lxml')
            scraping(soup0)
            time.sleep(3)

            anchors0 = soup0.find_all('a', {'class': 'button button--primary next-page', 'href': True})
            for anchor in anchors0:
                href0 = anchor['href']
                driver.find_element_by_xpath(f'//*[@href="{href0}"]').click()
                time.sleep(3)
                page1 = driver.page_source
                soup1 = BeautifulSoup(page1, 'lxml')
                scraping(soup1)
                time.sleep(3)

                anchors1 = soup1.find_all('a', {'class': 'button button--primary next-page', 'href': True})
                for anchor in anchors1:
                    href1 = anchor['href']
                    driver.find_element_by_xpath(f'//*[@href="{href1}"]').click()
                    time.sleep(3)
                    page2 = driver.page_source
                    soup2 = BeautifulSoup(page2, 'lxml')
                    scraping(soup2)
                    time.sleep(5)


def save_dataframe(category: str):
    # dictionary of lists
    dict = {'title': headings_c, 'comments': reviews_c, 'stars': stars_c, 'time': dates_c}
    df = pd.DataFrame(dict)

    # saving the dataframe
    df.to_csv(category+'.csv')


if __name__ == '__main__':
    # Initialize the Parser
    parser = argparse.ArgumentParser()

    # Add the parameters positional/optional
    parser.add_argument('-c', '--category_name', help='add category name', type=str)
    parser.add_argument('-p', '--page_number', help='add page number', type=int)

    # Parse the arguments
    args = parser.parse_args()

    if args.category_name in dictionary_categories.values():
        scraping_trustpilot_category(args.category_name, args.page_number)
        save_dataframe(args.category_name)
    else:
        print("The name of categories not exist!, you could find the list of categories name in "
              "dictionary_categories.txt")

    print("The running time is:", "%s seconds" % (time.time() - start_time))
