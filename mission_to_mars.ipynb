# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_par = mars_news(browser)

    # URL of page to be scraped
    url ="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

#
    news_title ="NASA Readies Perseverance Mars Rover's Earthly Twin"

    news_par="Did you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape."

    featured_image="https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA14417_ip.jpg"

    mars_facts="https://space-facts.com/mars/"

    tables = pd.read_html(mars_facts)
    tables

    type(tables)

    df=tables[0]
    df.columns=['0','1']
    #['Equatorial Diameter','Polar Diameter','Mass','Moons','Orbit Distance',
            #'Orbit Period','Surface Temperature','First Record','Recorded By']

    df.head(9)

    mars_html=df.to_html()

    mars_html

    #create dictionaries
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url":"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]

    data = {
        "news_title":news_title,
        "news_par":news_par,
        "featured_image":featured_image,
        "facts":mars_facts,
        "hemispheres":hemisphere_image_urls
    }
    return data
