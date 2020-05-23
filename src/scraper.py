
"""
   Main scraping script.

   Includes:
    * scraper_init
    * scraper_queue
    * product_scraper
"""

from bs4 import BeautifulSoup
import re
from src import utils, scrape_elements
from pathlib import Path
import os
import asyncio


async def scraper_init (selected_vendors,selected_products):
    """ Initializer for scraping operation """
    print("SCARAPER STARTS : ")
    for vendor in selected_vendors:
        print(" - Vendor : "+vendor)
        #TODO - check if vendors.products is empty 
        #print("situation : "+str(bool(scrape_elements.products.get(vendor)['products'])))
        await scraper_queue(vendor,selected_products)
    
    #maybe also parallelize vendors instead of a blocking loop
    """await asyncio.gather(
            scraper_queue("A",["hepsiburada"],file_list),
            scraper_queue("B",["hepsiburada"],file_list),
            scraper_queue("C",["hepsiburada"],file_list),
        ) """



async def scraper_queue(vendor,selected_products):
    """ Queues all the scraping tasks to work in parallel.
        Simply appends tasks to a task array and when a task returns, removes it from the arrays .
    """
    count = 0
    tasks = []
    
    try:    
        for productName in selected_products: 
            
            count = count + 1
            fileToOpen =  scrape_elements.products.get(vendor)['products'].get(productName)
            if fileToOpen != None:
                if os.path.isfile(fileToOpen):
                    if(scrape_elements.websites[0].get(str(vendor)) != None):
                        with open(fileToOpen, encoding='utf8') as infile:
                            soup = BeautifulSoup(infile, "html.parser")

                            print("WORKER "+str(count)+" STARTING SCRAPING FOR VENDOR : "+ str(vendor)+" and PRODUCT : "+productName)
                            tasks.append(asyncio.ensure_future(product_scraper(vendor+"_"+str(count), soup, scrape_elements.websites[0].get(vendor), productName )))      
                    else:
                        print(" 000 Cannot Found Vendor "+ vendor +" in mapping ! 000")
                        pass           
                             
                
        #TODO - For bigger data divide task management to batches and limit the parallelized tasks to 10. 
        while tasks:
            print(" **** Tasks are started **** ")
            done, pending = await asyncio.wait(tasks)
            #print(done)
            #print(pending)
            tasks[:] = pending
        print("**** Tasks are ended **** ")

        #for task in tasks:
        #    await task

    except Exception as e:
        print(" @@@@ ERROR IN QUEUE  @@@@ \n MESSAGE : "+ str(e))



async def product_scraper(taskName,soup,website,product):
    """ 
        This is where the magic happens.\n
        It gets dom elements in soup and then finds the desired ones via beautifulsoup\n
        To operate, it needs to know which elements will be scraped thus the website item must include structure similiar to one in scrape_elements.website\n
        #Same applies for the product.
    """
    #print("VENDOR : "+website.get("name")+" PRODUCT : "+product)
    try:
        
        product_elements = soup.find_all(website["product-scope"]["element"], class_= website["product-scope"]["name"])
        regex_title = re.compile(website["child-element"]['title_regex'])
        regex_price = re.compile(website["child-element"]['price_regex'])

        for child in product_elements:
            
            child_title = child.find(website["child-element"]["title"], {"class" : regex_title})
            child_price = child.find(website["child-element"]["price"], {"class" : regex_price})
            child_old_price = child.find(website["child-element"]["old_price"], {"class" : regex_price})
            
            #strip the text from dom element
            #TODO - Write scraped data to a csv
            if child_title:
                print(taskName+" PRODUCT : "+ child_title.text.strip())
            
            if child_price:
                print( taskName+ " PRICE : "+ child_price.text.strip())
            
            if child_old_price:
                print(taskName+ " OLD PRICE : "+ child_old_price.text.strip())
    except Exception as identifier:
        print("ERROR IN" + taskName +" PRODUCT-SCRAPER "+ str(identifier))

