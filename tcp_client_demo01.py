import socket


def main():
    # 1.创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入要链接的服务器的ip：")
    server_port = input("请输入要链接的服务器的port：")

    server_address = (server_ip, server_port);
    tcp_socket.connect(server_address)
    #3.发送/接收数据

    #4.关闭套接字


if __name__ == "__main__":
    main()