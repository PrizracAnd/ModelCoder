# -*- coding: utf-8 -*-

import src.T_class
import xml.etree.cElementTree as ET

class XMLReader(object):
    def __init__(self, path):
        self.path = path

    def parseXML(self, xml_file):
        root = ET.ElementTree(file= xml_file).getroot()
