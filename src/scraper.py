
"""
   Main scraping script.

   Includes:
    * scraper_init
"""

from bs4 import BeautifulSoup
import re
from src import utils, scrape_elements
from pathlib import Path
import os
import asyncio
#TODO - comment
async def scraper_init (vendors,selected_products):
    
    for vendor in vendors:
        print("VENDOR : "+vendor)
        file_list = utils.get_file_list(vendor) 
       
        utils.product_file_mapping(vendor)
        print("vendor "+vendor+" products in map : "+str(scrape_elements.products))
        if not file_list:
            print(" No file Found For : "+vendor)
        else:
            await scraper_queue(vendor,file_list,selected_products)
    

    #TODO - maybe parallelize vendors instead of a blocking loop
    """await asyncio.gather(
            scraper_queue("A",["hepsiburada"],file_list),
            scraper_queue("B",["hepsiburada"],file_list),
            scraper_queue("C",["hepsiburada"],file_list),
        ) """

#TODO - review, comment
async def scraper_queue(vendor,file_list,selected_products):

    count = 0
    tasks = []
    
    try:    
        

        for productName in selected_products:
            fileToOpen2 = scrape_elements.products.get(vendor)['products'].get(productName)
            print("fileToOpen2 "+str(productName) )
            print(fileToOpen2)
        #use selected_products to operate
        for target_list in file_list:
            count = count + 1
            fileToOpen = Path(target_list)
            print("file_list : "+str(fileToOpen))  
            print("file_list : "+str(os.path.isfile(fileToOpen)))

            if os.path.isfile(fileToOpen):
                
                if(scrape_elements.websites[0].get(str(vendor)) != None):
                    with open(fileToOpen, encoding='utf8') as infile:
                        soup = BeautifulSoup(infile, "html.parser")

                        print("WORKER "+str(count)+" STARTING SCRAPING FOR VENDOR :"+ str(vendor)+" and PRODUCT : "+str(fileToOpen.name))
                        tasks.append(asyncio.ensure_future(product_scraper(vendor+"_"+str(count), soup, scrape_elements.websites[0].get(vendor), str(fileToOpen.name) )))
                        #TODO - products are unknown, make a mapping between products and files to know what is what.          
                else:
                    print(" 000 Cannot Found Vendor "+ vendor +" in mapping ! 000")
                    pass           
                             
                
        
        while tasks:
            print("Tasks are started")
            done, pending = await asyncio.wait(tasks)
            #print(done)
            #print(pending)
            tasks[:] = pending
        print("Tasks are ended")

        #for task in tasks:
        #    await task

    except Exception as e:
        print(" @@@@ ERROR IN QUEUE  @@@@ \n MESSAGE : "+ str(e))

#TODO - comment
async def product_scraper(taskName,soup,website,product):
    
    print("VENDOR : "+website.get("name")+" PRODUCT : "+product)
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

