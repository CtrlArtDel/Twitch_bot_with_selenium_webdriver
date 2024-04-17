# Twitch Automated Test

This repository contains automated test scripts for Twitch, designed to navigate the site, handle a cookies modal, search for "StarCraft II", scroll through results, select a streamer, and take a screenshot using Selenium in Python.

## Repository Structure

### `src` Directory
Contains the core Python scripts:
- `driver_setup.py`: Sets up the Selenium WebDriver for Chrome, configured to use a mobile emulator. It dynamically selects the driver based on the operating system (Linux or Windows).
- `selenium_tools.py`: Provides reusable utility functions for common Selenium operations, such as clicking elements, entering text, and taking screenshots.
- `twitch_test.py`: The main test class that implements the Twitch navigation and interaction test scenario.
- `main.py`: The entry point for the test, initializing and running the test from the `TwitchTest` class.

### Outside the `src` Directory
- `drivers/`: Contains the WebDriver executables for Linux and Windows. Ensure you have the correct version of ChromeDriver that matches your Chrome browser version.
- `screenshots/`: Screenshots taken during tests are saved here.

## Running the Test

Before running the test, ensure Python and Selenium are installed on your machine, and you have the correct ChromeDriver in the `drivers` folder.

Navigate to the `src` directory and run:
```bash
python main.py 
```

## GIF Demonstration
Below is a GIF that shows the script in action, demonstrating how it operates on the Twitch platform:

This GIF helps visualize the script's functionality from starting the browser, navigating Twitch, to taking a screenshot.

## Setup Instructions
Clone the Repository: Clone this repository to your local machine.
Install Dependencies: Run pip install selenium to install Selenium if it is not already installed.
Driver Setup: Place the appropriate chromedriver for your operating system in the drivers folder.
Run the Script: Follow the instructions in the "Running the Test" section.


## Troubleshooting
If you encounter issues related to chromedriver, ensure that:

The version of chromedriver matches the version of your Google Chrome browser. Version 123.0.6312.122
The chromedriver path is correctly set in driver_setup.py.
For other issues, check the Python and Selenium installation on your system or review the script logs for errors.
