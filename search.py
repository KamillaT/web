import sys
from io import BytesIO
import requests
from PIL import Image
from set_params import set_map_params, set_geocoder_params, set_search_params
import math


toponym_to_find = ' '.join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"
search_api_server = "https://search-maps.yandex.ru/v1/"
geocoder_params = set_geocoder_params(toponym_to_find)
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coordinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coordinates.split(' ')
toponym_coords = ','.join([toponym_longitude, toponym_lattitude])
search_params = set_search_params("аптека", toponym_coords, "biz")
response = requests.get(search_api_server, params=search_params)
if not response:
    pass
json_response = response.json()
orgs = json_response["features"][:10]
org_points = []
for organization in orgs:
    org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    org_point = organization["geometry"]["coordinates"]
    point = [str(org_point[0]), str(org_point[1])]
    if "круглосуточно" in org_time:
        point.append("pmgns")
    elif org_time is None:
        point.append("pmgrs")
    else:
        point.append("pmbls")
    org_points.append(','.join(point))
params = set_map_params(toponym_longitude, toponym_lattitude, org_points)
response = requests.get(map_api_server, params=params)
Image.open(BytesIO(response.content)).show()
