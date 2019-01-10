import socket


def main():
    # 创建socket套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 目的信息
    server_ip = input("请输入服务器ip：")
    server_port = input("请输入服务器port：")

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    # 输入需要下载的文件名
    file_name = input("请输入您要下载的文件名：")

    # 发送文件下载请求
    tcp_client_socket.send(file_name.encode("utf-8"))
if __name__ == "main":
    main()