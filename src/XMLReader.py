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
        # elements = root.getchildren()
        self.get_element(root, -1)

    def get_element(self,  elem, fi):
        # element = ET.ElementTree(elem)



        #model = MM.MyModel(len(self.list), fi)
        el_type = self.tc.getTagsNumber(elem.tag)

        method = getattr(self, self.switch(el_type), lambda : 'method_def')
        method(elem, fi)

    """Switch methods begin"""

    def switch(self, arg):
        switch = {
            0: 'get_entity'
            # , 1: 'method_1'
            # , 2: 'method_2'
        }

        default = 'method_def_1'

        if arg > len(switch):
            return default

        return switch.get(arg, lambda : 'method_def')

    def get_entity(self, elem, fi):
        my_id = len(self.list)
        model = MM.MyModel(my_id, fi)
        model.type = self.tc.tags.index(elem.tag)
        model.name = elem.attrib

        self.list.append(model)

        # for element in elem.getchildren:
        #     self.get_element(element, my_id)

    # def method_2(self, elem):

    def method_def(self, elem, fi):
        print('Method not exist!')

    """Switch methods end"""


if __name__ == '__main__':
    reader = XMLReader(r'C:\Python\Projects\ModelCoder_data\123.xml')
    reader.parse_xml()

    for i in reader.list:
        print(i.type, i.name)
