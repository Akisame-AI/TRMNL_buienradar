import pandas as pd
from geopy.distance import geodesic

# User's coordinates
user_coords = (52.0, 4.7)

# List of stations with coordinates
stations = [
    {"stationname": "Meetstation Arcen", "lat": 51.5, "lon": 6.2},
    {"stationname": "Meetstation Arnhem", "lat": 52.07, "lon": 5.88},
    {"stationname": "Meetstation Berkhout", "lat": 52.65, "lon": 4.98},
    {"stationname": "Meetstation De Bilt", "lat": 52.1, "lon": 5.18},
    {"stationname": "Meetstation Den Helder", "lat": 52.92, "lon": 4.78},
    {"stationname": "Meetstation Eindhoven", "lat": 51.45, "lon": 5.42},
    {"stationname": "Meetstation Ell", "lat": 51.2, "lon": 5.77},
    {"stationname": "Meetstation Gilze Rijen", "lat": 51.57, "lon": 4.93},
    {"stationname": "Meetstation Goes", "lat": 51.53, "lon": 3.9},
    {"stationname": "Meetstation Groenlo-Hupsel", "lat": 52.07, "lon": 6.65},
    {"stationname": "Meetstation Groningen", "lat": 53.13, "lon": 6.58},
    {"stationname": "Meetstation Heino", "lat": 52.43, "lon": 6.27},
    {"stationname": "Meetstation Herwijnen", "lat": 51.87, "lon": 5.15},
    {"stationname": "Meetstation Hoek van Holland", "lat": 51.98, "lon": 4.1},
    {"stationname": "Meetstation Hoogeveen", "lat": 52.73, "lon": 6.52},
    {"stationname": "Meetstation Hoorn Terschelling", "lat": 53.38, "lon": 5.35},
    {"stationname": "Meetstation Houtribdijk", "lat": 52.65, "lon": 5.4},
    {"stationname": "Meetstation IJmuiden", "lat": 52.47, "lon": 4.57},
    {"stationname": "Meetstation Lauwersoog", "lat": 53.42, "lon": 6.2},
    {"stationname": "Meetstation Leeuwarden", "lat": 53.22, "lon": 5.77},
    {"stationname": "Meetstation Lelystad", "lat": 52.45, "lon": 5.53},
    {"stationname": "Meetstation Lopik-Cabauw", "lat": 51.97, "lon": 4.93},
    {"stationname": "Meetstation Maastricht", "lat": 50.92, "lon": 5.78},
    {"stationname": "Meetstation Marknesse", "lat": 52.7, "lon": 5.88},
    {"stationname": "Meetstation Nieuw Beerta", "lat": 53.2, "lon": 7.15},
    {"stationname": "Meetstation Rotterdam", "lat": 51.95, "lon": 4.45},
    {"stationname": "Meetstation Rotterdam Geulhaven", "lat": 51.88, "lon": 4.32},
    {"stationname": "Meetstation Schiphol", "lat": 52.3, "lon": 4.77},
    {"stationname": "Meetstation Stavoren", "lat": 52.88, "lon": 5.38},
    {"stationname": "Meetstation Texelhors", "lat": 53, "lon": 4.75},
    {"stationname": "Meetstation Twente", "lat": 52.27, "lon": 6.9},
    {"stationname": "Meetstation Vlieland", "lat": 53.25, "lon": 4.92},
    {"stationname": "Meetstation Vlissingen", "lat": 51.45, "lon": 3.6},
    {"stationname": "Meetstation Volkel", "lat": 51.65, "lon": 5.7},
    {"stationname": "Meetstation Voorschoten", "lat": 52.12, "lon": 4.43},
    {"stationname": "Meetstation Westdorpe", "lat": 51.23, "lon": 3.83},
    {"stationname": "Meetstation Wijdenes", "lat": 52.63, "lon": 5.17},
    {"stationname": "Meetstation Wijk aan Zee", "lat": 52.5, "lon": 4.6},
    {"stationname": "Meetstation Woensdrecht", "lat": 51.45, "lon": 4.33},
    {"stationname": "Meetstation Zeeplatform F-3", "lat": 54.85, "lon": 4.73},
]

# Calculate distances
for station in stations:
    station_coords = (station["lat"], station["lon"])
    station["distance"] = geodesic(user_coords, station_coords).kilometers

# Find the closest station
closest_station = min(stations, key=lambda x: x["distance"])
print(closest_station)
