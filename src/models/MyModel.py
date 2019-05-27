# -*- coding: utf-8 -*-

import src.T_class as TC


def sup_set_bul(value):
    return value == 'Y'


class MyModel(object):
    def __init__(self, my_id, father_id):
        self.my_id = my_id
        self.father_id = father_id
        self.name = None
        self.type_of_elem = None
        self.type = None
        self.noNull = False
        self.primaryKey = False
        self.foreignKey = False
        self.note = None

        self.tc = TC.TClass()

    def setattr(self, name, value):
        arg = self.tc.getTagsNumber(name)

        switch = {
            3: 'set_name'            # 3
            , 4: 'set_type'            # 4
            , 5: 'set_noNULL'          # 5
            , 6: 'set_primaryKey'      # 6
            , 7: 'set_foreignKey'      # 7
            , 8: 'set_note'            # 8
        }

        method = getattr(self, switch.get(arg, 'default_set'))
        method(value)

    def set_name(self, value):
        self.name = value

    def set_type(self, value):
        self.type = self.tc.getTypesNumber(value)

    def set_noNULL(self, value):
        self.noNull = sup_set_bul(value)

    def set_primaryKey(self, value):
        self.primaryKey = sup_set_bul(value)

    def set_foreignKey(self, value):
        self.foreignKey = sup_set_bul(value)

    def set_note(self, value):
        self.note = value

    def default_set(self, value):
        self.set_note(value)