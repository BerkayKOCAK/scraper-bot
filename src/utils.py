"""
   Utilization file for scraping environment.

   Includes:
    * get_file_list
    * product_file_mapping
    * vendor_folder_mapping
    * menu_add_vendors
    * menu_add_products
    * timeout
"""
import os
import asyncio
from pathlib import Path
from src import scrape_elements
#import scrape_elements
from termcolor import colored 


def get_file_list(vendor):
    """
    Reads given vendor folder to make a list from *only* html pages.\n
    Returns file paths. 
    """
    arranged_file_list = []
    #print("CWD : "+ str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor))
    if os.path.exists(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor)):
        
        file_list =  os.listdir(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor))
        for f in file_list:
            if f.find(".html") < 0:
                print("File "+f+" cannot be scraped because it is not a html file !")
                
            else:
                arranged_file_list.append(str((Path(__file__).parent.absolute()))+"\\assets\\"+str(vendor)+"\\"+str(Path(f)))
                #wow ! worst path management ever dumbass. make it generic.

    return arranged_file_list



def product_file_mapping(vendor):
    """ 
    Maps the files with respect to product names.\n
    Categorizes via vendor names.
    """
    if os.path.exists(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor)):

        file_list =  os.listdir(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor))
        for f in file_list:

            if (f.find(".html") < 0):
                print("File "+f+" cannot be scraped because it is not a html file !")
            else:
                scrape_elements.products.get(vendor)['products'][str(os.path.splitext(f)[0])] = str(str((Path(__file__).parent.absolute()))+"\\assets\\"+str(vendor)+"\\"+str(Path(f)))
                #dude wtf ...



#TODO - comment
def vendor_folder_mapping():

    folder_list = os.listdir(str(Path(__file__).parent.absolute())+"\\assets\\")
    if (len(folder_list) == 0):
        raise Exception(" - NO VENDOR FOUND - \nPlease read instructions again!")
    else:
        for folder in folder_list:
            scrape_elements.products[folder] = {"products":{}}
 
    

def menu_add_vendors(vendor_selection):
    """
    #Adds vendors to choices array at vendor_selection dict. as follows,
        'choices': [
                    Separator(' = Products = '),
                    {
                        'name': 'Hepsiburada',
                    },
                    {
                        'name': 'Vatan',
                        "disabled":"cause"
                        ...
                    },
                    ...
    """    
    new_vendor_selection = vendor_selection
    
    for vendor in scrape_elements.products.keys():
        temp = {"name":vendor}#,"disabled":"cause"}
        new_vendor_selection[0].get("choices").append(temp)
    return new_vendor_selection



def menu_add_products(product_selection):
    """
    #Adds products to choices array at product_selection dict. as follows,
        'choices': [
                    Separator(' = Products = '),
                    {
                        'name': 'Vatan',
                        "disabled":"cause"
                        ...
                    },
                    ...
    """    
    new_product_selection = product_selection
    flag = 0
    for vendor in scrape_elements.products.keys():
        
        for product in scrape_elements.products.get(vendor)['products'].keys():
            flag = 0
            temp = {"name":product}#,"disabled":"cause"}
            #print("choices : "+str(new_product_selection[0].get("choices")))
            
            for index in new_product_selection[0].get("choices"):
              
                #print("index: "+str(index))
                if hasattr(index, 'get'):
                    if product == index.get("name"): 
                        flag = 1   
                        break
            if flag == 0:
                new_product_selection[0].get("choices").append(temp)

    return new_product_selection




async def timeout(time):
    """Simple timeout, takes time as seconds"""
    await asyncio.sleep(time)

def instructions():
    print(colored('Welcome to scraper-bot', 'green'), colored('\nInstructions : ', 'yellow'))
    print(colored('     * ', 'red'), colored('Scraping operation needs a html content to work and implementation of this content changes for every vendor.', 'cyan'))
    print(colored('     * ', 'red'), colored('Thus, decide which vendor websites you want to work first than get their html content.', 'cyan'))
    print(colored('     * ', 'red'), colored('Html content shall not be vendors main page it must be the page where vendor lists the product', 'cyan'))
    print(colored('     * ', 'red'), colored('After getting desired content you shall download the page to put into scraping', 'cyan'))
    print(colored('     * ', 'red'), colored('You shall put the downloaded page under assets folder like => ','cyan'), colored ('assets/vendor-name/product-page.html','cyan',attrs=['bold','underline']))
    print(colored('     * ', 'red'), colored('After uploading html files, you need to specify which dom elements will be scraped if vendor is not in default vendors.', 'cyan'))
    print(colored('     * ', 'red'), colored('  -Default vendors : hepsiburada, vatan, gittigidiyor, n11, teknosa, mediamarkt, trendyol, akakçe, cimri, istanbulbilişim, amazon.tr ', 'magenta'))
    print(colored('     * ', 'red'), colored('To modify default vendors you need to go src/scrape_element.py', 'cyan'))
    print(colored('     * ', 'red'), colored('Product html page names are important because application will categorize by the file names', 'cyan'))
    print(colored('-------------------------------------------------------------------------------------------------------------------------------', 'grey'))
    print(colored('@ COMING SOON! A page aligner for products with multiple html pages to scrape from same vendor', 'blue'))
    print(colored('@ COMING SOON! A Crawler to get html pages automatically with product name will be implemented', 'blue'))
    print(colored('-------------------------------------------------------------------------------------------------------------------------------', 'grey'))
    #print(colored('     * ', 'red'), colored('', 'cyan'))
    

#TODO - implement this when you decide page management
def product_subpage_aligner():
    return 0
