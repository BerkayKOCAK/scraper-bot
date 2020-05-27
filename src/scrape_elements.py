"""
    #Websites has different kind of dom elements and management for each unique vendor.
    #Thus you need to add your elements to scrape like default ones. (hepsiburada,vatan,gittigidiyor...) 
    #Website names are case sensitive!
    #Non used items can be NULL.
    Includes:
        * websites
        * products
"""
websites = [
    {
    "hepsiburada" : 
        {
            "name": "hepsiburada",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 'box product'
                },        
            'child-element' : 
            
                {
                    'title': 'h3',
                    'title_regex' : '.*title.*',
                    'price': 'span',
                    'price_regex' : '.*price.*',
                    'old_price': 'del'
                }
        },
    
    "gittigidiyor" : 
        {
            "name": "gittigidiyor",
            'product-scope' : 
            
                {
                    'element': 'li',
                    'name': '.*catalog-seem-cell.*'
                },        
            'child-element' : 
            # #TODO - has multiple ways to present price if you prune product search with more specific product names !!
                {
                    'title': 'h3',
                    'title_regex' : '.*title.*',
                    'price': 'p',
                    'price_regex' : '.*price.*',
                    'old_price': 'strike'
                }
        },
    
    "n11" : 
        {
            "name": "n11",
            'product-scope' : 
            
                {
                    'element': 'li',
                    'name': 'column' #the fuck n11 ?
                },        
            'child-element' : 
            #TODO - "sepette ek indirim" price cannot be encapsulated with below specifications
                {
                    'title': 'h3',
                    'title_regex' : '.*productName.*',
                    'price': 'ins',
                    'price_regex' : None,
                    'old_price': 'del'
                }
        },
    "teknosa" : 
        {
            "name": "teknosa",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 'product-item-inner'
                },        
            'child-element' : 
                {
                    'title': 'div',
                    'title_regex' : 'product-name',
                    'price': 'span',
                    'price_regex' : '.*price.*',
                    'old_price': '' #TODO - old and new price tags are same , 'span'. cant take old one !
                }
        },
    "media_markt" : 
        {
            "name": "media_markt",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 'product-wrapper'
                },        
            'child-element' : 
                {
                    'title': 'div',
                    'title_regex' : 'content', #TODO - takes also details ! try to prune more
                    'price': 'div',
                    'price_regex' : '.*price small length*.',
                    'old_price': '' 
                }
        },
    "trendyol" : 
        {
            "name": "trendyol",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': '.*p-card-wrppr.*'
                },        
            'child-element' : 
                {
                    'title': 'span',
                    'title_regex' : '.*prdct.*', 
                    'price': 'div',
                    'price_regex' : 'prc-box-sllng',
                    'old_price': '' 
                }
        },
     "istanbulbilisim" : 
        {#this website has serious scripting issues, check when you are free !
            "name": "istanbulbilisim",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 'col-xs-6 col-sm-6 col-md-4'
                },        
            'child-element' : 
                {
                    'title': 'p',
                    'title_regex' : '.*title.*', 
                    'price': 'p',
                    'price_regex' : '.*price-act.*',
                    'old_price': 'p' 
                }
        },
    "amazon.tr" : 
        {#this website has serious scripting issues, check when you are free !
            "name": "amazon.tr",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 's-item-container'
                },        
            'child-element' : 
                {
                    'title': 'h2',
                    'title_regex' : '.*title.*', 
                    'price': 'span',
                    'price_regex' : '.*price*',
                    'old_price': '' 
                }
        },
    "vatan" : 
        {
            "name": "vatan",
            'product-scope' : 
            
                {
                    'element': 'div',
                    'name': 'product-list product-list--list-page'
                },        
            'child-element' : 
            
                {
                    'title': 'div',
                    'title_regex' : '.*name.*',
                    'price': 'span',
                    'price_regex' : '.*price.*',
                    'old_price': ''
                }
        }

    }
]

#EXAMPLE USAGE
"""
FOR WEBSITES
    websites = [
        {
        "vendor_name" : 
            {
                "vendor_name_to_call": "examplesite",
                'product-scope' :
                        #This item is for locating listing element in dom content, give its tag and class name to locate.
                        #Example; if products are listed in <ul> tag u need to write its generic <li> element here
                    {
                        'element': 'div',
                        'name': 'box product'
                    },        
                'child-element' : 
                        #This item is for locating listed product element in dom content, give its tag and class name to locate.
                        #Class names are generic with regex to look for word price, title etc. 
                        #Regex is not a must if you are sure class names of the target elements wont change.

                    {
                        'title': 'h3',
                        'title_regex' : '.*title.*',
                        'price': 'span',
                        'price_regex' : '.*price.*',
                        'old_price': 'del'
                    }
            }
        }
    ]
////////////////////////////////////////////////////////////////////////
FOR PRODUCTS :
    products = {
        
        "Hepsiburada" : 
            {
                'products' : {}
                #key: product name, value: file path
            },
        "Vatan" : 
            {
                'products' : {}
                #key: product name, value: file path
            }
}
"""
products = {}

"""
examples:

print(str(products.get("Hepsiburada")))

products.get("Hepsiburada")['key2'] = 'for'

print(str(products.get("Hepsiburada")))

for target_list in products.keys():
   print(str(target_list))

"""