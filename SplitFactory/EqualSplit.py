

from ExpenseSplitType import ExpenseSplit
class EqualSplit(ExpenseSplit):

    def validate_expense(self,split_list,total_amount):

        each_person_amount=total_amount//len(split_list)

        