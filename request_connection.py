import requests 
from bs4 import BeautifulSoup
#from WEB_SCRAPE_FUNCS import url_to_soup

def url_to_soup(url):
    page = requests.get(url)
    #parse into beautiful soup format 
    to_soup = BeautifulSoup(page.content, 'html.parser')
    return to_soup

example_input = "Python reverse list"
# get input from noah 

"""content = example_input.split(" ")
to_soup = 'https://stackoverflow.com/search?q='

for ii in content:
    to_soup += content[ii]
    to_soup += '+'

to_soup = url_to_soup(to_soup)"""

to_soup = url_to_soup('https://stackoverflow.com/search?q=python+reverse+list')
# starting to sift through the search results 

# finding all of the search results
answers = to_soup.find_all("div", {"class":"question-summary search-result"})

has_answers = []
# checking for the conditions of if answered, if answered go to url and check for green check and code 
for answer in answers:
    has_answers.extend(answer.find_all("div", {"class":"status answered-accepted"})) 
    
    # if there are answers check each webpage for check mark and if there's a code block

    # opening web page to check 
    link_find = answer.find("a", {"class":"question-hyperlink"})
    
    link = 'https://stackoverflow.com/' + link_find['href']

    to_check = url_to_soup(link)

    # find check mark 
    checked = to_check.find("div", {"class":"lang-py prettyprint prettyprinted"})
    print(checked)

    # check for all <code> tags in the html
    code = to_check.findAll("code")
    print(code)
