# -*- coding: utf-8 -*-

import src.T_class as TC
import src.models.MyModel as MM
import xml.etree.cElementTree as ET


class XMLReader(object):
    def __init__(self, path):
        self.path = path
        self.list = []
        self.tc = TC.TClass()

    def parse_xml(self):
        tree = ET.ElementTree(file=self.path)
        root = tree.getroot()
        self.get_element(root, -1)

    def get_element(self,  elem, fi):
        el_type = self.tc.getTagsNumber(elem.tag)

        method = getattr(self, self.switch(el_type))
        method(elem, fi)

    """Switch methods begin"""

    def switch(self, arg):
        switch = {
            0: 'get_entity'
            , 1: 'get_field'
            , 2: 'get_function'
        }

        return switch.get(arg, 'method_def')

    def get_entity(self, elem, fi):
        my_id = len(self.list)
        model = MM.MyModel(my_id, fi)
        model.type_of_elem = self.tc.tags.index(elem.tag)
        # model.name = elem.attrib
        model.name = elem.get('name')

        self.list.append(model)

        for element in elem:
            self.get_element(element, my_id)

    def get_field(self, elem, fi):
        my_id = len(self.list)
        model = MM.MyModel(my_id, fi)
        model.type_of_elem = self.tc.tags.index(elem.tag)

        for attribute in elem:
            model.setattr(attribute.tag, attribute.text)

        self.list.append(model)

    def get_function(self, elem, fi):
       self.get_field(elem, fi) #fixme !!!!!!!!!!!!!!!!!!

    def method_def(self, elem, fi):
        print('Method not exist!')

    """Switch methods end"""


if __name__ == '__main__':
    reader = XMLReader(r'C:\Python\Projects\ModelCoder_data\123.xml')
    reader.parse_xml()

    for i in reader.list:
        print(i.my_id, i.father_id, i.name)
        print('\t\ttype_of_elem\t', TC.TClass().tags[i.type_of_elem])
        if i.type is not None:
            print('\t\ttype\t\t\t', TC.TClass().types[i.type])
        if i.noNull:
            print('\t\tnoNULL\t\t\t Y')
        if i.primaryKey:
            print('\t\tprimaryKey\t\t Y')
        if i.foreignKey:
            print('\t\tforeignKey\t\t Y')
        if i.note is not None:
            print('\t\tnote\t\t\t', i.note)
        print()
