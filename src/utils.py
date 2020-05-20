"""
   Utilization file for scraping environment.

   Includes:
    * get_file_list
"""
import os
from pathlib import Path
from src import scrape_elements
#import scrape_elements

def get_file_list(vendor):
    """
    Reads "html-to-scrape" folder to make a list from *only* html pages.\n
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
    #new_products = {}
    if os.path.exists(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor)):

        file_list =  os.listdir(str(Path(__file__).parent.absolute())+"\\assets\\"+str(vendor))
        for f in file_list:

            if (f.find(".html") < 0):
                print("File "+f+" cannot be scraped because it is not a html file !")
            else:
                #print("xxx"+str(scrape_elements.products))
                scrape_elements.products.get(vendor)['products'][str(os.path.splitext(f)[0])] = str(str((Path(__file__).parent.absolute()))+"\\assets\\"+str(vendor)+"\\"+str(Path(f)))
                #dude wtf ...
                

