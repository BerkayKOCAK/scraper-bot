   
websites = [
    {
    "Hepsiburada" : 
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
    "Vatan" : 
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
print(str(products.get("Hepsiburada")))
products.get("Hepsiburada")['key2'] = 'for'
print(str(products.get("Hepsiburada")))
for target_list in products.keys():
   print(str(target_list))
"""