import psutil
import time

threshold = 80  #Setting up the CPU threshold to 80%.
int_time = 5   #Setting interval to 5 secs.

print("Monitoring CPU usage...")

try:
    while True:
        usage = psutil.cpu_percent(interval=int_time)
        if usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {usage}%")
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:

    print(f"An error occurred: {e}")
