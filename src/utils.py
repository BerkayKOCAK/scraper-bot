"""
   Utilization file for scraping environment.

   Includes:
    * get_file_list
"""
import os
import asyncio
from pathlib import Path
from src import scrape_elements
#import scrape_elements


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
            print("choices : "+str(new_product_selection[0].get("choices")))
            
            for index in new_product_selection[0].get("choices"):
              
                print("index: "+str(index))
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

   

#TODO - implement this when you decide page management
def product_subpage_aligner():
    return 0
