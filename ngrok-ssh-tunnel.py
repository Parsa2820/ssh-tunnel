from sshtunnel import SSHTunnelForwarder

# command is like ssh root@4.tcp.ngrok.io -p 10297
ssh_command = input('enter ssh command: ').split()
password = input('enter password: ')

port = int(ssh_command[3])
user_and_address = ssh_command[1].split('@')
user = user_and_address[0]
address = user_and_address[1]

server = SSHTunnelForwarder(
    ssh_address_or_host=(address, port),
    ssh_username=user,
    ssh_password=password,
    remote_bind_address=(address, port)
)

server.start()

print(server.local_bind_port)
input('tunnel is up, press enter if you want to close it')

server.stop()
