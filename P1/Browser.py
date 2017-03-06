from selenium import webdriver


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Browser:

    def __init__(self):
        self.br = webdriver.Chrome()


    def get(self, url):
        self.br.get(url)


    def __del__(self):
        pass
