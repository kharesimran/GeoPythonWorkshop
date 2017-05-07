import re

@qgsfunction(args='auto', group='Custom', referenced_columns=['tags'])
def hstore_get_value(key, feature, parent):
    """
    Give the key, return its value.
    If the key does not exist, return an empty string
    Usage example: hstore_get_value('addr:street')
    """
    hstore_string = feature['tags']
    reg_exp = '"'+key+'"=>"(.+?)"'
    re_output = re.search(reg_exp, hstore_string)
    if re_output:
    	value = re_output.group(1)
    else:
    	value = key + ' not known'
    return value
