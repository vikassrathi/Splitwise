



class UserExpenseBalanceSheet:

    def __init__(self):
        self.user_vs_balance={}
        self.total_your_expense=0
        self.total_payment=0
        self.total_amount_owe=0
        self.total_amount_get_back=0

    def get_total_amount_get_back(self):
        return  self.total_amount_get_back

    def set_total_amount_get_back(self,total_amount_get_back):
        self.total_amount_get_back=total_amount_get_back

    def set_total_amount_owe(self,total_amount_owe):
        self.total_amount_owe=total_amount_owe

    def get_total_amount_owe(self):
        return self.total_amount_owe

    def set_total_payment(self,total_payment):
        self.total_payment=total_payment
    def get_total_payment(self):
        return self.total_payment

    def set_total_your_expense(self,total_expense):
        self.total_your_expense=total_expense
    def get_total_your_expense(self):
        return  self.total_your_expense

    def get_user_vs_balance(self):
        return self.user_vs_balance
