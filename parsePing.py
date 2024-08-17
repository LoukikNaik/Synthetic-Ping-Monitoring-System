import pingparsing
import json
def get_user_input():
    """Prompt the user to enter a server address to ping."""
    server = input("Enter the server address to ping (e.g., google.com or 8.8.8.8): ")
    return server

def ping_server(server, probes):
    """Ping the server and return the ping result."""
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = server
    transmitter.count = probes  # Number of ping requests

    result = transmitter.ping()
    return ping_parser.parse(result).as_dict()

if __name__ == "__main__":
    server = get_user_input()
    ping_result = ping_server(server, 10)
    print(json.dumps(ping_result, indent=4))

