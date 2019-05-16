# -*- coding: utf-8 -*-

import src.T_class
import src.models.MyModel as MM
import xml.etree.cElementTree as ET


class XMLReader(object):
    def __init__(self, path):
        self.path = path
        self.list = []

    def parseXML(self, xml_file):
        tree = ET.ElementTree(file=xml_file)
        root = tree.getroot()
        elements = root.getchildren()

    def getElement(self, elem, fi):
        element = ET.ElementTree(elem)

        model = MM.MyModel(len(self.list), fi)


    """Switch methods begin"""

    def methodSwitch(self, arg):
        switch = {
            0: 'method_0'
            , 1: 'method_1'
            , 2: 'method_2'
        }

        default = 'method_def_1'

        if arg > len(switch):
            return default

        return switch.get(arg)


    def method_0(self):
        return 'method_0'


    def method_1(self):
        return 'method_1'


    def method_2(self):
        return 'method_2'


    def method_def(self):
        return 'Method not exist!'


    def execMethod(self, arg):
        from _ast import Lambda
        method = getattr(self, self.methodSwitch(arg), lambda : 'method_def')
        return method()


    """Switch methods end"""
