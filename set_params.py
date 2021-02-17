def set_map_params(toponym_longitude, toponym_lattitude, points):
    map_params = {
        "ll": ','.join([toponym_longitude, toponym_lattitude]),
        "l": "map",
        "pt": '~'.join(points)}
    return map_params


def set_geocoder_params(toponym_to_find):
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format" : "json"}
    return geocoder_params


def set_search_params(text, address_ll, stype):
    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": text,
        "lang": "ru_RU",
        "ll": address_ll,
        "type": stype}
    return search_params
        


