# Rpy-monitor
A lightweight hardware monitor for linux, with a headless Raspberry pi in mind.

## Features
A python script to render a real-time graph of temperture and CPU frequency vs time. 
* Lightweight and minimal dependencies.
* Does not need x11 forwarding as the graph is rendered directly to the terminal.

## Installation

Step 1: [SSH into the Raspberry Pi](https://itsfoss.com/ssh-into-raspberry/) (or any headless linux server)

Step 2:

    python3 -m pip install plotext
    sudo apt install stress
    mkdir ~/Rpy-monitor
    cd Rpy-monitor
    wget raw.githubusercontent.com/thariq-shanavas/Rpy-monitor/main/Rpy-monitor.py

## Usage
The script takes two arguments: Duration to monitor and whether to run a stress test. Duration (in seconds) is passed as an integer and the option to run a stress test in parallel is passed as either 0 or 1. If no arguments are supplied, the script runs for 5 minutes and skips the stress test. If only one argument is provided, it is interpreted as the duration to monitor and the stress test is skipped.

For example, the following command runs a CPU stress test for 5 minutes (300 seconds). The graph is refreshed every 5 seconds by default.

    cd ~/Rpy-monitor
    python3 Rpy-monitor.py 300 1
To simply run the monitor for 60 seconds without stressing the CPU

    python3 Rpy-monitor.py 60 0
  
Tested on Raspberry Pi 4b running Raspbian Lite and my laptop running Arch Linux. 

## Example graphs
1. Stress testing Raspberry Pi 4 with heatsink case, overclocked to 2 GHz

    ![Stress test](/examples/stress-test.png)
    
2. What happens if you stick an ice-pack on a Pi?

    ![Ice pack test](/examples/rpy-monitor-ice.png)

## Dependencies
* Python 3
* Python [plotext module](https://github.com/piccolomo/plotext)
* Python [Subprocess module](https://docs.python.org/3/library/subprocess.html), likely came with your Python installation.
* Stress tool (https://linux.die.net/man/1/stress)
