 Simple Network Sniffer (CodeAlpha Task)

 Overview
This is my first cybersecurity mini-project for CodeAlpha.
This project was created as part of my CodeAlpha Cybersecurity Internship (Task).    
I used Python and the Scapy library to build a simple packet sniffer.  
It captures live network traffic and displays source IP, destination IP, protocol, and payload size.

The program captures live network traffic and displays details such as:  
- Source IP address  
- Destination IP address  
- Protocol type (TCP/UDP/ICMP)  
- Payload length  


 Features
- Real-time packet capture
- Displays source and destination IP addresses
- Detects TCP and UDP protocols
- Shows payload length
- Runs continuously until stopped with Ctrl+C


 Requirements
To run this project, i used:  
- Python 3.x installed  
- Scapy library  

Install the dependencies by running: pip install -r requirements.txt

 How to Run
1. Download/clone this repository to your computer.  
2. Open Command Prompt as Administrator (required for sniffing).  
3. Navigate to the project folder:cd Desktop\CodeAlpha_NetworkSniffer
4. Run the script:python network_sniffer.py
5. While the sniffer is running, generate some network traffic:  
   - Open a website (e.g., google.com), OR  
   - Run `ping google.com` in another Command Prompt.  

 Demo Screenshot
Here is a screenshot of my sniffer in action:it has been saved into the project folder.

  Example Output
Here’s a sample of what the program prints when packets are captured:
============================================================
Source IP : 192.168.43.21
Destination IP : 8.8.8.8
Protocol Num : 1
Protocol : ICMP
Payload Length : 32



 Notes
- This project was developed as part of my CodeAlpha Internship (Task).  
- I tested it by using `ping google.com` to generate network traffic.  
- You must run it in Administrator mode on Windows.  



 Author:David Oluwaseun Onaopemipo
 Student ID: CA/SE3/2001
 Internship: CodeAlpha Cybersecurity Program


