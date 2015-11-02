import os

BASE_DIR = os.path.dirname(os.path.abspath('__file__')) + '/'

def path(name, type_of_resource='sprite'):
    """Return absolute path to file

    Keyword arguments:
        name -- file name
        type_of_resource - sprite, sound, ...
    """
    if type_of_resource == 'sprite':
        return BASE_DIR + 'assets/sprites/' + name
    elif type_of_resource == 'sound':
        return BASE_DIR + 'assets/sound/' + name