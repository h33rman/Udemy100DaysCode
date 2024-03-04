# Nesting Lists and Dictionaries
# # Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nesting a List in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log["France"])
print("-------------------")
print(capitals)
print(travel_log)
print("-------------------")
# Nesting a Dictionary in a List
travel_loglist = [
    {"country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12},
     
    {"country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": 5},
]