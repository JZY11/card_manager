import socket
import re
import select


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接受浏览器发送过来的请求即http发送过来的请求
    # GET / HTTP/1.1
    #......

    # request = new_socket.recv(1024).decode("utf-8") # 服务器对接收到的客户端发送过来的请求进行解码
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
        # response += "Content.length:%d\r\n" % len()
        response += "\r\n"
        response += "----- file not found --- "
        new_socket.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()

        response_body = html_content
        response_header = "HTTP/1.1 200 0K\r\n"
        response_header += "Content-length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body  #  将头部信息response_header.encode("utf-8") 变为二进制

        # 2. 返回http格式的数据给浏览器
        new_socket.send(response)  # 发送头部信息和body信息


    # 关闭套接字
    # new_socket.close()  # 就是因为服务器先close，所以就变成了短连接   等下次浏览器再次请求资源时还得要进行三次握手


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

    # 设置套接字为非堵塞的方式
    tcp_server_socket.setblocking(False)

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)  # 第二个参数目的是为了：收到数据的时候通知你也就是检测第一参数(监听套接字)是否有输入，若有输入则表明：有客户端开始连接该服务器啦

    fd_event_dict = dict()
    while True:

        fd_event_list = epl.poll()  # 默认是堵塞的，直到os检测到有数据到来通过事件通知方式告诉这个程序，此时才会解堵塞

        # fd_event_list: [(fd, event),(套接字对应的文件描述符, 这个文件描述符到底是什么事件(到底是收还是发) 例如：可以调用recv()接受等)]
        for fd, event in fd_event_list: # 拆包
            # 4. 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_address = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:   # 如果recv_data 是空的  则表明浏览器客户端已经关闭即4次挥手开始
                    fd_event_dict[fd].close()
                    epl.unregister(fd)  # 从epoll对象中撤销该套接字对应的fd
                    del fd_event_dict[fd] # 如果recv_data为空则浏览器已经关闭，我们需要将字典对象中该fd对应着的套接字对象删除

        # 5. 为这个客户端服务
        # service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()













