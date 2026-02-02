import time
from zeroconf import Zeroconf, ServiceBrowser

class ServiceListener:
    def add_service(self, zeroconf, service_type, name):
        info = zeroconf.get_service_info(service_type, name)
        if info:
            ip_address = ".".join(map(str, info.addresses[0]))
            print("\nDiscovered Device")
            print("Service Name:", name)
            print("IP Address:", ip_address)
            print("Port:", info.port)
            print("Metadata:", info.properties)

    def update_service(self, zeroconf, service_type, name):
        pass

zeroconf = Zeroconf()
listener = ServiceListener()

ServiceBrowser(
    zeroconf,
    "_customdevice._tcp.local.",
    listener
)

try:
    while True:
        time.sleep(1)   # <-- MUST be indented
except KeyboardInterrupt:
    pass
finally:
    zeroconf.close()
