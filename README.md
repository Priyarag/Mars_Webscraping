# Mars_Webscraping
Code for a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.
# Web Scraping from the following websites:

https://mars.nasa.gov/news/ 
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars 
https://twitter.com/marswxreport?lang=en 
https://space-facts.com/mars/ 
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 

BeautifulSoup, splinter and python pandas were used to scrape and get data .

# Flask:
Converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape which will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
# /scrape: 
'/scrape' route which will import the Python script and call the scrape function to scrape the mars data.


# route / :
A root route /  is created that will query the Mongo database and pass the mars data into an HTML template to display the data.
A new database and a new collection was created.
All of the scraped data was stored in the above created database.


# HTML and BootStrap: (index.html)
Bootswatch - Slate template is used for the website https://bootswatch.com/slate/ 
Html file 'index.html' is created that displays all of the data in HTML elements.

# Screenshot 1:
![alt text](https://github.com/Priyarag/Mars_Webscraping/blob/master/mars%20images/Screen%20Shot%202019-05-19%20at%2010.55.31%20PM.png)

# Screenshot 2:
![alt text](https://github.com/Priyarag/Mars_Webscraping/blob/master/mars%20images/Screen%20Shot%202019-05-19%20at%2010.55.49%20PM.png)
