# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "urllib3",
#   "geopy",
# ]
# ///
import geopy.geocoders
import urllib3

def locate(desc):
    locator = geopy.geocoders.Nominatim(user_agent="metuirology").geocode(desc)
    return locator.latitude, locator.longitude

def fetch_forecast(lat, lon):
    location = urllib3.request("GET", f"https://api.weather.gov/points/{lat},{lon}")
    forecast = urllib3.request("GET", location.json()["properties"]["forecast"])
    return [
        "🌨️" if "snow" in (sF := period["shortForecast"].lower()) else 
        "🌧️" if "rain" in sF else
        "☁️" if "cloud" in sF else
        "☀️"
        for period in forecast.json()["properties"]["periods"]
    ]

if __name__ == "__main__":
    import sys
    print("\t".join(fetch_forecast(*locate(sys.argv[1]))))
