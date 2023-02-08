import plotext as plt
import subprocess
import time
import sys

duration = int(sys.argv[1]) # seconds
graphing_interval = 5 # seconds
temp_vs_time = []
freq_vs_time = []

if bool(int(sys.argv[2])):
        print("Beginning stress test in 5 seconds...")
        time.sleep(5)
        stress_process=subprocess.Popen("stress -c 4 -t " + str(duration)+ " > /dev/null",shell=True)
freq_file = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq","r")
temperature_file = open("/sys/class/thermal/thermal_zone0/temp","r")

for i in range(duration):       # Poll every second
        freq_file.seek(0)
        temperature_file.seek(0)
        cpu_freq = float(freq_file.readline().rstrip())/1000 # MHz
        cpu_temp = float(temperature_file.readline().rstrip())/1000 # Celcius
        temp_vs_time.append(cpu_temp)
        freq_vs_time.append(cpu_freq)
        if (i%graphing_interval ==0):
                #subprocess.Popen("clear",shell=True)
                plt.clf()
                plt.scatter(temp_vs_time, xside = "lower", yside = "left", label = "Temperature")
                plt.scatter(freq_vs_time, xside = "lower", yside = "right", label = "CPU Frequency")
                plt.ylim(20,100,yside = "left")
                plt.ylim(0,2500,yside = "right")
                plt.xlim(0,duration)
                plt.xlabel("Time (s)")
                plt.ylabel("Temperature (°C)", yside = "left")
                plt.ylabel("CPU Frequency (MHz)", yside = "right")
                plt.title("Rpy-monitor")
                plt.show()
        time.sleep(1)
#print(temp_vs_time)
#print(freq_vs_time)
freq_file.close()
temperature_file.close()
