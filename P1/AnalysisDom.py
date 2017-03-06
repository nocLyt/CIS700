from bs4 import BeautifulSoup
from User import *


class AnalysisDom:
    """
    AnalysisDom is used to analysis html information

    """
    def __init__(self, html):
        self.bs = BeautifulSoup(html, "lxml")

    def test(self):
        print ("Title")
        print ad.bs.title

    def get_num_follow_info(self):
        """
        get the the number of follower and following from user profile website html DOM
        :return: NO. of [follower, followering]
        """

        tmp = self.bs.find("div", class_="secondary").find_all("a")
        print tmp
        print tmp[0]
        print tmp[0].find("span")
        print tmp[0].find("span").text

        follower = self.string2num(tmp[0].find("span").text)
        following = self.string2num(tmp[1].find("span").text)
        return [follower, following]

    def string2num(self, ss):
        return int(''.join(ss.strip().split(',')))

    def get_list_follower(self):
        # 2. get user
        pass

    def get_list_following(self):
        # 2. get user
        pass

    def get_list_id_name(self):
        """
        :return: [id_name, id_name, ...]
        """
        tmp = self.bs.find("div", class_="layout_3col_center").find_all("a", class_="user")
        users = []
        for ht in tmp:
            # name = ht.text

            id_name = (ht['href'].split('/')[-1])
            id_name = id_name.encode('utf-8')
            users.append(id_name)
        return users



if __name__ == '__main__':
    # bs = BeautifulSoup(open('ex.html'), "lxml")
    ad = AnalysisDom(open('ex.html'))

    print ad.string2num('2,3,4')

