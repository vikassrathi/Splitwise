from Models.Group import Group


class GroupController:

    def __init__(self):
        self.group_list=[]

    def create_group(self,group_id,description,created_by_user):
        group= Group()
        group.set_group_id(group_id)
        group.set_group_name(description)
        group.add_members(created_by_user)
        group.group_members.append(group)

    def get_group(self,group_id):

        for group in self.group_list:
            if group==group_id:
                return group
        return None