#!/usr/bin/env python
import json, sys
countries = ["guatemala", "mexico", "costa_rica", "panama", "columbia",\
             "venezuela", "nicaragua", "honduras", "ethiopia","kenya",\
             "peru","brazil"]

country_geojson = {}
country_data = {}
country_regions = {}
coffee_geojson = {
    u'type': u'Feature Collection', 
    u'features': list() 
    }

for country in countries:
    try:
        open_f = open("./{}.json".format(country))
    except:
        open_f = open("./geojson/{}.json".format(country))
    lines = json.loads(open_f.read())
    open_f.close()
    
    for element in lines['elements']:
        if 'custom' in element.keys():
            if 'map_json' in element['custom'].keys():
                country_geojson[country] = element['custom']['map_json']
                country_data[country] = element['data']
    
    country_regions[country] = [region[0] for region in country_data[country][0] if (region[2].lower() in ['coffee growing region', 'coffee growing regions', 'arabica', 'robusta']) or (region[2].lower().startswith("group"))]
    #try:
    coffee_geojson['features'].extend([feature for feature in country_geojson[country]['features'] if feature['properties']['name'] in country_regions[country]])
    #except Exception as e:
    #    print>>sys.stderr, e
        