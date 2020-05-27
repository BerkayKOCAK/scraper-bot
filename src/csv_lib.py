"""
    In here there are functions to manage and implement csv features
"""
import csv
import os


#TODO - implement an append functionality for csv write
def write_csv(vendor,product,scrape_array):
    """ creates a output file like "vendor-product.csv" and then writes mapped items in scrape_array"""
    if not os.path.exists('output'):
        os.makedirs('output')
    if not os.path.exists('output/'+vendor):
        os.makedirs('output/'+vendor)
    if os.path.exists('output/'+vendor+'/'+vendor+'-'+product+'.csv'):
        write_mode = 'a'
    else:
        write_mode = 'w'
    f = open('output/'+vendor+'/'+vendor+'-'+product+'.csv', write_mode)
    #if you make write mode append, it will write headers for every new append request !

    with f:
    
        headers = ['productName', 'price(TL)',"old_price(TL)"]
        writer = csv.DictWriter(f, fieldnames=headers) 
        if write_mode == 'w':   
            writer.writeheader()
        for target_list in scrape_array:
            writer.writerow(target_list)

#TODO - make a read func.   
""" Example
        arrayProduct = []
        arrayProduct.append( {'productName' : 'Robert', 'price(TL)': 'Brown'})
        arrayProduct.append( {'productName' : 'TURBOX ATM900110 Intel i5 8GB Ram 240GB Ssd 4GB Ekran Kartı Masaüstü Oyun Bilgisayarı', 'price(TL)': '2.075,00','old_price(TL)':'2.350,00'})
        write_csv("hepsiburada","bilgisayar",arrayProduct)
"""