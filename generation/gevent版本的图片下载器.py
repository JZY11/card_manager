import urllib.request


def main():
    req = urllib.request.urlopen("https://rpic.douyucdn.cn/live-cover/roomCover/2018/12/21/a77342abaa632c7760684a6a99f1f387_big.png")
    image_content = req.read()
    with open("1.jpg", "wb") as f:
        f.write(image_content)


if __name__ == "__main__":
    main()


