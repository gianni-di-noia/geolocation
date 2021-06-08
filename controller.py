"""
Geolocation service.
"""
import os
import maxminddb

PATH = os.path.dirname(os.path.realpath(__file__))
DB = maxminddb.open_database(PATH + "/GeoLite2-Country.mmdb")


def search_country(ip_address):
    """Return the closest restaurants from the given lat/lon."""
    data = DB.get(ip_address)
    if not data:
        return None
    try:
        return data["country"]["names"]["en"]
    except TypeError as identifier:
        print("error", identifier)
        return False
    except KeyError as identifier:
        print("error", identifier)
        # print(data)
        return False
    # return country
