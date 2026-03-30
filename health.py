#first time writing a script zero clue wtf im doing :-)
import psutil

print("=" * 30)
print("   SYSTEM HEALTH REPORT")
print("=" * 30)

cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

ram = psutil.virtual_memory()
print(f"RAM Usage: {ram.percent}%")
print(f"RAM Used: {ram.used // 1024 // 1024} MB / {ram.total // 1024 // 1024} MB")

disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
print(f"Disk Used: {disk.used // 1024 // 1024 //1024} GB / {disk.total // 1024 // 1024 //1024} GB")

print("=" * 30)


