import psutil # type: ignore
import time

def monitor_cpu(interval=1):
    try:
        while True:
            # Get the CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=interval)
            # Get the number of logical CPUs in the system
            cpu_count = psutil.cpu_count(logical=True)
            
            print(f"CPU Usage: {cpu_usage}% across {cpu_count} CPUs")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    # Monitor CPU usage every 1 second
    monitor_cpu(interval=1)
