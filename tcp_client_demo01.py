import socket


def main():
    """tcp的客户端"""

    # 1.创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入要链接的服务器的ip：")
    server_port = input("请输入要链接的服务器的port：")

    server_address = (server_ip, server_port)
    tcp_socket.connect(server_address)

    #3.发送/接收数据
    send_data = input("请输入要发送说的信息：")
    tcp_socket.send(send_data.encode("utf-8"))

    #4.关闭套接字
    tcp_socket.close()

if __name__ == "__main__":
    main()