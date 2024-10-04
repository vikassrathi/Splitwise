from Models.Group import Group


class GroupController:

    def __init__(self):
        self.group_list={}
    def create_group(self,group_id,description,created_by_user):
        group= Group()
        group.set_group_id(group_id)
        group.set_group_name(description)
        group.add_members(created_by_user)
        group.group_members.append(group)
        self.group_list[group_id]=group

    def get_group(self,group_id):

        for group,group_object in self.group_list.items():
            if group==group_id:
                return group_object
        return None