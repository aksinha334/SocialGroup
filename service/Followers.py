from SocialGroup.entity.SocialGroupClass import SocialGroup
from SocialGroup.Dao.DaoLayer import DAO
class Follower:
    def follower(username,following):
        object = SocialGroup()
        object.UserName = username
        DAO.following(object,following)
        del object