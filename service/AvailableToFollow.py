from SocialGroup.Dao.DaoLayer import DAO
from SocialGroup.entity.SocialGroupClass import SocialGroup
class Available:
    def AvailableToFollow(userName):
        object = SocialGroup()
        object.UserName = userName
        value = DAO.availableUsersToFollow(object)
        del object
        return value
