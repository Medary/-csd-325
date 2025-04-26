def city_country(city_name, country_name, population=None, language=None):
    if population and language:
        return f"{city_name}, {country_name} - population {population}, {language}"
    elif population:
        return f"{city_name}, {country_name} - population {population}"
    elif language:
        return f"{city_name}, {country_name}, {language}"
    else:
        return f"{city_name}, {country_name}"


location1 = city_country("Santiago", "Chile", population=8000000, language="Spanish")
location2 = city_country("New York", "United States", population=8000000)
location3 = city_country("London", "United Kingdom", population=9000000, language="English")

print(location1)
print(location2)
print(location3)







