states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# Negative indexes count from the end of the list.
print(states_of_america[0])

# [name list].append() - added new item in list at the and of it
states_of_america.append("dachshund-land")
print(states_of_america[-1])

# list_name.extend([list of new items]) - adds multiple items to the end of the list

states_of_america.extend(["Dachshund-land", "Cat-land", "Dog-land"])
print(states_of_america[-3:])