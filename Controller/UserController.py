


class UserController:

    def __init__(self):
        self.user_list=[]

    def add_user(self,user):
        self.user_list.append(user)

    def get_user(self,user_id):
        for users in self.user_list:

            if users.get_user_id()==user_id:
                return users
        return None
    def get_all_user(self):
        return self.user_list