from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        print("="*60)
        print(f"Source IP      : {src}")
        print(f"Destination IP : {dst}")
        print(f"Protocol Num   : {proto}")

        if TCP in packet:
            print("Protocol       : TCP")
            print(f"Payload Length : {len(packet[TCP].payload)}")
        elif UDP in packet:
            print("Protocol       : UDP")
            print(f"Payload Length : {len(packet[UDP].payload)}")

print("🚀 Enhanced Sniffer running — press Ctrl+C to stop")
sniff(prn=packet_callback, store=0)  # keep capturing until stopped
