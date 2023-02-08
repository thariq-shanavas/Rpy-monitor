# Rpy-monitor
A lightweight hardware monitor for headless Raspberry pi. 

## Features
A python script to render a real-time graph of temperture and CPU frequency vs time for a Raspberry Pi. 
* Lightweight and minimal dependencies.
* Does not need x11 forwarding as the graph is rendered directly to the terminal.

## Installation

Step 1: [SSH into the Raspberry Pi.](https://itsfoss.com/ssh-into-raspberry/)

Step 2:

    python3 -m pip install plotext
    mkdir ~/Rpy-monitor
    cd Rpy-monitor
    wget github link - FIX ME

## Usage
The script takes two arguments: Duration to monitor and whether to run a stress test. Duration to run (in seconds) is passed as an integer and the option to run a stress test in parallel is passed as either 0 or 1.

For example, the following command runs a CPU stress test for 5 minutes (300 seconds)

    cd ~/Rpy-monitor
    python3 Rpy-monitor.py 300 1
To simply run the monitor for 60 seconds without stressing the CPU

    python3 Rpy-monitor.py 60 0
  
Tested on Raspberry Pi 4b running Raspbian Lite.

## Example graphs
1. Stress testing Raspberry Pi 4 with heatsink case, overclocked to 2 GHz

    ![Stress test](/examples/stress_test.png)
    
2. What happens if you stick an ice-pack on a Pi?

    ![Ice pack test](/examples/rpy-monitor-ice.png)

## Dependencies
* Python 3 (duh)
* Python [plotext module](https://github.com/piccolomo/plotext)
* Python [Subprocess module](https://docs.python.org/3/library/subprocess.html), likely came with your Python installation.
