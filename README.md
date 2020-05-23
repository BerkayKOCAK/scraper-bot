# scraper-bot
This project is about creating a scraper via Python 3.7 using Beautiful Soup 4.9.0

## Requirements & Install
You need to have these following packages in your environment :
beautifulsoup4==4.9.0
PyInquirer==1.0.3
pyfiglet==0.7

To install packages in requirements.txt simply run ;

    pip install -r requirements.txt

## Instructions
   *  Scraping operation needs a html content to work and resumation of this content changes for every vendor.
   *  Thus, decide which vendor websites you want to work first than get their html content.
   *  Html content shall not be vendors main page it must be the page where vendor lists the product
   *  After getting desired content you shall download the page to put into scraping
   *  You shall put the downloaded page under assets folder like =>  assets/vendor-name/product-page.html
   *  After uploading html files, you need to specify which dom elements will be scraped if vendor is not in default vendors.
   *        -Default vendors : hepsiburada, vatan, gittigidiyor, n11, teknosa, mediamarkt, trendyol, akakçe, cimri, istanbulbilişim, amazon.tr 
   *  To modify default vendors you need to go src/scrape_element.py
   *  Product html page names are important because application will categorize by the file names

----------

@ COMING SOON! A page aligner for products with multiple html pages to scrape from same vendor.

@ COMING SOON! A Crawler to get html pages automatically with product name will be implemented.

-----------
