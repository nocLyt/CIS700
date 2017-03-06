# -*- coding:utf-8 -*-


from Browser import Browser
from selenium import webdriver
from Handler import *
from AnalysisDom import *
import time


def login_success(br):
    return True;


def login(br):
    LOGIN_URL = "https://www.quora.com"
    br.get(LOGIN_URL)
    time.sleep(30)
    return


def follow_number_strategy():
    return None

# def mouse_strategy(repeat_cnt=20):
#     l_new = len(br.page_source)
#     l_old = 0;
#     while (l_old != l_new) and (repeat_cnt>0):
#         time.sleep(1)
#         br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         l_old = l_new
#         l_new = len(br.page_source)
#         repeat_cnt -= 1

def mouse_strategy(num):
    if (num>400):
        num = 400
    #
    timeout_cnt = 0
    MAX_TIME_OUT_CNT = 200
    #
    accumulator = 0
    MAX_ACCUMULATOR = 15
    last_l = -1

    while True:
        timeout_cnt += 1
        if timeout_cnt >= MAX_TIME_OUT_CNT:
            print "TIME OUT!"
            break
        time.sleep(0.5)     # every 500ms
        br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ad = AnalysisDom(br.page_source)
        ls = ad.get_list_id_name()
        l = len(ls)
        print ("--- %d %d\n" % (len(ls), num))
        if (last_l == l):
            accumulator += 1
        else:
            accumulator = 0
        if accumulator >= MAX_ACCUMULATOR:
            print "TIME OUT!"
            break
        last_l = l
        if (len(ls) >= num-3):   ## ! I don't know why --- 106 107
            break;



def crawl_infomation(title, url, id_name, num):
    print ("We get %s ing..." % title)
    # Do follower
    br.get(url)
    # 1. 根据 follow 数量，开始开始模拟鼠标
    nomeans = follow_number_strategy()
    # 2. 模拟鼠标策略
    mouse_strategy(num)
    # 3. 分析 html
    html = br.page_source
    ad = AnalysisDom(html)
    # 4. 将 html 中的数据提取
    id_name_list = ad.get_list_id_name()
    print "id_name_list: ", id_name_list
    # 5. 把图信息写入
    hd.append2file_relationships(title, id_name, id_name_list)
    # 6. Handle 将提取的 id_names 判断是否已经访问过，并加入 Handle 中的已经爬过的节点集合和所有用户集合。
    un_crawled_id_name = hd.save_id_name_list(id_name_list)
    print "un_crawled_id_name: ", un_crawled_id_name
    # 6. 保存新的没有爬过的节点到文件
    hd.append2file_new_id_name_list(un_crawled_id_name)


def crawl():
    print "-- Begin Crawl --"
    print "Queue size : ", hd.q.qsize()
    print "Is empty : ", hd.q.empty()
    while(not hd.is_empty_uncrawled_user()):
        id_name = hd.q.get()
        user = User(id_name)
        print "Out Queue  ", user
        # 1. 打开 URL
        url_profile = user.url_profile()
        br.get(url_profile)
        time.sleep(1.5);
        html = br.page_source
        ad = AnalysisDom(html)
        num_follower, num_following = ad.get_num_follow_info()
        print "Get num_follower = %d , num_following = %d\n" % (num_follower, num_following)
        hd.append2file_user_info(id_name, num_follower, num_following)

        # 3. 开始爬 follower
        crawl_infomation("follower", user.url_follower(), id_name, num_follower)
        # 4. 开始爬 following
        crawl_infomation("following", user.url_following(), id_name, num_following)

        # 5. 将这个 id_name 标记为 已经爬过了，并保存到文件
        hd.add_crawled_id_name(id_name)
        hd.append2file_crawled_id_name(id_name)
        # 6. over!
    print "Over"
    return


hd = Handler()
br = webdriver.Chrome()

if __name__ == "__main__":


    # 1. LOGIN
    login(br);

    # 2. 读取文件，找到已经处理完的，和没有处理完的

    hd.read()
    # 3. 将没有处理完的入队
    # Done it from 2.

    # 4. 开始进行循环操作
    crawl()
