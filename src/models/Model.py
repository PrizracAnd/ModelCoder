# -*- coding: utf-8 -*-

"""
    Created by Demjanov 16.06.2019

    This is base class for data models in any languages
"""
import src.models.MyModel as MM


class Model(object):
    """
        This is Data block

        This most by contained:

            -- ext - extension of result files;

            -- types - glossary of types in next format:
                {value : key of suitable type in T_class}

                example:
                types = {
                    int: 0
                    , string: 1
                    , text: 1
                }
    """

    ext = None  # must be override!!!
    types = {}  # must be override!!!

    """
        This is methods bloc
    """

    def get_type(self, type_key):

        for v, k in enumerate(self.types):
            if k == type_key:
                return v
        return None

    def get_types(self, type_key):
        strt = None
        for v, k in enumerate(self.types):
            if k == type_key:
                strt = v if strt is None else strt + ';' + v

        return strt

    # def identify_method(self, elem_type):
    #     switcher = {
    #         0: 'get_filename'
    #         , 1: 'get_declare_attr'
    #         , 2: 'get_function'
    #     }

    # must be override!!!
    @staticmethod
    def get_filename(file_name):
        pass

    # must be override!!!
    @staticmethod
    def get_declare_attr(my_model):
        pass

    # must be override!!!
    @staticmethod
    def get_function(my_model):
        pass
