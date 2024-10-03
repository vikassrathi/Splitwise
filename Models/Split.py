



class Split:

    def __init__(self,user_id,amount_owe):
        self.user_id=user_id
        self.amount_owe=amount_owe

    def get_amount_owe(self):
        return self.amount_owe

    def set_amount_owe(self,amount_owe):
        self.amount_owe=amount_owe