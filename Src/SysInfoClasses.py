import platform
import psutil
import GPUtil
from datetime import datetime


def get_size(bytes, suffix="B"):
# Scale bytes to its proper format
# e.g:
#     1253656 => '1.20MB'
#     1253656678 => '1.17GB'
    _factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < _factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= _factor


class ThisSysSys:
    def __init__(self):
        _uname = platform.uname()
        _boot_time_timestamp = psutil.boot_time()
        _bt = datetime.fromtimestamp(_boot_time_timestamp)
        self.system = f"{_uname.system}"
        self.node = f"{_uname.node}"
        self.release =f"{_uname.release}"
        self.version =f"{_uname.version}"
        self.machine =f"{_uname.machine}"
        self.processor =f"{_uname.processor}"
        self.boot_time =f"{_bt.year}/{_bt.month}/{_bt.day} {_bt.hour}:{_bt.minute}:{_bt.second}"


class ThisSysCPU:
    def __init__(self):
        # number of cores
        self.physical_cores = psutil.cpu_count(logical=False)
        self.total_cores = psutil.cpu_count(logical=True)
        # CPU frequencies
        _cpufreq = psutil.cpu_freq()
        self.max_frequency =f"{_cpufreq.max:.2f}Mhz"
        self.min_frequency =f"{_cpufreq.min:.2f}Mhz"
        self.current_frequency =f"{_cpufreq.current:.2f}Mhz"
        
class ThisSysMem:
    def __init__(self):
        # get the memory details
        _svmem = psutil.virtual_memory()
        self.total_memory = f"{get_size(_svmem.total)}"
        self.available_memory = f"{get_size(_svmem.available)}"
        self.used_memory = f"{get_size(_svmem.used)}"
        self.percentage = f"{_svmem.percent}%"
        # get the swap memory details (if exists)
        _swap = psutil.swap_memory()
        self.total_swap = f"{get_size(_swap.total)}"
        self.free_swap = f"{get_size(_swap.free)}"
        self.used_swap = f"{get_size(_swap.used)}"
        self.percentage_swap = f"{_swap.percent}%"
    def show_partitions_disks(cls):
        # Disk Information
        for partition in partitions:
            if partition.fstype != "squashfs":
                print(f"=== Device: {partition.device} ===")
                print(f"  Mountpoint: {partition.mountpoint}")
                print(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    # this can be catched due to the disk that
                    # isn't ready
                    continue
                print(f"  Total Size: {get_size(partition_usage.total)}")
                print(f"  Used: {get_size(partition_usage.used)}")
                print(f"  Free: {get_size(partition_usage.free)}")
                print(f"  Percentage: {partition_usage.percent}%")

class ThisSysNet:
    def __init__(self):
        self.total_bytes_sent = f"{get_size(net_io.bytes_sent)}"
        self.total_bytes_received = f"{get_size(net_io.bytes_recv)}"
    def net_info(cls):
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")

class ThisSysGPU:
    def __init__(self):
        _gpus = GPUtil.getGPUs()
        _list_gpus = []
        for gpu in _gpus:
        # get the GPU id
            gpu_id = gpu.id
        # name of GPU
            gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
            gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
            gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
            gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
            gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
            gpu_temperature = f"{gpu.temperature} °C"
            gpu_uuid = gpu.uuid
            _list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))
        self.gpus_list=_list_gpus

