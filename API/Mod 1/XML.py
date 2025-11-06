

# XML.py"
# cars_for_sale
#          car
#                  id = 1
#                  brand = Ford
#                  model = Mustang
#                  production_year = 1972
#                  price{'currency': 'USD'} = 35900
#          car
#                  id = 2
#                  brand = Aston Martin
#                  model = Rapide
#                  production_year = 2010
#                  price{'currency': 'GBP'} = 32000

# import xml.etree.ElementTree
# import os

# cars_for_sale = xml.etree.ElementTree.parse("C:/Users/skrohn/Documents/INTERMEDIATE-PYTHON-ADD-160-001L-main/API/Mod 1/cars.xml").getroot()
# print(cars_for_sale.tag)
# for car in cars_for_sale.findall('car'):
#     print('\t', car.tag)
#     for prop in car:
#         print('\t\t', prop.tag, end='')
#         if prop.tag == 'price':
#             print(prop.attrib, end='')
#         print(' =', prop.text)


import xml.etree.ElementTree
import os

tree = xml.etree.ElementTree.parse("C:/Users/skrohn/Documents/INTERMEDIATE-PYTHON-ADD-160-001L-main/API/Mod 1/cars.xml")
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')
