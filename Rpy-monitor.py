import plotext as plt
import subprocess
import time
import sys


graphing_interval = 5 # seconds
temp_vs_time = []
freq_vs_time = []

if len(sys.argv) == 3:
        perform_stress_test = bool(int(sys.argv[2]))
        duration = int(sys.argv[1]) # seconds
        
if len(sys.argv) == 2:
        perform_stress_test = False
        duration = int(sys.argv[1]) # seconds

if len(sys.argv) == 1:
        perform_stress_test = False
        duration = 300 # seconds



if perform_stress_test:
        print("Beginning stress test in 5 seconds...")
        time.sleep(5)
        num_threads = str(subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l",shell=True))[2]     # Slightly convoluted to avoid more dependencies
        stress_process=subprocess.Popen("stress -c "+num_threads+" -t " + str(duration)+ " > /dev/null",shell=True)
freq_file = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq","r")
temperature_file = open("/sys/class/thermal/thermal_zone0/temp","r")

max_CPU_freq_file = open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq","r")
max_cpu_freq = float(max_CPU_freq_file.readline().rstrip())/1000 # MHz
max_CPU_freq_file.close()

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
                plt.ylim(0,max_cpu_freq+500,yside = "right")
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
