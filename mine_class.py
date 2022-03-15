class Mines:

    def __init__(self, material_mined, num_material_produced, set):
        self.material_mined = material_mined
        self.num_material_produced = num_material_produced
        self.set = False

    def set_mine(self, raw_material_dict, material_mined):
        """
        :param raw_material_dict: the imported dict containg the raw materials and recipes
        :param material_mined: the material that is going to be mined
        :return: nothing
        """
        # if a mine isnt set yet then set it to a material and change set to true
        if self.set == False:
            self.material_mined = material_mined
            self.num_material_produced = raw_material_dict["raw materials"][self.material_mined]
            self.set = True
        else:
            print("mine in use")

    def display(self):
        #if a mine is set print what its minging and how much it mines
        if self.set == True:
            print("\t\t {} mine producing {} per turn".format(self.material_mined, self.num_material_produced))

        else:
            print("\t\tmine Currently Inactive")
