# Server configuration dictionary
server_config = {
    "server1": {"ip": "198.168.1.1", "port": 8080, "status": "active"},
    "server2": {"ip": "198.168.1.2", "port": 8080, "satus": "inactive"},
    "server3": {"ip": "198.168.1.3", "port": 8080, "status": "active"}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get("status", "Server not found")

# Example usage
server_name = "server2"
status = get_server_status(server_name)
print(f"{server_name} status: {status}")