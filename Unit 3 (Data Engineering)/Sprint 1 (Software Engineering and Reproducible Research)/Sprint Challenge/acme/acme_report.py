from acme import Product
import random
import numpy as np
import pandas as pd

'''Ramdomly generates products and return an inventory report
    with the information of those products'''


adjetives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved', 'Magic']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Pen', 'Cube', 'Trap']


def generate_products(list1 = adjetives, list2 = nouns, n_products = 30):

    '''Takes a list of adjetives and a list of nouns as first and second parameter
        and generates as many random names of products as
        indicated in the 3rd parameter (default 30)'''

    # empty list to append random names    
    products_list = []

    # generating random names from list1 and list2
    for i in range(n_products):     
        item1 = random.choice(list1)
        item2 = random.choice(list2)
        new_product = str(item1) + ' ' + str(item2)
        products_list.append(new_product)
    return products_list



def inventory_report(p_list):

    '''Takes a list of product names then instantiates each
        using Product class, assign random values to
        the features of each product and return a 
        summary report using df with products information'''

    # empty dic to create df    
    report_dic = {}

    # empty lists to append ramdom values and fill report_dic
    price_list = []
    weight_list = []
    flammability_list = []
    id_list = []
    p_name_list = []

    # instantiating and creating random values and appending
    for i in p_list:
        price = np.random.randint(5,101)
        weight = np.random.randint(5,101)
        flammability = round(np.random.uniform(0.0,2.5), 1)

        prod = Product(i)
        prod.price = price
        prod.weight = weight
        prod.flammability = flammability

        id_list.append(prod.identifier)
        p_name_list.append(prod.name)
        price_list.append(prod.price)
        weight_list.append(prod.weight)
        flammability_list.append(prod.flammability)
        
    # filling report_dic and creating df
    report_dic['id'] =  id_list
    report_dic['Name'] =  p_name_list
    report_dic['Price'] =  price_list
    report_dic['Weight'] =  weight_list
    report_dic['Flammability'] =  flammability_list

    report_df = pd.DataFrame(report_dic)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f"Unique Product Names: {report_df['Name'].nunique()}")
    print(f"Average Price: {round(report_df['Price'].mean(), 2)}")
    print(f"Average Weight: {report_df['Weight'].mean()}")
    print(f"Average Flammability: {report_df['Flammability'].mean()}")    


inventory_report(generate_products())



    