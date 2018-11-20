from SocialGroup.Dao import MongoDB

class SocialGroup:
    def __init__(self):
        self.Name = None
        self.UserName = None
        self.Password = None
        self.Followers = []
        self.Following = []

