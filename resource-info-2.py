import psutil
import platform
import pyfiglet
from termcolor2 import colored
from datetime import datetime
#Sec-1
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
#Sec-2

message="pouria"
ascii_art=pyfiglet.figlet_format(message)
ascii_art=colored(ascii_art,color="green")
print(ascii_art)
result = pyfiglet.figlet_format("resource info", font = "digital" )
print(result)
print("="*80)



def cpu():
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    input("Press Enter to continue...")

def memory():
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    input("Press Enter to continue...")

def disk():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    input("Press Enter to continue...")
def menu():
    print("please Enter your number:")
    print("[1] CPU info")
    print("[2] MEMORY info")
    print("[3] DISK info")
    print("[4] ACCOUNT NAME")
    result2 = colored("Choose a menu option, or press 0 to Exit:",color = "blue" )
    print(result2)


while True:
    menu()
    number=int(input())

    if number== 1 :
        cpu()
        print("="*80)
                
    elif number== 2:
        memory()
        print("="*80)
        
        
    elif number== 3:
        disk()
        print("="*80)
        
    elif number== 4:
        uname = platform.uname()
        print(f"User Account: {uname.node}")
        input("Press Enter to continue...")
        print("="*80)
        
    elif number>4 or number<0:
        result3 = colored("You enter a wrong number, Choose a another number, or press 0 to Exit:",color = "red" )
        print(result3)
        print("="*80)
        
    elif number== 0:
        exit()      
