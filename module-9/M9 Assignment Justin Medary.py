import requests


print("TESTING API CONNECTION: ")
try:
    test_response = requests.get("https://www.dnd5eapi.co/api")
    print(f" Connection successful Status: {test_response.status_code}\n")
except Exception as e:
    print(f" Connection failed: {e}\n")
    exit()


print("FETCHING DRAGON DATA: ")
try:
    response = requests.get("https://www.dnd5eapi.co/api/monsters/adult-black-dragon")
    data = response.json()

    print("RAW RESPONSE: ")
    print(data)

    print("FORMATTED DRAGON: ")
    print(f"Name: {data['name']}")
    print(f"Size: {data['size']}")
    print(f"Type: {data['type']}")
    print(f"Challenge Rating: {data['challenge_rating']}")
    print(f"Hit Points: {data['hit_points']}")
    print("\nAbilities:")
    for ability in data['special_abilities'][:3]:
        print(f"- {ability['name']}")

        

except Exception as e:
    print(f"Error: {e}")
