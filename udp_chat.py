import socket


def send_message(udp_socket):
    """发送消息"""
    # destaddr = ("192.168.0.4", 8080)
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))

    # 从键盘获取要发送的内容
    send_data = input("请输入要发送的消息：")

    # 发送
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def receive_message(udp_socket):
    # 接收并显示
    recive_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recive_data[1]), recive_data[0].decode("utf_8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind("",7788)

    # 循环来处理事情
    while True:
        send_message(udp_socket)



if __name__ == "__main__":
    main()