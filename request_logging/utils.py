"""Utilities for the django_request_logging module"""
from django.utils.safestring import mark_safe

def clean_dict(data):
    """
    converts all items to unicode, so that
    it can de json serialized
    """
    data = dict(data)
    for key, value in data.items():
        data[key] = unicode(value)
    return data

def format_as_table(data):
    """
    formats dictionary as HTML table
    """
    output = ''
    for key in data:
        row = '<tr><td>%s</td><td>%s</td></tr>' % (key, data[key])
        output += row
    return mark_safe('<table>'+ output + '</table>')

def replace_dict_values(the_dict, keys, replacement):
    """
    replaces values in dictionary for keys
    if present in the dictionary
    """
    for key in keys:
        if key in the_dict:
            the_dict[key] = replacement


def import_attribute(path):
    """
    given path x.y.z
    does the same as statement
    from x.y import z

    Code copied from appconfig.utils.import_attribute and simplified
    https://github.com/jezdez/django-appconf/blob/develop/appconf/utils.py
    """
    try:
        from importlib import import_module
    except ImportError:
        from django.utils.importlib import import_module
    module_name, object_name = path.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)
