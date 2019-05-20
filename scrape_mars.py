from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import re
import time

def scrape():
    #Choose the executable path to driver 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_dict = {}
    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(4)
    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    mars_dict['news_title'] = news_title
    news_p = soup.find('div', class_='article_teaser_body').text

    # Display scrapped data 

    mars_dict['news_p'] = news_p
    mars_dict
    ###########JPL Mars Space Images - Featured Imag#####################
    #Visit Mars Space Images through splinter module
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    time.sleep(3)
    html_jpl = browser.html
    soup = BeautifulSoup(html_jpl, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style']
    #print(featured_image_url)
    image_url = re.findall(r"(/spaceimages[^']*\.(?:png|jpg|jpeg|gif|png|svg))", featured_image_url)
    # print(image_url[0])
    # Website Url 
    jplimg_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = f'{jplimg_url}{image_url[0]}'

    # Display full link to featured image
    mars_dict['featured_image_url'] = featured_image_url

    ### Mars Weather ################
    mars_turl = 'https://twitter.com/marswxreport?lang=en'
    mars_twit_req = requests.get(mars_turl)

    #print(mars_twit_req.text)
    mars_soup = BeautifulSoup(mars_twit_req.text, 'html.parser')
    # print(mars_soup)
    mars_weather = re.sub(r'pic.*', "",(mars_soup.find_all(class_='js-tweet-text-container')[0].text))
    # mars_weather = (mars_soup.find(class_='js-tweet-text-container').text)
    mars_dict['mars_weather'] = mars_weather

    ######### Mars Facts #########
    mars_facts = "http://space-facts.com/mars/"

    facts_table = pd.read_html(mars_facts)
    df_facts_table = facts_table[0]
    df_facts_table.columns=["description","value"]
    df_facts_table.set_index(["description"], inplace=True)
    html_table = df_facts_table.to_html()
    #html_table
    html_table = html_table.replace("\n", "")
    html_table
    mars_dict['html_table'] = html_table

    ########## Mars Hemispheres #######
    mars_hemp_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_img_urls = []
    # mars_hemp_req = requests.get(mars_hemp_url)
    browser.visit(mars_hemp_url)
    #Cerberus Hemisphere #
    cerberus_link = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(1) > div > a>h3").click()
    time.sleep(2)
    cerb_html = browser.html
    cerb_soup = BeautifulSoup(cerb_html, 'html.parser')
    #print(cerb_soup)
    cerberus_title = (cerb_soup.find("h2",class_="title").text).strip("Enhanced")
    #print(cerberus_title)
    #soup.find('a', {'class': 'class'})['href'] 
    cerb_relative = cerb_soup.find(class_='wide-image-wrapper').find(href=True)
    cerberus_hemp_full_img = cerb_relative.get('href')
    #print(cerberus_hemp_full_img)
    cerberus = {"image_title":cerberus_title, "image_url": cerberus_hemp_full_img}
    hemisphere_img_urls.append(cerberus)
    browser.back()
    #Schiaparelli Hemisphere
    Schiaparelli_link = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(2) > div > a>h3").click()
    time.sleep(2)
    Schiaparelli_html = browser.html
    Schiaparelli_soup = BeautifulSoup(Schiaparelli_html, 'html.parser')
    #print(cerb_soup)
    Schiaparelli_title = (Schiaparelli_soup.find("h2",class_="title").text).strip("Enhanced")
    #print(Schiaparelli_title)
    #soup.find('a', {'class': 'class'})['href'] 
    Schiaparelli_relative = Schiaparelli_soup.find(class_='wide-image-wrapper').find(href=True)
    Schiaparelli_full_img = Schiaparelli_relative.get('href')
    #print(Schiaparelli_full_img)
    Schiaparelli = {"image_title":Schiaparelli_title, "image_url": Schiaparelli_full_img}
    hemisphere_img_urls.append(Schiaparelli)
    browser.back()
    #Syrtis Major Hemisphere
    Syrtis_link = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(3) > div > a>h3").click()
    time.sleep(2)
    Syrtis_html = browser.html
    Syrtis_soup = BeautifulSoup(Syrtis_html, 'html.parser')
    #print(cerb_soup)
    Syrtis_title = (Syrtis_soup.find("h2",class_="title").text).strip("Enhanced")
    #print(Schiaparelli_title)
    #soup.find('a', {'class': 'class'})['href'] 
    Syrtis_relative = Syrtis_soup.find(class_='wide-image-wrapper').find(href=True)
    Syrtis_full_img = Syrtis_relative.get('href')
    #print(Schiaparelli_full_img)
    Syrtis = {"image_title":Syrtis_title, "image_url": Syrtis_full_img}
    hemisphere_img_urls.append(Syrtis)
    browser.back()
    #print(hemisphere_img_urls)
    #Valles Marineris Hemisphere
    Valles_link = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(4) > div > a >h3").click()
    time.sleep(2)
    #product-section > div.collapsible.results > div:nth-child(4) > div > a > h3
    Valles_html = browser.html
    Valles_soup = BeautifulSoup(Valles_html, 'html.parser')
    #print(cerb_soup)
    Valles_title = (Valles_soup.find("h2",class_="title").text).strip("Enhanced")
    #print(Schiaparelli_title)
    #soup.find('a', {'class': 'class'})['href'] 
    Valles_relative = Valles_soup.find(class_='wide-image-wrapper').find(href=True)
    Valles_full_img = Valles_relative.get('href')
    #print(Schiaparelli_full_img)
    Valles = {"image_title":Valles_title, "image_url": Valles_full_img}
    hemisphere_img_urls.append(Valles)
    mars_dict['hemisphere_img_urls'] = hemisphere_img_urls
    browser.back()    
    #close the browser
    #browser.quit()
    #print(mars_dict)
    return(mars_dict)
