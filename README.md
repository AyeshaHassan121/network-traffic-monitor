# Network Traffic Monitor

A web-based network traffic monitoring and analysis platform built with Python and Flask.

## Project Description
This project simulates a network traffic monitoring system that reads packet data from a dataset and displays it through a clean web interface. It allows users to monitor, filter, and analyze network traffic data including TCP, UDP, and ICMP protocols.

## Files
- `app.py` : Flask backend that loads and serves packet data
- `dataset.csv` : Network traffic dataset with 100 simulated packets
- `templates/index.html` : Frontend web interface

## Technologies Used
- Python 3
- Flask (web framework)
- HTML, CSS, JavaScript (frontend)
- CSV module (dataset handling)

## How to Run
1. Install Flask: `pip install flask`
2. Open Command Prompt in the project folder
3. Run: `python app.py`
4. Open browser and go to: `http://127.0.0.1:5000`

## Features
- Start and Stop monitoring
- Displays Source IP, Destination IP, Protocol, Ports, Service, Size
- Port to service mapping (HTTP, HTTPS, DNS, SSH, FTP etc.)
- Filter by Protocol (TCP / UDP / ICMP)
- Filter by Source IP
- Filter by Destination IP
- Reset filter
- Basic statistics: Total packets, TCP count, UDP count, ICMP count, Average packet size

## Dataset Fields
- Time
- Source IP
- Destination IP
- Protocol (TCP / UDP / ICMP)
- Source Port
- Destination Port
- Service
- Packet Size (bytes)
