"""
Smart Home Controller Interface

This script provides a command-line user interface (UI) for interacting with smart home devices.
Users can control devices such as lights, LED lights, smart bulbs, and thermostats using a menu system.

How to Use:
-----------
1. Run the script in a terminal or command prompt.
2. The main menu will display a list of available smart home devices.
3. Enter the number corresponding to the device you want to control.
4. A submenu will appear with options specific to that device:
   - Turn On / Turn Off
   - Set Brightness (for Light, LEDLight, SmartBulb)
   - Set Color (for LEDLight, SmartBulb)
   - Set Schedule (for SmartBulb)
   - Set Temperature (for Thermostat)
   - Return to Main Menu
5. Follow the prompts to enter values (e.g., brightness level, color name, temperature).
6. Enter '0' at any time to return to the previous menu or exit the program.

Example:
--------
- Select "1" for Light
- Choose "1" to turn it on
- Choose "3" to set brightness to 75
- Choose "0" to return to the main menu

Note:
-----
This program is intended to be run in a local Python environment with access to standard input/output.
It does not support GUI or web-based interaction.

Author: Stephen Krohn
Date: 09/19/2025
"""
