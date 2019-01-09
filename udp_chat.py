import socket

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind("",7788)
    # 循环来处理事情
    while True:
        # 从键盘获取要发送的内容
        send_data = input("请输入要发送的数据：")
        destaddr = ("192.168.0.4", 8080)

        # 发送
        udp_socket.sendto(send_data.encode("utf-8"),destaddr)
        # 接收并显示

if __name__ == "__main__":
    main()