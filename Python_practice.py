
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in  the list of counties.")
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for county in counties_dict:
        print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, str("county has"), voters, str("registered voters."))
voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver", "registered_voters":463353},
                {"county":"Jefferson", "registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)
    for value in county_dict.values():
        print(value)
        
for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,.2f} registered voters.")