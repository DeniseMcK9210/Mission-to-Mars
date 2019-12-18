# Mission to Mars
A web application that scrapes various websites for news, images, weather and facts related to the Mission to Mars and displays the information in a single HTML page.

### Data Sources
* [NASA's Latest Mars News] (https://mars.nasa.gov/news/)
* [JPL Featured Mars Space Image] (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
* [Mars Weather's Latest Tweet] (https://twitter.com/marswxreport?lang=en)
* [Mars Facts] (https://space-facts.com/mars/)
* [USGS Astrogeology Mars Hemispheres] (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

### The Site (screenshots)
![Mission to Mars1](/Screenshots/Mars1.png)
![Mission to Mars2](/Screenshots/Mars2.png)

### The Process
1. Designed HTML5 page with CSS3 and Bootstrap5.
2. Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
3. MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the data sources.
