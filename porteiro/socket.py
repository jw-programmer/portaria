import socket


class Portaria:
    def __init__(ip, porta):
        self.ip_porta = ip
        self.porta = porta
        self.sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def enviarSinal(self):
        canal = (self.ip_porta, self.porta)
        self.sock_tcp.connect(canal)
        self.sock_tcp.send("Acesso Liberado, Abra o portão")
        self.sock_tcp.close()