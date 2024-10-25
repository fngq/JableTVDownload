import server 
from jable import Jmanager,Jtask
import logging

def main():
    url = r"https://jable.tv/videos/ssni-647/"
    m = Jmanager(logging.getLogger(),"./")
    m.CreateTask(url,0)

if __name__ == "__main__":
    main()