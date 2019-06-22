# -*- coding: utf-8 -*-

import os
"""
    Created by Demjanov 16.06.2019
"""


class FileSaver (object):
    def __init__(self, path, name, ext):
        self.path = path
        self.name = name
        self.ext = ext
        self.err = None

    """Method save"""
    def save(self):
        l = False
        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            f = open(self.get_path(), 'w')
            f.close()
        except FileExistsError:
            self.err = 'попытка создания файла или директории, которая уже существует'
        except FileNotFoundError:
            self.err = 'файл или директория не существует'
        except InterruptedError:
            self.err = 'системный вызов прерван входящим сигналом'
        except IsADirectoryError:
            self.err = 'ожидался файл, но это директория'
        except NotADirectoryError:
            self.err = 'ожидалась директория, но это файл'
        except PermissionError:
            self.err = 'не хватает прав доступа'
        except OSError:
            self.err = 'неизвестная системная ошибка'
        except Exception:
            self.err = 'неизвестно, что пошло не так'
        else:
            l = True
        finally:
            return l

    """Getters"""
    def get_path(self):
        os_names = ([
            'posix'
            , 'nt'
            , 'mac'
            , 'os2'
            , 'ce'
            , 'java'
        ])

        os_name = os.name
        n = os_names.index(os_name) if os_name in os_names else -1

        slash = r'\ ' if (n == 1 or n == -1) else r'/ '
        return self.path + slash[:1] + self.name + '.' + self.ext

    def get_error_message(self):
        return self.err


if __name__ == '__main__':
    fs = FileSaver(r'C:\Python\Projects\ModelCoder_data\TestSave1', 'test', 'txt')
    s = 'Ok\n' + fs.get_path() if fs.save() else fs.err
    print(s)
