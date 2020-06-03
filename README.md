# scraper-bot
Local scraper application. Offline use cases only at the moment but will support online data gathering from websites soon.

## Requirements & Install
You need to have these following packages in your environment :

*beautifulsoup4==4.9.0

*PyInquirer==1.0.3

*pyfiglet==0.7


To install packages in requirements.txt simply run ;

    pip install -r requirements.txt

## Documentation

### Instructions
   *  Scraping operation needs a html content to work and implementation of this content changes for every vendor.
   *  Thus, decide which vendor websites you want to work first than get their html content.
   *  Html content shall not be vendors main page it must be the page where vendor lists the product
   *  After getting desired content you shall download the page to put into scraping
   *  You shall put the downloaded page under assets folder like =>  assets/vendor-name/product-page.html
   *  After uploading html files, you need to specify which dom elements will be scraped if vendor is not in default vendors.
           **Default vendors :** hepsiburada, vatan, gittigidiyor, n11, teknosa, mediamarkt, trendyol, akakçe, cimri, istanbulbilişim, amazon.tr 
   *  To modify default vendors you need to go src/scrape_element.py
   *  Product html page names are important because application will categorize by the file names
   
#### Example Assets
You can find example web pages of default vendors in following link; https://drive.google.com/drive/folders/1rtpoT3sJrdUf2UDkZgZNZ5NBcMQMvE22?usp=sharing

### Multiple Pages For A Product
   *  Page management handled via regex and labeling.
   *  For example; 
        Lets say there is  bilgisayar.html,  bilgisayar_1.html, bilgisayar_2.html files.
        It takes bilgisayar.html as category and adds it as "bilgisayar". Then if other files includes "bilgisayar" as substring and "_" symbol, it aligns them as sub-pages.
        
        *Category name must NOT include "_"  
        
        *Sub pages which belongs to a category must include "_"
        
  (Folder based categorization might be implemented instead of symbol labeling)

----------

@ COMING SOON! A Crawler to get html pages automatically with product name will be implemented.

-----------
