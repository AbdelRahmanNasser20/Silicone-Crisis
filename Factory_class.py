class Factory:

    def __init__(self, producing):
        self.producing = producing
        self.production = 0
        self.total_production = 0
        self.set = False

    def set_factory(self, material, raw_material_dict):
        """
        :param material: takes in the recipe it will set the factory to build
        :param raw_material_dict: the imported dict
        :return: nothing
        """
        # if a factory is set to false then set that factory to build the material and set the production to how ever much the recipe produces
        # sets factory to true after it is  set to a recipe
        if self.set == False:
            self.producing = material
            self.production = raw_material_dict["recipes"][material]["output count"]
            self.set = True

        else:
            print("factory in use")

    def display(self):

        if self.set == True:
            print("\t\t{} Factory producing {} per turn, total production {} Factory".format(self.producing, self.production, self.total_production))

        else:
            print("\t\tFactory Currently Inactive")
