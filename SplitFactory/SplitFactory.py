from SplitFactory import EqualSplit


class SplitFactory:

    def get_split_object(self,splitType):
        if splitType=='EQUAL':
            return EqualSplit()
