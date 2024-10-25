import download

def test_download():
    url = r"https://jable.tv/videos/abw-087/"
    m = download.Jmanager(download.jlogger,"./")
    m.CreateTask(url,0)


if __name__ == "__main__":
    test_download()