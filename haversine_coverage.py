from math import sin, cos, sqrt, atan2, radians


def haversine(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    earthRadius = 6373.0

    #  convert coordinates to radians
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)

    #  calculate longtitude and latitude distances
    lngDistance = lng2 - lng1
    latDistance = lat2 - lat1

    # calculate distance using haversine fomula
    a = sin(latDistance / 2)**2 + cos(lat1) * \
        cos(lat2) * sin(lngDistance / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earthRadius * c


def calculateCoverages(shoppers, locations):
    coverages = []

    for shopper in shoppers:
        #  Make sure the shopper is enabled
        if(shopper['enabled'] != True):
            continue

        covered = 0
        total = len(locations)

        for location in locations:
            #  calculate distance between shopper and location
            distance = haversine(
                shopper['lat'], shopper['lng'], location['lat'], location['lng']
            )

            #  count as covered if distance is less than 10km
            if(distance <= 10):
                covered += 1

        # calculate coverage percentage
        coverage = (covered*100)/total

        # append coverage dictionary to coverages list
        coverages.append({'shopper_id': shopper['id'], 'coverage': coverage})

    #  return list sorted by percentage coverage
    return sorted(coverages, key=lambda k: k['coverage'], reverse=True)


#  test - python haversine_coverage.py
locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02}
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True}
]

print(calculateCoverages(shoppers, locations))
