import paramiko.client as pssh

def _get_ssh_client(server_address, server_user, server_port):
    client = pssh.SSHClient()
    client.load_system_host_keys()
    client.connect(server_address, server_port, server_user)
    return client

def backup(
        server_address, 
        server_user, 
        tank, 
        snapshot, 
        ask_user=True, 
        dry_run=False, 
        server_port=22):
    # check if server is available
    sshclient = _get_ssh_client()

