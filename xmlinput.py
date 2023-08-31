import xmltodict
import json
xml_filename = input("enter xml file:")
with open(xml_filename, 'r') as xml_file:
    xml_content = xml_file.read()
    xml_dict = xmltodict.parse(xml_content)
    json_data = json.dumps(xml_dict,indent = 4)
print(json_data)

