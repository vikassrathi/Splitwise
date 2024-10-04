from UserExpenseBalanceSheet import UserExpenseBalanceSheet


class User:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
        self.splitBalanceSheet=UserExpenseBalanceSheet()


    def get_user_id(self):
        return self.user_id
    def get_user_name(self):
        return self.user_name


    def set_user_id(self,user_id):
        self.user_id=user_id

    def set_user_name(self,user_name):
        self.user_name=user_name
    def get_user_expense_balance_sheet(self):
        return self.splitBalanceSheet