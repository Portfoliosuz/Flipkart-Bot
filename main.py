import scrape
url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
page_url = url + "&page={}"
web_url = url[:24]
scraper = scrape.Scrape
def get(convert,*search_object):
    convert = scrape._()
    page_ = scraper(page_url, *search_object)
    page = page_.get_html()
    contents_position = page.find_all("div", class_="_13oc-S")
    contents = {}
    contents["page_id"] = search_object[1]
    id = 1
    def get_product(id,content):
        contents[id] = {}
        content_url = content.find("a")["href"]
        content_img_url = content.find("img")["src"]
        title = content.find("img")["alt"]
        price = content.find("div", class_="_30jeq3").text[1:]
        contents[id]["url"] = web_url + str(content_url)
        contents[id]["image"] = str(content_img_url)
        contents[id]["title"] = str(title)
        price = float(str(price).replace(',', '')) * convert
        contents[id]["price"] = round(price)
    for result in contents_position:
        for content in result.find_all("div", style="width:25%"):
            get_product(id,content)
            id += 1
        for content in result.find_all("div", style="width:100%"):
            get_product(id, content)
            id += 1
    return contents

def get_pages_count(*search_object):
    page = scraper(url, *search_object)
    page = page.get_html()
    get_content_pages = page.find("div", class_="_2MImiq")
    get_content_pages = get_content_pages.find("span").text
    get_content_pages_count = ''
    for i in get_content_pages:
        if i.isdigit():
            get_content_pages_count += i
    results = int(get_content_pages_count[1:])
    return results
def get_all_contents(search_text):
    convert = scrape._()
    if convert == False:
            return False
    contents = {}
    count = get_pages_count(search_text)
    contents["results"] = count
    for content in range(count):
        contents[content+1] = get(convert,search_text,content+1)
    return contents
















