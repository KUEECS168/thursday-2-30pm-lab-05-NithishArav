'''
Author: Nithish Aravinthan
KUID: 3211410
Date: 3/3/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: Log visited planets and find neighbors for a specified planet
'''


planets = []

is_entering_planets = True

while is_entering_planets:
    planet = input("Enter planet name: ")
    planets.append(planet)

    if input("Is the mission over? (y/n): ").upper() == "Y":
        is_entering_planets = False

planet_choice = input("Which planets do you want to see neighbors for?: ")

planet_index = -1

for i in range(len(planets)):
    if planet_choice.upper() == planets[i].upper():
        planet_index = i

if planet_index == -1:
    print("Bad input: planet not in flight plan")
else:
    neighbors = []
    lower_index = planet_index - 1
    if lower_index >= 0:
        neighbors.append(planets[lower_index])
    
    upper_index = planet_index + 1
    if upper_index < len(planets):
        neighbors.append(planets[upper_index])

    if len(neighbors) == 0:
        print(f"No planets neighbors {planet_choice}")
    else:
        print(f"Planets neighboring {planet_choice}:")
        for planet in neighbors:
            print(f"\t{planet}")

print("\nProgram ending . . .")
