from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

def suggestions_by_keyword(user_query):
    
    search_text = { "q": user_query}
    urllib.parse.urlencode(search_text)
    final_url = "https://www.google.com/search?" + urllib.parse.urlencode(search_text)

    
    #https://support.google.com/webmasters/answer/1061943?hl=en
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }

    req = urllib.request.Request(final_url, None, headers)

    response = urlopen(req)
    page = response.read()
    response.close() 

    soup = BeautifulSoup(page,'html.parser')
    cat = soup.find_all("div",attrs={'class': "wwUB2c"})
    for c in cat:
        caa = c.find_all("span")
        cat = caa[0].text
        
    suggestions = soup.find_all("div",attrs={'class': "oBrLN"})
    
    list_of_suggestions = []
    for i in range(len(suggestions)):
        list_of_suggestions.append(suggestions[i].text)
    return cat,list_of_suggestions


suggestions_by_keyword(input())
