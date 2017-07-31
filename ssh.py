import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.16.22.169', username='phpor', password='lijunjie')

transport = client.get_transport()
transport.set_keepalive(30)
transport.use_compression(True)

channel = transport.open_session()
channel.set_environment_variable("SSH_TEST", "123")
channel.invoke_shell()

channel.close()
client.close()

