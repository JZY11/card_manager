import socket


def main():
    # 1.买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind("", 7890)
    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)
    # 4.等待别人的电话到来(等待客户端的连接 accept)
    tcp_server_socket.accept()

if __name__ == "__mian__":
    main()