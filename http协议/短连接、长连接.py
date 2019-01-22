# 短连接：三次握手成功后回数据后断开连接  当浏览器发现需要一些个图片的时候就会再次与服务器进行三次握手建立连接等等
# 长连接：先把请求1发过去，服务器就会给浏览器回数据，浏览器进行解析，解析的过程中浏览器发现需要一个图片，接下来浏览器再发送请求2(次请求没有用新的套接字，用的是原来的)


import socket
import re


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1. 接受浏览器发送过来的请求即http发送过来的请求
    # GET / HTTP/1.1
    #......

    request = new_socket.recv(1024).decode("utf-8") # 服务器对接收到的客户端发送过来的请求进行解码
    # print(request)
    request_lines = request.splitlines()
    print(">" * 20)
    print(request_lines)

    ret = re.match(r"[^/]+/[^ ]*", request_lines[0])   # r是为了原生字符串不用转义
    if ret:
        file_name = ret.group(1)

    # 2.2 准备好发送给浏览器的数据 ---  body
    try:
        f = open("./html/index.html", "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----- file not found --- "
        new_socket.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()
        # 2. 返回http格式的数据给浏览器
        # 2.1 准备好发送给浏览器的数据 ---  header
        response = "HTTP/1.1 200 0K\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))  # 发送头部信息
        new_socket.send(html_content)  # 发送body信息


    # 关闭套接字
    new_socket.close()  # 就是因为服务器先close，所以就变成了短连接   等下次浏览器再次请求资源时还得要进行三次握手


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













