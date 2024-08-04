import pandas as pd
from lxml import etree as et
import os
import openpyxl
import xml.etree.ElementTree as ET
'''
raw_data = pd.read_excel(r'Grades.xlsx')  #read excel
print(raw_data)

root = et.Element('odoo')                   #create odoo balise
root_tags0 = et.SubElement(root, 'data',  no_update="1")    #create data balise
print(root) 

for row in raw_data.iterrows():                         #loop for each tag
    root_tags = et.SubElement(root_tags0, 'record', id="artec_produit" , model="product product")     #=== > employe Root name
    print(root_tags)

# These are the tag names for each row (SECTION 1)
    Column_heading_1 = et.SubElement(root_tags, 'field', name="Name")
    Column_heading_2 = et.SubElement(root_tags, 'field', name="active", eval="acive")
    Column_heading_3 = et.SubElement(root_tags, 'filed', name="price")

###These are the values that will be populated for each row above
# The values inside the [] are the raw file column headings.(SECTION 2)
    Column_heading_1.text = str(row[1]['Name'])
    Column_heading_2.text = str(row[1]['active'])
    Column_heading_3.text = str(row[1]['price'])

for record in root.iter('id'):

    new_rank = int(record.text) + 1

    record.text = str(new_rank)

    record.set('updated', 'yes')

tree = et.ElementTree(root) #==> The variable tree is to hold all the values of "root"
et.indent(tree, space="\t", level=0) #===> This just formats in a way that the XML is readable
tree.write('output.xml', encoding="utf-8") #==> The data is saved to an XML file
'''



r_data = pd.read_excel(r'Grades.xlsx')  #read excel
print(r_data)

odoo = ET.Element('odoo')                   #create odoo tag
data = ET.SubElement(odoo, 'data',  no_update="1")    #create data tag
print(odoo) 

for id, row in r_data.iterrows():    #looping the rows 
    
    product_name = row['Name']
    print(product_name)
    record_id = f"Artec_product_{product_name}"
    record_model = f"product_product"
                          
    record = ET.SubElement(data, 'record', id = record_id , model = record_model)
    print(record)
        
    for field in r_data:
        field_value = row[field]  #values from rows
        print(field)
        print(field_value)

        if field == 'active': 

            if field_value == 'True':
                eval_value = '1'
            else :  
                eval_value= '0'

            ET.SubElement(record, 'field', name = field, eval = f"{eval_value}")
            print(eval_value)

        else: 
            field_element = ET.SubElement(record, 'field', name=field )
            field_element.text = str(field_value)
            print(field_element.text)
            
tree = ET.ElementTree(odoo)
tree.write('xml_final.xml') 



'''

raw_data = pd.read_excel(r'Grades.xlsx')  #read excel
print(raw_data)

root = et.Element('odoo')                   #create odoo balise
root_tags0 = et.SubElement(root, 'data',  no_update="1")    #create data balise
print(root) 

for row in raw_data.iterrows():                         #loop for each tag
    root_tags = et.SubElement(root_tags0, 'record', id="artec_produit" , model="product product")     #=== > employe Root name
    print(root_tags)

# These are the tag names for each row (SECTION 1)
    Column_heading_1 = et.SubElement(root_tags, 'field', name="Name")
    Column_heading_2 = et.SubElement(root_tags, 'field', name="active", eval="acive")
    Column_heading_3 = et.SubElement(root_tags, 'filed', name="price")

###These are the values that will be populated for each row above
# The values inside the [] are the raw file column headings.(SECTION 2)
    Column_heading_1.text = str(row[1]['Name'])
    Column_heading_2 = row[1]['active']
    Column_heading_3.text = str(row[1]['price'])


tree = et.ElementTree(root) #==> The variable tree is to hold all the values of "root"
et.indent(tree, space="\t", level=0) #===> This just formats in a way that the XML is readable
tree.write('output.xml', encoding="utf-8") #==> The data is saved to an XML file

'''