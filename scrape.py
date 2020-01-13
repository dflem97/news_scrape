# Imports 
from bs4 import BeautifulSoup
import requests
import os 

# List of URLS
urls = [r'https://www.bbc.co.uk/news', 
        r'https://edition.cnn.com/',
        r'https://www.dailymail.co.uk/home/index.html]', 
        'https://www.independent.co.uk/']

# Find current working directory
curr_dir = os.getcwd()

# Create output file
f = open(curr_dir + '\webscrape_output.txt', 'w+')

# Select HTML from each URL
for url in urls:
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    tag = 'title'
    title_soup = soup.find(tag)
    
# Write to output file 
    f.write("{}\n".format(title_soup.string))
    
f.close()
    

    
