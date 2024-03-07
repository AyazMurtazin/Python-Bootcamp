NORM_JSON_DATA = {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 8,
    "armed": True,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"},
                    {"first_name": "Alana", "last_name": "Sheparda", "rank": "Commandera"}]
}
DUPLICAT_JSON_DATA = {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 8,
    "armed": True,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"},
                    {"first_name": "Alana", "last_name": "Sheparda", "rank": "Commandera"}]
}
DUPLICAT_JSON_DATA_WITH_DIFFER1 = {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 220,
    "crew_size": 8,
    "armed": True,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"},
                    {"first_name": "Alana", "last_name": "Sheparda", "rank": "Commandera"}]
}
DUPLICAT_JSON_DATA_WITH_DIFFER2 = {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 9,
    "armed": True,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"},
                    {"first_name": "Alana", "last_name": "Sheparda", "rank": "Commandera"}]
}
JSON_DATA_WITH_IMPOSTOR = {
    "alignment": "Enemy",
    "name": "Normndy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 8,
    "armed": True,
    "officers": [{"first_name": "Alan", "last_name": "Shepard", "rank": "Commander"}]
}