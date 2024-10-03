

from abc import  ABC,abstractmethod
class ExpenseSplit(ABC):


    @abstractmethod
    def validate_expense(self,split_list,total_amount):
        pass