"""
        SCARAPER-BOT CLI
        Berkay KOÇAK - 2020 May

        CLI Web page scraper for product prices.

Written with Python 3.7.3
Additional libraries:
    *Beautiful Soup 4.9^
    *PyInquirer
    *PyFiglet

"""

from __future__ import print_function, unicode_literals
from src import scraper, utils, scrape_elements

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import Figlet
import asyncio

style1 = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

style2 = style_from_dict({
    Token.Separator: '#33FFEC',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#33FFEC',  # default
    Token.Pointer: '#AF601A bold',
    Token.Instruction: '#EC7063',  # defaults
    Token.Answer: '#AF601A bold',
    Token.Question: '#EC7063',
})
template_vendor_selection = [
    {
        'type': 'checkbox',
        'message': 'Selected Options',
        'name': 'vendors', #name of selected items array
        'choices': [
            Separator(' = Vendors = ')
           
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]


template_product_selection = [
    {
        'type': 'checkbox',
        'message': 'Selected Options',
        'name': 'products',
        'choices': [
            Separator(' = Products = ')
    
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

def main ():
    
    f = Figlet(font='cyberlarge')
    print(f.renderText(' - SCRAPER - '))
    print(f.renderText(' * By Berkay * '))


    try:
        utils.vendor_folder_mapping()
        vendor_selection = utils.menu_add_vendors(template_vendor_selection)
    except Exception as identifier:
        print(" - ERROR AT MAPPING INITALIZE -")
        print(identifier)
    
    while(True):
        
        vendors = prompt(vendor_selection, style=style1)
        if(len(vendors['vendors']) != 0):
            print("Selected Vendors : "+str(vendors['vendors']))
            asyncio.run(utils.timeout(1))

            for vendor in vendors['vendors']:
                utils.product_file_mapping(vendor)
            
            print(scrape_elements.products)
            product_selection = utils.menu_add_products(template_product_selection)
            if(len(product_selection[0].get("choices"))>1):
                products = prompt(product_selection, style=style2)
                if (len(products['products']) != 0):
                    print("Selected Products : "+str(products['products']))
                    asyncio.run(utils.timeout(1))
                    asyncio.run(scraper.scraper_init(vendors['vendors'], products['products']))
            else:#maybe throw this during mapping
                print("No Product File Found For Vendor : "+str(vendors['vendors']))
            break
        else:
            pass

main()
