import scrape
from bs4 import BeautifulSoup as bs
url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
web_url = "https://www.flipkart.com"
scraper = scrape.Scrape
def Result(url,convert,*search_object):
    ### scrape
    page = scraper(url, *search_object)
    page = page.get_html()
    
    ###  get count of products
    
    get_content_pages = page.find("div", class_="_2MImiq")
    get_content_pages =get_content_pages.find("span").text
    get_content_pages_count = ''
    for i in get_content_pages:
        if i.isdigit():
            get_content_pages_count += i
    get_content_page_id = int(get_content_pages_count[0])
    get_content_pages_count = int(get_content_pages_count[1:])
    
    ### get position of  contents
    contents_position = page.find_all("div", class_="_13oc-S")
    results = []
    for result in contents_position:
        for item in result.find_all("div",style="width:25%"):
            results.append(item)
        for item in result.find_all("div",style="width:100%"):
            results.append(item)
            
    ### get contents
    id = 1
    contents = {}
    contents["page_id"] = get_content_page_id
    if convert != 0:
        for content in results:

            contents[id] = {}
            content_url = content.find("a")["href"]
            content_img_url = content.find("img")["src"]
            title  = content.find("img")["alt"]
            price  = content.find("div", class_="_30jeq3").text[1:]
        
        
            contents[id]["url"]=web_url + str(content_url)
            contents[id]["image"]= str(content_img_url)
            contents[id]["title"]= str(title)
            price = float(str(price).replace(',',''))  * convert
            contents[id]["price"]= round(price)
        
            id += 1
    else:
        contents["results"] = get_content_pages_count
    return  contents

class get_all:
    def __init__(self, search_text ):
        self.url = url
        self.search = search_text

    def get(self):
        scrape_data = {}
        try:
            data = Result(self.url,0, self.search)
        except:
            return False
        ### convert
        convert = scrape._()
        if convert == False:
            while True:
                print("Xatolik:converter")

        if data:
            scrape_data["results"] = data["results"]
            for i in range(data["results"]):
                page_id = i + 1
                result = Result(self.url + "&page={}",convert, self.search, page_id)
                scrape_data[page_id] = result

            return scrape_data
    


























