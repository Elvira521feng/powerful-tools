import paramiko


class SshOperation(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ssh = None
        self.transport = None

    def ssh_connect_pwd(self, username, password):
        """
        用用户密码连接远程服务器
        参数：
            host:服务器ip
            port:服务器端口
            username:用户名
            password:密码
        返回：
            ssh:连接实例
        """
        transport = paramiko.Transport(self.host, self.port)
        transport.connect(username=username, password=password)

        self.ssh = paramiko.SSHClient()
        self.transport = transport

    def ssh_connect_secret_key(self, username, secret_key_file):
        """
        用用户密钥连接远程服务器
        参数：
            host:服务器ip
            port:服务器端口
            username:用户名
            secret_key_file:密钥文件
        返回：
            ssh:连接实例
        """
        private_key = paramiko.RSAKey.from_private_key_file(secret_key_file)

        transport = paramiko.Transport(self.host, self.port)
        transport.connect(username=username, pkey=private_key)

        self.ssh = paramiko.SSHClient()
        self.transport = transport

    def exec_command(self, command):
        """
        执行命令
        参数：
            command:需要执行的命令
        返回：
            stdin：
            stdout：
            stderr：
        """
        stdin, stdout, stderr = self.ssh.exec_command(command)

        return stdin, stdout, stderr

    def download_file(self, remove_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        # 将location.py 上传至服务器 /tmp/test.py
        # 将remove_path 下载到本地 local_path
        sftp.get(remove_path, local_path)

    def close(self):
        """
        关闭连接
        :返回:
        """
        self.transport.close()

