#Dependencies
import os
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    ##NASA MARS NEWS
    #Visit NASA Mars News site in the Browser
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    #Grab html code as string
    nasa_html = browser.html
    #Translate to html as bs object
    nasa_soup = bs(nasa_html, 'html.parser')

    #Find latest article title
    title_div = nasa_soup.find("div", class_="content_title")
    #Get title text
    nasa_title = title_div.find("a").text

    #Find <p> for article
    nasa_p = nasa_soup.find("div", class_="article_teaser_body").text

    ##JPL MARS SPACE
    #Visit JPL Mars Space site in the Browser
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    #Grab html code as string
    jpl_html = browser.html
    #Translate to html as bs object
    jpl_soup = bs(jpl_html, 'html.parser')

    #Find Featured Mars img
    img_article = jpl_soup.find("article", class_="carousel_item")
    img_style = img_article['style']
    img_split = img_style.split("'")
    featured_img_url = 'https://www.jpl.nasa.gov' + img_split[1]

    #MARS WEATHER TWITTER
    #Visit Mars Weather Twitter page in the Browser
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    #Grab html code as string
    weather_html = browser.html
    #Translate to html as bs object
    weather_soup = bs(weather_html, 'html.parser')

    #Find latest tweet
    tweet_div = weather_soup.find("div", class_="js-tweet-text-container")
    #Get the text
    mars_weather = tweet_div.find("p").text
    print(mars_weather)

    #MARS FACTS TABLE
    #Visit Mars Weather Twitter page in the Browser
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    #Read in tables from the page w/ pandas
    fact_table = pd.read_html(facts_url)
    #Choose the Mars fact table
    fact_df = fact_table[1]

    #HTML code string
    fact_html = fact_df.to_html()

    #MARS HEMISPHERES (USGS)
    #Visit USGS Astrogeology page in the Browser
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

    #Grab html code as string
    usgs_html = browser.html
    #Translate to html as bs object
    usgs_soup = bs(usgs_html, 'html.parser')

    #Initialize list of for hemisphere info
    usgs_imgs = []

    #Find div with hemisphere links
    hemispheres = usgs_soup.find_all("div", class_="item")

    #Loop through each hemisphere page link
    for hemisphere in hemispheres:
        #Get hemisphere partial link
        hem_a = hemisphere.a['href']
        #Complete hemisphere link
        hem_href = 'https://astrogeology.usgs.gov' + hem_a
        #Visit hemisphere page
        browser.visit(hem_href)
        
        #Grab html code of each page as a string
        hem_html = browser.html
        #Translate to html as bs object
        hem_soup = bs(hem_html, "html.parser")
        
        #Get hemisphere title (save to variable)
        img_title = hem_soup.find("h2", class_="title").text
        
        #Get hemisphere img url (save to variable)
        half_img_url = hem_soup.find("img", class_="wide-image")["src"]
        img_url = 'https://astrogeology.usgs.gov' + half_img_url
        
        #Put title and img variables into dictionary
        hem = { 'title': img_title,
                'img_url': img_url}
        #Append dictionary to list
        usgs_imgs.append(hem)

    mars_data = {
        "nasa_title":"nasa_title",
        "nasa_p":"nasa_p",
        "jpl_img": "featured_img_url",
        "tweet": "mars_weather",
        "fact_table": "fact_html",
        "hemispheres": "usgs_imgs"
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

print("done that thang")

