# -*- coding: utf-8 -*-

"""
    Created by Demjanov 16.06.2019
"""
import src.models.Model as model


class JavaModel(model):
    ext = 'java'
    types = {
        'boolean':  -2
        , 'short':  -2
        , 'byte':   -2
        , 'int':    0
        , 'long':   0
        , 'float':  -2
        , 'double': -2
        , 'string': 1
    }

    @staticmethod
    def get_filename(file_name):
        fn = file_name[:1].upper + file_name[1:] if file_name is not None else None
        return fn

    def get_declare_attr(self, my_model, tab=None, isnote=False):
        strt = self.get_type(my_model.type)
        res = None
        if strt is not None and my_model.name is not None:
            res = tab + strt + ' ' + my_model.name + ';'

        if isnote and res is not None:
            res += '\t// '
            res += 'Not Null, ' + my_model.note if my_model.noNull else my_model.note

        return res

    def get_function(self, my_model, tab=None):
        res = None
        if my_model.name is not None:
            res = tab + '// ' + my_model.name

        if res is not None:
            if my_model.note is not None:
                res += '\t' + my_model.note

            res += '\n' + tab
            strt = self.get_type(my_model.type)

            if strt is not None:
                res += strt + ' ' + my_model.name + '(){'
                res += '\n' + tab + '\t'
                res += 'return Null;' if my_model.type == 1 else 'return 0;'
            else:
                res += 'void ' + my_model.name + '(){'

            res += '\n' + tab + '}'
