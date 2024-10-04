from ExpenseSplitType.ExpenseSplitType import ExpenseSplitType
from SplitFactory.EqualSplit import EqualSplit


class SplitFactory:

    def get_split_object(self,splitType):
        if splitType==ExpenseSplitType.EQUAL:
            return EqualSplit()
