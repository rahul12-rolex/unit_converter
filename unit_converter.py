
def meters_to_kilometers(meters):
    return meters / 1000

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# --- Main Function ---
def main():
    print("Choose conversion:")
    print("1. Meters to Kilometers")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        meters = float(input("Enter meters: "))
        print(f"{meters} m = {meters_to_kilometers(meters)} km")
    elif choice == '2':
        celsius = float(input("Enter °C: "))
        print(f"{celsius}°C = {celsius_