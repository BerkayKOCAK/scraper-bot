"""
   Utilization file for scraping environment.

   Includes:
    * get_file_list
"""
import os
from pathlib import Path

def get_file_list():
    """
    Reads "html-to-scrape" folder to make a list from *only* html pages.\n
    Returns file paths. 
    """
    arranged_file_list = []

    if os.path.exists(str(Path(__file__).parent.absolute())+"\\assets\\html-to-scrape"):
        
        file_list =  os.listdir("assets\\html-to-scrape")
        for f in file_list:
            if f.find(".html") < 0:
                print("File "+f+" cannot be scraped because it is not a html file !")
                
            else:
                arranged_file_list.append(str((Path(f).parent.absolute()))+"\\assets\\html-to-scrape\\"+str(Path(f)))
                #wow ! worst path management ever dumbass. make it generic.

    return arranged_file_list



