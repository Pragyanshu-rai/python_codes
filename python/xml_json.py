# loads function converts/parse the json data into python data
from json import loads

# xml.etree.ElementTree.formstring is used to convert string into an Element 
import xml.etree.ElementTree as xt

def give_json(json_data):
    
    try:
        data = loads(json_data)
        for student in data['student']:
            print("id:-", student['id'], "\nStudent Name:-", student['name'], student['lastname'])
    # if either key or value is missing
    except ValueError as ve:
        print(ve)
        print("Value Error: Key or Value Missing!", json_data)
    except KeyError as ke:
        print(ke)
        print("Key Error: Incorrect or Missing Key!", json_data)
    except Exception as ex:
        print(ex, "\n", json_data)

def give_xml(xml_data):
    
    try:
        data = xt.fromstring(xml_data)
        #finding all the elements "student"
        #findall returns a list of elements
        students = data.findall('student')
        for student in students:
            print("id:-", student.find('id').text, "\nStudent Name:-", student.find('name').text, student.find('lastname').text)    
    # if any tag is missing or is incorrect
    except xt.ParseError as pe:
        print(pe)
        print("Parse Error: Check your xml data \"structure\"\n", xml_data)
    except AttributeError as ae:
        print(ae)
        print("Attribute Error: Tag Not Found!\nPlease check if the tag name is correct.", xml_data)
    except Exception as ex:
        print(ex,'\n', xml_data)

#given xml data as string
xml_data="""<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<student>
		<id>01</id>
		<name>Manish</name>
		<lastname>Panday</lastname>
	</student>
	<student>
		<id>02</id>
		<name>Kunal</name>
		<lastname>Roy</lastname>
	</student>
</root>
"""
xml_data2=xml_data.replace('<student>', '<stu>')
#given json data
json_data='{"student": [{"id": "01", "name": "Manish", "lastname": "Panday"}, {"id": "02", "name": "Kunal", "lastname": "Roy"}]}'
json_data2=json_data.replace('"student":', ':')

print("JSON")
give_json(json_data)

print("XML")
give_xml(xml_data)

print("JSON-2")
give_json(json_data2)

print("XML-2")
give_xml(xml_data2)
