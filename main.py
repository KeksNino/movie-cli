from bs4 import BeautifulSoup
import requests

def xprime_scraper():
    query = input("Enter search query: ")
    url = "https://xprime.tv/search?query=" + query
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a', href=True)
    
    for link in links:
        print(link['href'])

if __name__ == "__main__":
    xprime_scraper()
