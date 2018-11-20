from SocialGroup.entity.SocialGroupClass import SocialGroup
from SocialGroup.Dao.DaoLayer import DAO

class SignUp:

    def signUp(Name,UserName,Password):
        object = SocialGroup()
        object.Name = Name
        object.UserName = UserName
        object.Password = Password

        if(DAO.isUserNameExist(object)):
            if(DAO.insertIntoDB(object)==True):
                del object
                return True
        del object
        return False
