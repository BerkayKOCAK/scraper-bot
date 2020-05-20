"""
        SCARAPER-BOT CLI
        Berkay KOÇAK - 2020 May

        CLI Web page scraper for product prices.

Additional libraries:
    *Beautiful Soup 4.9^
    *PyInquirer
    *PyFiglet

"""

from __future__ import print_function, unicode_literals
from src import scraper, utils

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
website_selection = [
    {
        'type': 'checkbox',
        'message': 'Selected Options',
        'name': 'websites',
        'choices': [
            Separator(' = Websites = '),
            {
                'name': 'Hepsiburada',
            },
            {
                'name': 'Gittigidiyor'
            },
            {
                'name': 'n11'
            },
            {
                'name': 'Akakçe'
            },
            {
                'name': 'Vatan'
            },
            {
                'name': 'Teknosa'
            }
           
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

#TODO - get product names from files uploaded and start mapping here.

product_selection = [
    {
        'type': 'checkbox',
        'message': 'Selected Options',
        'name': 'products',
        'choices': [
            Separator(' = Products = '),
            {
                'name': 'Laptop',
            },
            {
                'name': 'Desktop',
                'disabled': 'coming soon!'
            },
            {
                'name': 'Tablet',
                'disabled': 'coming soon!'
            },
            {
                'name': 'Televizyon',
                'disabled': 'coming soon!'
            },
            {
                'name': 'Telefon',
                #'disabled': 'coming soon!'
            },
            {
                'name': 'Tabletler',
                #'disabled': 'coming soon!'
            }
           
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

def main ():
    
    f = Figlet(font='cyberlarge')
    print(f.renderText(' - SCRAPER - '))
    print(f.renderText(' * By Berkay * '))

    while(True):
        websites = prompt(website_selection, style=style1)
        products = prompt(product_selection, style=style2)

        if(len(websites['websites']) != 0 and len(products['products']) != 0):
            pprint(websites['websites'])
            pprint(products)
           
            asyncio.run(scraper.scraper_init(websites['websites'], products['products']))
            #init_scraping()
            break
        else:
            pass

main()