from Controller.BalanceSheetController import BalanceSheetController
from Controller.GroupController import GroupController
from Controller.UserController import UserController
from ExpenseSplitType.ExpenseSplitType import ExpenseSplitType
from Models.Split import Split
from Models.User import User




class Splitwise:
    def __init__(self):
        self.user_controller=UserController()
        self.group_controller=GroupController()
        self.balance_sheet_controller=BalanceSheetController()

    def add_user_to_splitwise(self):
        user1 = User('U001', 'user1')
        user2 = User('U002', 'user2')
        user3 = User('U003', 'user3')
        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)

    def setup_user_and_group(self):
        self.add_user_to_splitwise()
        user1 = self.user_controller.get_user('U001')
        self.group_controller.create_group('G001', 'Outing_with_friend_for_lunch', user1)



    def Check(self):
        self.setup_user_and_group()

        #adding members
        group=self.group_controller.get_group('G001')
        print(group)
        group.add_members(self.user_controller.get_user('U002'))
        group.add_members(self.user_controller.get_user('U003'))
        splits=[]
        split1=Split(self.user_controller.get_user('U001'),400)
        split2=Split(self.user_controller.get_user('U002'),400)
        split3=Split(self.user_controller.get_user('U003'),400)
        splits.append(split1)
        splits.append(split2)
        splits.append(split3)
        group.create_expense('Ex001','Lunch',1600,self.user_controller.get_user('U001'),ExpenseSplitType.EQUAL,splits)




