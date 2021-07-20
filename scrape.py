from bs4 import BeautifulSoup as bs
import requests
class Scrape:
    def __init__(self, url, *query):
        self.url = url.format(*query)

    def get_url(self):
        return self.url
    def get_code(self):
        print("Scrapping...")
        html = requests.get(self.url)
        if html.status_code == 200:
            return html.text
        return False
    def get_html(self):
        if self.get_code():
            page = bs(self.get_code(),'html.parser')
            print("Scrapped:)")
            return page
        else:
            print("Not Scrapped:(")

def _(from_ = "INR",to_ = "USD",amount_= 1,url = "https://www.xe.com/currencyconverter/convert/?Amount={}&From={}&To={}"):
    try:
        convert = ''
        page = requests.get(url.format(amount_,from_, to_))
        page = bs(page.text, 'html.parser')
        result = page.find("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        result = str(result.text)
        print("Converted")
        for i in result:
            if i.isdigit() or i == '.':
                convert += i
        return float(convert)
    except:
        return False











