from parseYaml import read_yaml_file
from parsePing import ping_server
import json
import time
from prometheus_client import start_http_server, Gauge

server = 'localhost:8000'
ping_latency_min = Gauge('ping_latency_min', 'Minimum Round Trip Time', ['server'])
ping_latency_avg = Gauge('ping_latency_avg', 'Average Round Trip Time', ['server'])
ping_latency_max = Gauge('ping_latency_max', 'Maximum Round Trip Time', ['server'])
ping_packet_loss = Gauge('ping_packet_loss', 'Packet Loss', ['server'])
ping_packets_transmitted = Gauge('ping_packets_transmitted', 'Packets Transmitted', ['server'])
ping_packets_received = Gauge('ping_packets_received', 'Packets Received', ['server'])

def display_metrics(server_name, metrics):
    print(f"Ping results for {server_name}:")
    print(f"  Packet Transmitted: {metrics['packet_transmit']}")
    print(f"  Packet Received: {metrics['packet_receive']}")
    print(f"  Packet Loss: {metrics['packet_loss_rate']}%")
    print(f"  Round Trip Time (min/avg/max/stddev): {metrics['rtt_min']}/{metrics['rtt_avg']}/{metrics['rtt_max']}/{metrics['rtt_mdev']}")
    print("",flush=True)

    ping_latency_min.labels(server=server_name).set(metrics['rtt_min'])
    ping_latency_avg.labels(server=server_name).set(metrics['rtt_avg'])
    ping_latency_max.labels(server=server_name).set(metrics['rtt_max'])
    ping_packet_loss.labels(server=server_name).set(metrics['packet_loss_rate'])
    ping_packets_transmitted.labels(server=server_name).set(metrics['packet_transmit'])
    ping_packets_received.labels(server=server_name).set(metrics['packet_receive'])

config_name = input("Please Input Config File Path: ")

config = read_yaml_file(config_name)
# print(config.get('servers'))
print(config)

start_http_server(8000)
servers = config.get('servers', [])
interval = config.get('interval', 0)
l=0
while True:

    for server in servers:
        server_name = server.get('address')
        # ip = server.get('ip')
        # interval = server.get('interval', 10)
        probes = server.get('probes', 4)
        
        metrics = ping_server(server_name, probes)
        # print(json.dumps(metrics, indent=4))
        display_metrics(server_name, metrics)
        
    time.sleep(interval)