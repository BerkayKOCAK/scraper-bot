from bs4 import BeautifulSoup
import re

def test_parser_page(filename):
    with open(filename, encoding='utf8') as infile:
        soup = BeautifulSoup(infile, "html.parser")
    #you can reach hepsiburada-computer by https://www.hepsiburada.com/bilgisayarlar-c-2147483646

    print(soup.title)
    #find all nodes in dom with tag "a"
    for child in soup.find_all("a"):
        if child.string == "Bilgisayar":
            print(child.string)
            print(child.contents)
            print(child['href'])
        else:
            pass
            #print(child.string)


def test_parser_product(filename):
    
    with open(filename, encoding='utf8') as infile:
        soup = BeautifulSoup(infile, "html.parser")
    
    #find all div elements with class name "xxx"
    product_elements = soup.find_all("div", class_= 'box product')
    
    #regex for desired substrings/names in elements
    regex_title = re.compile('.*title.*')
    regex_price = re.compile('.*price.*')

    for child in product_elements:
          
        child_title = child.find("h3", {"class" : regex_title})
        child_price = child.find("span", {"class" : regex_price})
        child_old_price = child.find("del", {"class" : regex_price})
        
        #strip the text from dom element
        if child_title:
            print("PRODUCT : "+ child_title.text.strip())
        
        if child_price:
            print("PRICE : "+ child_price.text.strip())
        
        if child_old_price:
            print("OLD PRICE : "+ child_old_price.text.strip())
            

        
        
#test_parser_page("Hepsiburada.html")
test_parser_product("hepsiburada-example/Bilgisayar.html")

#print(soup.find_all("a"))
#soup = BeautifulSoup("<html>data</html>")