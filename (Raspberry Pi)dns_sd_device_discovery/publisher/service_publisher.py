import socket
import time
from zeroconf import Zeroconf,ServiceInfo

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

zeroconf = Zeroconf()

device_name = "RaspberryPi-01"
service_type = "_customdevice._tcp.local."
service_name = device_name + "." + service_type
port = 5000

ip_address = socket.inet_aton(get_ip_address())

service_info = ServiceInfo(
    type_=service_type,
    name=service_name,
    addresses=[ip_address],
    port=port,
    properties={
        "device": device_name,
        "role": "publisher"
    },
    server=device_name + ".local."
)


zeroconf.register_service(service_info)

print("Service announced on network")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    zeroconf.unregister_service(service_info)
    zeroconf.close()
