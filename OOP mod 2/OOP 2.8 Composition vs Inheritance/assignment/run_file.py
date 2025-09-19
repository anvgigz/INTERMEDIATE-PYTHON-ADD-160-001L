from SmartHome import SmartHome


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
