from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


DEBUG = 1

USERS_FILE = "users.txt"


def run1(br, name):
    URL = "https://www.quora.com/profile/"+name+"/followers "
    br.get(URL)
    print br.page_source

URL_LOGIN = "https://www.quora.com"


def save_cookie(br):
    print br.get_cookies()


def test_long():
    br = webdriver.Chrome()
    br.get(URL_LOGIN)
    time.sleep(10)

    run1(br, "Lukman-Leong")
    save_cookie(br)
    time.sleep(3600*5);
    br.close();



# Gather user data and save into csv file
def crawlUser():
    if (DEBUG): print "In crawlUser..."

    unique_users = set(open(USERS_FILE).readlines())

    open('temp.txt', 'w').writelines(set(unique_users))

    file_users = open("temp.txt", mode='r')

    # file_users_csv = open("users.csv", mode='w')
    total = 0
    cur_line = file_users.readline()
    while(cur_line):
        print "--"
        browser = webdriver.Chrome()
        browser.get(cur_line)

        # print browser.page_source
        src_updated = browser.page_source
        src = ""
        while src != src_updated:
            print "----"
            src = src_updated
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            src_updated = browser.page_source
            print "11"
        print browser.page_source
        print browser.title
        break
    browser.close()

    """
    current_line = file_users.readline()
    while (current_line):

        # Open browser to current_question_url
        chromedriver = "chromedriver"  # Needed?
        os.environ["webdriver.chrome.driver"] = chromedriver  # Needed?
        browser = webdriver.Chrome()
        browser.get(current_line)

        # Fetch page
        src_updated = browser.page_source
        src = ""
        while src != src_updated:
            time.sleep(.5)
            src = src_updated
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Find user id
        user_id = browser.current_url
        html_source = browser.page_source
        browser.quit()

        source_soup = BeautifulSoup(html_source)
        part = source_soup.find_all(attrs={"class": "link_label"})
        part_soup = BeautifulSoup(str(part))
        raw_info = part_soup.text.split(",")
        if (DEBUG): print raw_info

        for x in range(1, len(raw_info)):
            # if (DEBUG): print raw_info[x]
            key = raw_info[x].split(" ")[1]
            value = raw_info[x].split(" ")[2]
            if key == "Topics":
                num_topics = value
                if (DEBUG): print "num_topics:", num_topics
            elif key == "Blogs":
                num_blogs = value
                if (DEBUG): print "num_blogs:", num_blogs
            elif key == "Questions":
                num_questions = value
                if (DEBUG): print "num_questions:", num_questions
            elif key == "Answers":
                num_answers = value
                if (DEBUG): print "num_answers:", num_answers
            elif key == "Edits":
                value = value.split("]")[0]
                num_edits = value
                if (DEBUG): print "num_edit:", num_edits

        # Find followers
        followers_url = user_id.split('?')[0] + "/followers?share=1"
        browser = webdriver.Chrome()
        browser.get(followers_url)

        src_updated = browser.page_source
        src = ""
        while src != src_updated:
            time.sleep(.5)
            src = src_updated
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            src_updated = browser.page_source
        followers_html_source = browser.page_source
        browser.quit()

        followers_soup = BeautifulSoup(followers_html_source)
        followers_raw = followers_soup.find_all(attrs={"class": "user"})
        if (DEBUG): print "num of followers:", len(followers_raw)

        followers = ""
        count = 0
        for x in range(1, len(followers_raw)):
            followers_soup = BeautifulSoup(str(followers_raw[x]))
            for follower in followers_soup.find_all('a', href=True):
                count += 1
                if (followers):
                    followers += ", " + "http://www.quora.com" + follower['href'] + "?share=1"
                else:
                    followers += "http://www.quora.com" + follower['href'] + "?share=1"

        if (DEBUG): print "Followers count:", count
        followers = "{{{" + followers + "}}}"

        # Find following
        following_url = user_id.split('?')[0] + "/following?share=1"
        browser = webdriver.Chrome()
        browser.get(following_url)

        src_updated = browser.page_source
        src = ""
        while src != src_updated:
            time.sleep(.5)
            src = src_updated
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            src_updated = browser.page_source
        following_html_source = browser.page_source
        browser.quit()

        following_soup = BeautifulSoup(following_html_source)
        following_raw = following_soup.find_all(attrs={"class": "user"})
        if (DEBUG): print "num of following:", len(following_raw)

        following = ""
        count = 0
        for x in range(1, len(following_raw)):
            following_soup = BeautifulSoup(str(following_raw[x]))
            for each_following in following_soup.find_all('a', href=True):
                count += 1
                if (following):
                    following += ", " + "http://www.quora.com" + each_following['href'] + "?share=1"
                else:
                    following += "http://www.quora.com" + each_following['href'] + "?share=1"

        if (DEBUG): print "Following count:", count
        following = "{{{" + following + "}}}"

        s = user_id + ", " + str(num_topics) + ", " + str(num_blogs) + ", " + str(num_questions) + ", " + str(
            num_answers) + ", " + str(num_edits) + ", " + followers + ", " + following
        if (DEBUG): print s
        file_users_csv.write((s + '\n').encode('utf8'))
        current_line = file_users.readline()
        total += 1

    file_users.close()
    file_users_csv.close()
    print "Total users:{0}".format(str(total))
    return 0
    """


def main():
    # crawlUser()
    test_long()

if __name__ == "__main__":
    main()