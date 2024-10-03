from Controller.BalanceSheetController import BalanceSheetController
from Models.Expense import Expense
from SplitFactory.SplitFactory import SplitFactory


class ExpenseController:


    def __init__(self):
        self.balance_sheet_controller=BalanceSheetController()

    def create_expense(self,expense_id,description,expense_amount,paid_by_user,split_type,split_details):
        expense_split=SplitFactory().get_split_object(split_type)
        expense_split.validate_expense(split_details,expense_amount)
        expense=Expense(expense_id,description,expense_amount,paid_by_user,split_type)
        self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by_user,split_details,expense_amount)
        return  expense

