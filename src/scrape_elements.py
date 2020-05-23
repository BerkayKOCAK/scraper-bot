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