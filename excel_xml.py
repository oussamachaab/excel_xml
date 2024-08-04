import pandas as pd
import xml.etree.ElementTree as ET


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

