import socket


def send_file_2_client(new_client_socket):
    # 1.接收客户端发送过来的 需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")  # 接受1024个字节  返回不是元组，是一个普通数据  decode()是为了解码

    # 2.打开这个文件然后读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    if file_content:
        # 3.将数据发送给客户端
        new_client_socket.send(file_content)


def main():
    # 1.买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 监听套接字：等待有新的客户端进行连接

    # 2.插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind("", 7890)

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:
        # 4.等待别人的电话到来(等待客户端的连接 accept) accept返回的是一个元组
        new_client_socket, clientAddr = tcp_server_socket.accept()  # 左边第一个是accept产生的套接字用来为客户端服务，第二个是某客户端连接过来的信息，也是一个元组(客户端ip，客户端port)

        # 5.调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket,)

        # 6.关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()