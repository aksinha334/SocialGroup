from SocialGroup.entity.SocialGroupClass import SocialGroup
from SocialGroup.Dao.DaoLayer import DAO
class SignIn:
    def signIn(UserName, Password):
        object = SocialGroup()
        object.UserName = UserName
        object.Password = Password
        if(DAO.isUserExists(object)):
            return True
        else:
            return False

