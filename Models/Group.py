


class Group:

    def __init__(self):
        self.group_id=0
        self.group_name=0
        self.group_members=[]

    def get_group_id(self):
        return self.group_id

    def set_group_id(self,group_id):
        self.group_id=group_id

    def set_group_name(self,group_name):
        self.group_name=group_name

    def add_group_members(self,member):
        self.group_members.append(member)
    def get_group_name(self):
        return self.group_name

    def get_group_members(self):
        return self.group_members

    def add_members(self,member):
        self.group_members.append(member)
