import socket


def service_client():
    """为这个客户端返回数据"""


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    # 4. 等待新客户端的链接
    new_socket, client_address = tcp_server_socket.accept()

    # 5. 为这个客户端服务
    service_client()


if __name__ == "__main__":
    main()

