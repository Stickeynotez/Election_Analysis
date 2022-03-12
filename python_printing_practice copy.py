counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for county in counties_dict:
        print(counties_dict[county])


#Set for loop as for (county,voters) in 
# (counties_dict.items():) 
# as (Key,value) in (selected_dictionary)
for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,.2f} registered voters.")
