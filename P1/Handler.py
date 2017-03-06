# -*- coding:utf-8 -*-

import Queue
from User import *


class Handler:
    Crawled_USERS_FILE_NAME = "data/crawled_users.txt"
    ALL_USERS_FILE_NAME = "data/all_users.txt"
    RELATIONSHIP_FILE_NAME = "data/r.txt"
    USER_INFO_FILE_NAME = "data/user_info.txt"


    """
    3 Files: Crawled users, all users, relationship.
    crawled_users.txt: (user_id_name)
    all_users.txt: (user_id_name)
    r.txt: (v_user_id_name, u_user_id_name)
    """

    def __init__(self):
        self.crawled_users = set() # element is  string
        self.all_users = set()  # element is User
        self.q = Queue.Queue()  # node wait to deal with


    def __del__(self):
        pass

    def read(self):
        self.read_crawled_users()   # read have crawled user
        self.read_all_users()       # read all user and add not crawled user to queue.

        print "No. of crawled_users = %d, No. of all_users = %d, Qsize = %d" % (len(self.crawled_users),
                                                                                len(self.all_users),
                                                                                self.q.qsize())

    def read_crawled_users(self):
        """
        read have crawled user
        :return: None
        """
        print "-- read_crawled_users --"
        self.crawled_users.clear()
        f = open(self.Crawled_USERS_FILE_NAME)
        for line in f.readlines():
            id_name = line.strip()
            self.crawled_users.add(id_name)
        f.close()
        return

    def read_all_users(self):
        """
        read all user and add not crawled user to queue.
        :return:
        """
        print "-- read_all_users  --"
        self.all_users.clear()
        f = open(self.ALL_USERS_FILE_NAME)
        for line in f.readlines():
            # tmp = line.strip().split(' ')
            # id_name, num_follower, num_following = tmp[0], int(tmp[1]), int(tmp[2])
            id_name  = line.strip()
            self.all_users.add(id_name)
            # we should judge
            # user = UserInfo(id_name, num_follower, num_following)
            # self.all_users[id_name] = user

            if (id_name not in self.crawled_users):
                self.q.put(id_name)
        return

    def write_crawled_user(self, user):
        """
        appaned an user information to file tail
        :param user:
        :return:
        """
        f = open(self.Crawled_USERS_FILE_NAME, "a")
        f.write(user.id_name+"\n")
        f.close()

    def write_new_user(self, user_info):
        """
        write a new user infomation to all_users.txt file
        :param user_info:
        :return:
        """
        f = open(self.ALL_USERS_FILE_NAME, "a")
        f.write(user_info.get_all_para_str()+"\n")
        f.close()

    def add_uncrawl_id_name(self, id_name):
        """
        put a new uncrawl user to queue
        :param user_info:
        :return:
        """
        self.all_users.add(id_name)
        self.q.put(id_name)


    def is_visited(self, id_name):
        return id_name in self.all_users

    def is_in_crawled_user(self, id_name):
        return id_name in self.crawled_users

    def check_add_new_user(self, user_info):
        """
        For a new user, we check if we haven't crawled him,
        if have crawled, return false else return true
        :param user_info:
        :return:
        """
        if (not self.ishas_crawled_user() and not self.ishas_user()):
            self.add_uncrawl_user(user_info)
            return True
        return False

    def is_empty_uncrawled_user(self):
        """
        check whether have uncrawled user
        :return:  True(empty), False(have element)
        """
        return self.q.empty()

    # def get_user(self, id_name):
    #     """
    #     :param id_name: user_id_name
    #     :return:  UserInfo()
    #     """
    #     return self.all_users[id_name]


    def __str__(self):
        print "Hanld's condition: No. of all_users = %d" \
              "No. of crawled_users = %d, " \
              "No. of wait_users = %d" % (len(self.all_users),
                                          len(self.crawled_users),
                                          self.q.qsize)

    def save_id_name_list(self, id_name_list):
        """

        :param id_name_list:
        :return: [new_id_name_list...]
        """
        ret = []
        for id_name in id_name_list:
            if self.is_in_crawled_user(id_name):  # 1. 是已经爬取过的
                # pass
                pass
            elif self.is_visited(id_name):  # 2. 是待爬取的
                # pass
                pass
            else:  # 3. 是一个新节点
                self.add_uncrawl_id_name(id_name)
                ret.append(id_name)
        return ret

    def append2file_new_id_name_list(self, id_name_list):
        f = open(self.ALL_USERS_FILE_NAME, "a")
        for id_name in id_name_list:
            f.write(id_name+"\n")
        f.close()

    def add_crawled_id_name(self, id_name):
        self.crawled_users.add(id_name)

    def append2file_crawled_id_name(self, id_name):
        f = open(self.Crawled_USERS_FILE_NAME, "a")
        f.write(id_name+"\n")
        f.close()

    def append2file_relationships(self, flag, id_name, id_name_list):
        f = open(self.RELATIONSHIP_FILE_NAME, "a")
        str_mod = ""
        if flag == "follower":
            str_mod = id_name+" %s\n"
        elif flag == "following":
            str_mod = "%s "+id_name+"\n"
        else:
            print "!!!!!!!!!!!!!!!!!!!!!"

        for _id_name in id_name_list:
            f.write(str_mod % _id_name)
        f.close()
    def append2file_user_info(self, id_name, num_follower, num_following):
        f = open(self.USER_INFO_FILE_NAME, "a")
        f.write("%s %d %d\n" % (id_name, num_follower, num_following))
        f.close()

    def write_crawled_user(self):
        pass

    def write_all_user(self):
        pass

