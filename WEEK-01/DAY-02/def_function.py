#def 

def check_reading(current_value, minimum_value, maximum_value):
    if current_value >= minimum_value and current_value <= maximum_value:
        return "PASS"
    else:
        return "FAIL"


temperature = float(input("Enter water temperature: "))
ph_level = float(input("Enter pH level: "))

temperature_result = check_reading(temperature, 74, 78)
ph_result = check_reading(ph_level, 6.8, 7.0)

print("Temperature:", temperature_result)
print("pH:", ph_result)