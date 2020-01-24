# Implement a class to hold room information. This should have name and
# description attributes.


class __Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.does_block = False


class Wall(__Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.does_block = True


class Room(__Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.n_to = Wall('wall', 'There is a wall here')
        self.s_to = Wall('wall', 'There is a wall here')
        self.w_to = Wall('wall', 'There is a wall here')
        self.e_to = Wall('wall', 'There is a wall here')
