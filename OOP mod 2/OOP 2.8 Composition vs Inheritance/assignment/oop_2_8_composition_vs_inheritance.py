



class Device:
    """Represents a generic smart home device with basic on/off functionality."""

    def __init__(self, device_name: str | int | float, status: bool = False) -> None:
        """
        Initialize a Device instance.

        Args:
            device_name (str | int | float): The name or identifier of the device.
            status (bool, optional): The initial status of the device (on/off). Defaults to False.

        Raises:
            TypeError: If device_name is not a string, integer, or float.
            TypeError: If status is not a boolean.
        """
        if not isinstance(device_name, (str, int, float)):
            raise TypeError("device_name must be a string, integer, or float.")
        if not isinstance(status, bool):
            raise TypeError("status must be a boolean.")

        self.device_name = device_name  # Store the device's name or ID
        self.status = status            # Store the device's current status (True for on, False for off)

    def turn_on(self) -> bool:
        """
        Turn the device on.

        Returns:
            bool: The updated status of the device (True).
        """
        self.status = True
        print("Device turned on")
        return self.status

    def turn_off(self) -> bool:
        """
        Turn the device off.

        Returns:
            bool: The updated status of the device (False).
        """
        self.status = False
        print("Device turned off")
        return self.status
    





class Light(Device):
    """A class representing a Light device, inheriting from Device."""

    def __init__(self, device_name, level=50, status=False):
        super().__init__(device_name, status)
        self.level = level

    def brightness(self, level: int) -> int:
        """
        Set the brightness level of the light.

        Args:
            level (int): Desired brightness level.

        Returns:
            int: The adjusted brightness level of the light.
        """
        if not isinstance(level, int):
            raise TypeError("Brightness level must be an integer.")

        # Clamp the brightness level between 0 and 100
        if level < 0:
            level = 0
        elif level > 100:
            level = 100

        self.level = level
        print(f"Light brightness set to {self.level}")
        return self.level





class LEDLight(Light):
    """A class representing an LED Light device, inheriting from Light.

    Args:
        Light (Light): The parent class representing a generic light.
    """
    def __init__(self, device_name, color="white", level=50, status=False):
        super().__init__(device_name, level, status)
        self.color = color
        
    def set_color(self, color="white") -> str:
        """
        Set the color of the LED light.

        Args:
            color (str): Desired color of the LED light.

        Returns:
            str: The updated color of the LED light.
        """
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")

        self.color = color
        print(f"LED Light color set to {self.color}")
        return self.color
    
    
    
    
    
    
class SmartBulb(Light):
    """A class representing a Smart Bulb with scheduling capability."""

    def __init__(self, device_name, level=50, status=False, schedule=None):
        super().__init__(device_name, level, status)
        self.schedule = schedule if schedule is not None else {}

    def set_schedule(self, time: str, action: str | int) -> dict:
        """
        Set a scheduled action for the smart bulb.

        Args:
            time (str): Time of day (e.g., "07:00", "evening", "bedtime").
            action (str | int): Action to perform 
            (e.g., "on", "off", or brightness level as int).

        Returns:
            dict: The updated schedule dictionary.
        """
        if not isinstance(time, str):
            raise TypeError("Time must be a string.")
        if not isinstance(action, (str, int)):
            raise TypeError("Action must be a string or an integer.")

        self.schedule[time] = action
        print(f"Scheduled '{action}' at '{time}'")
        return self.schedule





class Thermostat(Device):
    """Represents a smart thermostat device that controls temperature."""

    def __init__(self, device_name, temperature=72, status=False, current_temp=70):
        """
        Initialize a Thermostat instance.

        Args:
            device_name (str | int | float): The name or identifier of the device.
            temperature (int, optional): Initial desired temperature. Defaults to 72°F.
            status (bool, optional): Initial power status. Defaults to False (off).
            current_temp (int, optional): Current room temperature. Defaults to 70°F.
        """
        super().__init__(device_name, status)
        self.temperature = temperature      # Desired temperature
        self.current_temp = current_temp    # Simulated current room temperature

    def set_temperature(self, temperature: int) -> str:
        """
        Set the desired temperature for the thermostat.

        Args:
            temperature (int): Desired temperature in degrees Fahrenheit.

        Returns:
            str: A message indicating the adjusted temperature and system status.
        
        Raises:
            TypeError: If temperature is not an integer.
        """
        if not isinstance(temperature, int):
            raise TypeError("Temperature must be an integer.")

        # Clamp extreme values
        if temperature > 80:
            temperature = 78
            print("Temperature too high. Setting to 78°F.")
        elif temperature < 60:
            temperature = 65
            print("Temperature too low. Setting to 65°F.")

        self.temperature = temperature

        # Compare desired temperature with current room temperature
        if self.temperature > self.current_temp:
            print(f"Desired temp ({self.temperature}°F) is above current temp ({self.current_temp}°F). Heater turned on.")
            return f"Heater turned on at {self.temperature}°F"
        elif self.temperature < self.current_temp:
            print(f"Desired temp ({self.temperature}°F) is below current temp ({self.current_temp}°F). A/C turned on.")
            return f"A/C turned on at {self.temperature}°F"
        else:
            print(f"Desired temp matches current temp ({self.current_temp}°F). System turned off.")
            return f"System off at {self.temperature}°F"