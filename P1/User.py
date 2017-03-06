URL_USER_PROFILE_PREFIX = "https://www.quora.com/profile/"
URL_USER_FOLLOWER_TMPL = "https://www.quora.com/profile/%s/followers"
URL_USER_FOLLOWING_TMPL = "https://www.quora.com/profile/%s/following"


class User:
    def __init__(self, id_name):
        self.id_name= id_name
        pass

    def __del__(self):
        pass

    # def __str__(self):
    #     return "User name = %s, id_name = %s" % (self.name, self.id_name)

    def __str__(self):
        return "User id_name = %s" % (self.id_name)

    def url_profile(self):
        return '/'.join([URL_USER_PROFILE_PREFIX, self.id_name])

    def url_follower(self):
        return (URL_USER_FOLLOWER_TMPL % self.id_name)

    def url_following(self):
        return (URL_USER_FOLLOWING_TMPL % self.id_name)


class UserInfo(User):
    def __init__(self, id_name, num_follower=-1, num_following=-1):
        User.__init__(self, id_name)
        self.num_follower = num_follower;
        self.num_following = num_following

    def __del__(self):
        pass

    def __str__(self):
        return ("User id_name = %s, No. of follower = %d, No. of following = %d."
                % (self.id_name, self.num_follower, self.num_following))
    def get_all_para_str(self):
        return ("%s %d %d" % (self.id_name, self.num_follower, self.num_following))


if __name__ == "__main__":
    pass