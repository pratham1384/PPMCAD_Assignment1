import psutil
import time

threshold = 80  # Set your desired CPU usage threshold in %
int_time = 5    # Check every 5 second

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