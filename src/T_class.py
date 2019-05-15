# -*- coding: utf-8 -*-

class TClass(object):
    def __init__(self):
        self.tags = ([
            "entity"            # 0
            , "field"           # 1
            , "function"        # 2
            , "name"            # 3
            , "type"            # 4
            , "noNULL"          # 5
            , "primaryKey"      # 6
            , "foreignKey"      # 7
            , "note"            # 8
        ])

        self.types = ([
            "int"               # 0
            , "string"          # 1
            # , "function"        # 2
            # , "name"            # 3
            # , "type"            # 4
            # , "noNULL"          # 5
            # , "primaryKey"      # 6
            # , "foreignKey"      # 7
            # , "note"            # 8
        ])

    def getTagsNumber(self, tag):
        n = -1
        for i, v in enumerate(self.tags):
            if v == tag:
                n = i
        return n

    def getTypesNumber(self, type):
        n = -1
        for i, v in enumerate(self.types):
            if v == type:
                n = i
        return n

