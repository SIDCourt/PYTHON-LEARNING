#DAY 02 - Aquaponics automation
# water levels
# use def command for multiple functions

def check_water_temperature(current_water_temp_f):
    water_temp_minimum_f= 74 
    water_temp_maximum_f = 78 
    if current_water_temp_f > water_temp_maximum_f:
        print(f"The water is too hot, at {current_water_temp_f}F.")
    elif current_water_temp_f < water_temp_minimum_f:
        print(f"The water is too cold, at {current_water_temp_f}F.")
    else:
        print(f"The water temperature is just right, at {current_water_temp_f}F.")




# pH level
pH_minimum = 6.8
pH_maximum = 7.0

current_pH = float(input("What is the current pH level? "))
if current_pH > pH_maximum:
    print(f"The water is too alkaline, at {current_pH}.")
elif current_pH < pH_minimum:
    print(f"The water is too acidic, at {current_pH}.")
else:
    print(f"The pH level is just right, at {current_pH}.")


# dissolved oxygen in mg/L
dissolved_oxygen_minimum = 6.5
dissolved_oxygen_maximum = 8.0

current_dissolved_oxygen = float(input("What is the current dissolved oxygen level in mg/L? "))
if current_dissolved_oxygen > dissolved_oxygen_maximum:
    print(f"The water has too much dissolved oxygen, at {current_dissolved_oxygen} mg/L.")
elif current_dissolved_oxygen < dissolved_oxygen_minimum:
    print(f"The water has too little dissolved oxygen, at {current_dissolved_oxygen} mg/L.")
else:
    print(f"The dissolved oxygen level is just right, at {current_dissolved_oxygen} mg/L.")