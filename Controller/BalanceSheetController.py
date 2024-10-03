from Models.Balance import Balance


class BalanceSheetController:

    def update_user_expense_balance_sheet(self,expense_paid_by,splits,total_amount):
        paid_by_user_expense_balance_sheet=expense_paid_by.get_user_expense_balace_sheet()
        paid_by_user_expense_balance_sheet.set_total_payment(paid_by_user_expense_balance_sheet.get_total_payment()+total_amount)


        for split in splits:
            user_owe=split.get_user_id()
            user_owe_expense_balance_sheet=user_owe.get_user_expense_balance_sheet()
            owe_amount=user_owe.get_amount_owe()

            if expense_paid_by.get_user_id()==user_owe.get_user_id():
                paid_by_user_expense_balance_sheet.set_total_your_expense(paid_by_user_expense_balance_sheet.get_total_your_expense()+owe_amount)
            else:
                paid_by_user_expense_balance_sheet.set_total_amount_get_back(paid_by_user_expense_balance_sheet.get_total_amount_get_back()+owe_amount)
            if user_owe.get_user_id() in paid_by_user_expense_balance_sheet.get_user_vs_balance():
                user_owe_balance=paid_by_user_expense_balance_sheet.get_user_vs_balance()[user_owe.get_user_id()]
            else:
                user_owe_balance=Balance()
                paid_by_user_expense_balance_sheet.get_user_vs_balance()[user_owe.get_user_id()]=user_owe_balance
            user_owe_balance.set_amount_get_back(user_owe_balance.get_amount_get_back()+owe_amount)

            user_owe_expense_balance_sheet.set_total_amount_owe(user_owe_expense_balance_sheet.get_total_amount_owe()+owe_amount)
            user_owe_expense_balance_sheet.set_total_your_expense(user_owe_expense_balance_sheet.get_total_your_expense()+owe_amount)

            if expense_paid_by.get_user_id() in user_owe_expense_balance_sheet.get_user_vs_balance():
                user_paid_balance=user_owe_expense_balance_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()]
            else:
                user_paid_balance=Balance()
                user_owe_expense_balance_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()]=user_paid_balance

            user_paid_balance.set_amount_owe(user_paid_balance.get_amount_owe()+owe_amount)


    def show_balance_of_user(self,user):
        print('Get Balance Sheet of user',user.get_user_id())
        user_expense_balance_sheet=user.get_user_expense_balace_sheet()
        print('Total Expense',user_expense_balance_sheet.get_total_your_expense())
