import re

@qgsfunction(args='auto', group='Custom', referenced_columns=['tags'])
def hstore_contains_key_value(key_value, feature, parent):
    """
    Does key/value exist in hstore_attr?
    Returns True or False
    Usage example: hstore_contains_key_value('amenity=>restaurant')
    """
    hstore_string = feature['tags']
    [key, value] = key_value.split('=>')
    search_string = '"'+key.strip()+'"=>"'+value.strip()+'"' 
    return search_string in hstore_string
