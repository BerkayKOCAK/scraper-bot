
"""
   Main scraping script.

   Includes:
    * scraper_init
"""

from bs4 import BeautifulSoup
import re
import utils
import scrape_elements
from pathlib import Path
import os
import asyncio

async def scraper_init (vendors):
    
    #TODO - get file list for selected vendors
    file_list = utils.get_file_list()

    #TODO - maybe parallelize vendors instead of blocking loop
    for vendor in vendors:
        await scraper_queue(vendor,file_list)

    """await asyncio.gather(
        scraper_queue("A",["hepsiburada"],file_list),
        scraper_queue("B",["hepsiburada"],file_list),
        scraper_queue("C",["hepsiburada"],file_list),
    ) """


async def scraper_queue(vendor,file_list):

    count = 0
    tasks = []

    try:
       
        #for key in scrape_elements.websites[0].keys():
            
        for target_list in file_list:
            count = count + 1
            fileToOpen = Path(target_list)  
            if os.path.isfile(fileToOpen):
                 with open(fileToOpen, encoding='utf8') as infile:
                    soup = BeautifulSoup(infile, "html.parser")

                    print(str(count)+" STARTING SCRAPING FOR VENDOR :"+ str(vendor)+"\nPRODUCT : "+str(fileToOpen.name))
                    tasks.append(asyncio.ensure_future(product_scraper(vendor+str(count), soup,scrape_elements.websites[0][str(vendor)] )))
                    #TODO - products are unknown, make a mapping between products and files to know what is what.          
                              
                             
                
        
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

async def product_scraper(taskName,soup,website):
    
    """
    if taskName == "1":
        await asyncio.sleep(5)
    elif taskName == "2":
        await asyncio.sleep(10)
    elif taskName == "3":
        await asyncio.sleep(3)
    """
    try:
        
        product_elements = soup.find_all(website["product-scope"]["element"], class_= website["product-scope"]["name"])
        regex_title = re.compile('.*title.*')
        regex_price = re.compile('.*price.*')

        for child in product_elements:
            
            child_title = child.find(website["child-element"]["title"], {"class" : regex_title})
            child_price = child.find(website["child-element"]["price"], {"class" : regex_price})
            child_old_price = child.find(website["child-element"]["old_price"], {"class" : regex_price})
            
            #strip the text from dom element
            if child_title:
                print(taskName+" PRODUCT : "+ child_title.text.strip())
            
            if child_price:
                print( taskName+ " PRICE : "+ child_price.text.strip())
            
            if child_old_price:
                print(taskName+ " OLD PRICE : "+ child_old_price.text.strip())
    except Exception as identifier:
        print("ERROR IN" + taskName +" PRODUCT-SCRAPER "+ str(identifier))

asyncio.run(scraper_init(["hepsiburada","vatan"]))