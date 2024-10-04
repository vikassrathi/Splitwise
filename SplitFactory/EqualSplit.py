from logging import exception

from ExpenseSplitType.ExpenseSplit import ExpenseSplit


class EqualSplit(ExpenseSplit):

    def validate_expense(self, split_list, total_amount):

        each_person_amount = total_amount // len(split_list)

        for split in split_list:
            if split.get_amount_owe() != each_person_amount:
                raise exception('Invalid Split')
