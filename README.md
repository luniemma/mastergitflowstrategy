CPU Monitoring Script
This Python script monitors CPU usage on a system and displays the usage percentage every second. It utilizes the psutil library to fetch system-level information.

Features
Monitor the overall CPU usage percentage.
Get the number of logical CPUs on the system.
Displays the CPU usage in real-time, refreshing every second.
Easily configurable monitoring interval.
Prerequisites
Make sure you have Python installed on your system. You can check this by running:

bash
Copy code
python --version
Required Libraries
This script uses the psutil library. Install the required library by running:

bash
Copy code
pip install psutil
Usage
Clone the repository or download the script.
Install the required dependencies.
Run the script to start monitoring CPU usage.
Steps
bash
Copy code
# Clone the repository
git clone <repository_url>

# Navigate into the directory
cd cpu-monitor

# Install required library
pip install psutil

# Run the script
python monitor_cpu.py
Configuration
The monitoring interval can be adjusted by changing the interval parameter when calling the monitor_cpu() function. By default, the interval is set to 1 second:

python
Copy code
monitor_cpu(interval=1)
Stopping the Monitoring
To stop monitoring, simply press Ctrl + C in the terminal.

License
This project is licensed under the MIT License - see the LICENSE file for details.

# CPU Monitor Script

This Python script monitors the CPU usage of your machine and displays it in real-time. It prints the percentage of CPU utilization at specified intervals.

## Features
- Displays CPU usage as a percentage.
- Monitors the CPU usage for all logical CPUs.
- Configurable interval for monitoring.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Clone the repository or download the script.
   
   ```bash
   git clone <repository_url>
