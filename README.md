# Custom Device Discovery via DNS-SD

## Overview
This project implements automatic device discovery on a local network using
mDNS and DNS Service Discovery (DNS-SD). A Raspberry Pi (physical or virtual)
acts as a service publisher, announcing itself on the network, while a client
device discovers the service and displays the device details.

The implementation uses Python and the `python-zeroconf` library.

---

## Architecture
- **Publisher**: Raspberry Pi / Virtual Raspberry Pi OS  
- **Client**: Laptop (Windows/Linux/macOS)  
- **Network**: Same Local Area Network (LAN)

---

## Technologies Used
- Python 3
- python-zeroconf
- Raspberry Pi OS / Virtual Raspberry Pi
- mDNS / DNS-SD

---

## Project Structure
```

Custom-Device-Discovery-DNS-SD/
│
├── publisher/
│   └── service_publisher.py      # Service announcer (Raspberry Pi)
│
├── client/
│   └── service_discovery.py      # Service discovery client
│
├── screenshots/
│   ├── publisher_output.png      # Publisher execution proof
│   └── client_output.png         # Client discovery output proof
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

````

---

## How It Works
1. The Raspberry Pi publishes a service using DNS-SD over mDNS.
2. The service includes metadata such as device name, IP address, and port.
3. The client listens on the local network for available services.
4. When the service is discovered, the client prints the device details.

---

## Setup and Execution

### Prerequisites
- Python 3 installed on both devices
- Both devices connected to the same LAN
- Virtual Raspberry Pi must use **bridged networking**

---

### Publisher Setup (Raspberry Pi / VM)

Install dependency:
```bash
pip3 install zeroconf
````

Run the publisher:

```bash
python3 publisher/service_publisher.py
```

Expected output:

```
Service announced on network
```

---

### Client Setup (Laptop)

Install dependency:

```bash
python -m pip install zeroconf
```

Run the client:

```bash
python client/service_discovery.py
```

Expected output:

```
Discovered Device
Service Name: RaspberryPi-01._customdevice._tcp.local.
IP Address: xxx.xxx.xxx.xxx
Port: 5000
Metadata: {...}
```

---

## Verification

* Publisher terminal confirms service announcement.
* Client terminal displays discovered device details.
* Screenshots are provided in the `screenshots/` directory as proof.

---

## Notes

* mDNS works only within the same local network.
* No manual IP configuration is required.
* The client runs for a fixed duration to demonstrate discovery.

---

## Conclusion

This project successfully demonstrates DNS-SD based service discovery using
Python. The Raspberry Pi advertises its presence on the network, and the client
automatically discovers and displays the device information without manual
intervention.

---

## Author

**Arijeet Dey**

