from parseYaml import read_yaml_file
from parsePing import ping_server
import json
import time

def display_metrics(server_name, metrics):
    print(f"Ping results for {server_name}:")
    print(f"  Packet Transmitted: {metrics['packet_transmit']}")
    print(f"  Packet Received: {metrics['packet_receive']}")
    print(f"  Packet Loss: {metrics['packet_loss_rate']}%")
    print(f"  Round Trip Time (min/avg/max/stddev): {metrics['rtt_min']}/{metrics['rtt_avg']}/{metrics['rtt_max']}/{metrics['rtt_mdev']}")
    print("",flush=True)

config = read_yaml_file('config.yaml')
# print(config.get('servers'))
print(config)
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