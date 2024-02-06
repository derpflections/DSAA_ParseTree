# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07

"""
main.py

This is the main script for the Caesar Cipher Encrypted Message Analyzer application. It orchestrates
the user interaction through a command line interface, utilizing the MainMenu class for navigation and
providing various options for encryption, decryption, and analysis.

The script sets up the main menu, displays welcome messages, and handles the overall program flow,
including user input and navigation through different functionalities of the application.

Usage:
- Run this script in a command line interface to start the application.
- Follow the on-screen prompts to navigate through the various options.
"""


from application.menu import MainMenu

program_running = True

# Creates list of options. Can be expanded if further development is required.
options_list = [
    "Add/Modify assignment statement",
    "Display current assignment statements",
    "Evaluate a single variable",
    "Read assignment statements from file",
    "Sort assignment statements",
    "Extra Function 1",
    "Show Dependencies/Dependants",
    "Visualize Dependencies",
    "History of Assignment Statements",
    "Exit",
]


# Initiates MainMenu class using given options.
mainMenu = MainMenu(options=options_list)

# Display welcome screen/banner to user.
mainMenu.display_welcome_screen()
# Broken by return in .program_navigation.
while program_running:
    # Prints option menu
    selection = mainMenu.display_main_menu()
    # Runs selected option.
    mainMenu.program_navigation(selection, exit_int=len(options_list))
