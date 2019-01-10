import socket


def main():
    """文件下载"""

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
    
    # 接收对方发送回来的数据，最大1024个字节(1k)
    recv_data = tcp_client_socket.recv(1024)
    # print('接收到的数据为：', recv_data.decode('utf-8'))

    # 如果真的接收到了数据再创建文件，否则不创建
    if recv_data:
        with open("[接收]" + file_name,"wb") as f:
            f.write(recv_data)
        # with 这种形式不用写 close()
    # 关闭套接字
    tcp_client_socket.close()

if __name__ == "main":
    main()