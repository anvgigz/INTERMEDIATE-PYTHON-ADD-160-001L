"""
Smart Home Controller Interface

This script serves as the main control interface for managing smart home devices
using object-oriented classes imported from the 'smart_devices' module.

Imported Classes:
- Device
- Light
- LEDLight
- SmartBulb
- Thermostat

Usage:
1. Instantiate devices:
    light = Light("Living Room Light")
    led = LEDLight("Kitchen LED", color="blue")
    bulb = SmartBulb("Bedroom Bulb")
    thermostat = Thermostat("Hallway Thermostat")

2. Control devices:
    light.turn_on()
    light.brightness(75)

    led.set_color("red")
    led.turn_off()

    bulb.set_schedule("07:00", 80)
    bulb.set_schedule("22:00", "off")

    thermostat.set_temperature(85)

3. View device states:
    print(light.status)
    print(bulb.schedule)
    print(thermostat.temperature)

This file can be extended with a user interface or automation logic to simulate
a full smart home environment.

Author: [Your Name]
Date: [Today's Date]
"""





from oop_2_8_composition_vs_inheritance import Light
from oop_2_8_composition_vs_inheritance import LEDLight
from oop_2_8_composition_vs_inheritance import SmartBulb
from oop_2_8_composition_vs_inheritance import Thermostat




class SmartHome:
    """Main class to manage smart home devices using composition."""

    def __init__(self):
        # Create instances of each device
        self.light = Light("Living Room Light")
        self.led_light = LEDLight("Kitchen LED", color="blue")
        self.smart_bulb = SmartBulb("Bedroom Bulb")
        self.thermostat = Thermostat("Hallway Thermostat")

        # Store devices in a dictionary for easy access
        self.devices = {
            "1": ("Light", self.light),
            "2": ("LEDLight", self.led_light),
            "3": ("SmartBulb", self.smart_bulb),
            "4": ("Thermostat", self.thermostat)
        }

    def list_devices(self):
        print("\nSmart Home Devices:")
        for key, (name, _) in self.devices.items():
            print(f"{key}. {name}")
        print("0. Exit")

    def control_device(self, key):
        name, device = self.devices.get(key, (None, None))
        if not device:
            print("Invalid selection.")
            return

        while True:
            print(f"\n--- {name} Control Menu ---")
            print("1. Turn On")
            print("2. Turn Off")

            if isinstance(device, Light):
                print("3. Set Brightness")

            if isinstance(device, LEDLight) or isinstance(device, SmartBulb):
                print("4. Set Color")

            if isinstance(device, SmartBulb):
                print("5. Set Schedule")

            if isinstance(device, Thermostat):
                print("6. Set Temperature")

            print("0. Return to Main Menu")
            choice = input("Select an option: ")

            if choice == "1":
                device.turn_on()
            elif choice == "2":
                device.turn_off()
            elif choice == "3" and isinstance(device, Light):
                try:
                    level = int(input("Enter brightness (0–100): "))
                    device.brightness(level)
                except ValueError:
                    print("Invalid brightness value.")
            elif choice == "4" and hasattr(device, "set_color"):
                color = input("Enter color: ")
                device.set_color(color)
            elif choice == "5" and isinstance(device, SmartBulb):
                time = input("Enter time (e.g., '07:00'): ")
                action = input("Enter action ('on', 'off', or brightness level): ")
                try:
                    action = int(action) if action.isdigit() else action
                    device.set_schedule(time, action)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "6" and isinstance(device, Thermostat):
                try:
                    temp = int(input("Enter temperature (°F): "))
                    device.set_temperature(temp)
                except ValueError:
                    print("Invalid temperature value.")
            elif choice == "0":
                break
            else:
                print("Invalid option.")
                
                
                
def run_smart_home():
    """Launch the Smart Home interactive menu."""
    home = SmartHome()
    while True:
        home.list_devices()
        choice = input("Select a device to control (or 0 to exit): ")

        if choice == "0":
            print("Exiting Smart Home System. Goodbye!")
            break
        else:
            home.control_device(choice)

# Entry point
if __name__ == "__main__":
    run_smart_home()