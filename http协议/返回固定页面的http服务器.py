import socket


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1. 接受浏览器发送过来的请求即http发送过来的请求
    # GET / HTTP/1.1
    #......

    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据给浏览器
    # 2.1 准备好发送给浏览器的数据 ---  header
    response = "HTTP/1.1 200 0K\r\n"
    response += "\r\n"

    # 2.2 准备好发送给浏览器的数据 ---  body
    f = open("./html/index.html", "rb")
    html_content = f.read()
    f.close()

    new_socket.send(response.encode("utf-8")) # 发送头部信息
    new_socket.send(html_content)   # 发送body信息


    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close，即服务器4词挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即执行
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_address = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

