"""
File:    silicon_crisis.py
Author:  Abdel Nasser
Date:    05/10/2021
Section: 23
E-mail:  abdelrn1@umbc.edu
Description: silicon crisis game
"""

import json
from Factory_class import Factory
from mine_class import Mines

def display_recipes(dict):
    print(":::Recipes:::")

    # iterates through all the recipes and prints out what they are
    for key in dict["recipes"].keys():
        print("\t {} - produced in increments of {}".format(key,dict["recipes"][key]["output count"]))
        print("\t required materials:")

        # iterates through all mat and number of mat and prints them out
        for mat, num in dict["recipes"][key]["parts"].items():
            print("\t\t{}: {}".format(mat,num))

def display_stockpile(dict):
    print(":::Current Stockpile:::")

    # iterates through the stockpile dict and print out both key and value
    for mat, num in dict["materials"].items():
        print("\t{}: {}".format(mat, num))

def display_raw_materials(dict):
    print(":::Raw Materials:::")

    # iterates through the raw materials dict and print out the key and value
    for mat, num in dict["raw materials"].items():
        print("\t{}: {}".format(mat, num))


def load_file(file_name):
    read_file = open(file_name, 'r')
    # just a string with the json stuff read in.
    json_string = read_file.read()
    # just call read once, get everything out of the file.
    data = json.loads(json_string)
    dict = (data)
    return dict


def set_mines(mines_dict, mine_number, material_mined, raw_material_dict):
    """
    :param mines_dict: dict containging mines
    :param mine_number: the current mine we are setting
    :param material_mined:  the material being mined
    :param raw_material_dict: the recipe dict
    :return: nothing
    """
    #takes in the mine number form the mine class and calls it in the mine class
    temp = mines_dict[mine_number]
    temp.set_mine(raw_material_dict, material_mined)

def display_mines(mines_dict):
    # loop through mine dict
    temp = 0
    for mine in mines_dict.keys():
        # prints the mine number and calls the display method in mine class
        print("\tMine {}".format(str(temp)))
        temp += 1
        mines_dict[mine].display()

def display_factories(factory_dict):
    # loop through factory dict
    temp = 0
    for factory in factory_dict.keys():

        # prints the factory number and calls the display method in factory class
        print("\tfactory {}".format(str(temp)))
        temp += 1
        factory_dict[factory].display()

def set_factories(factory_dict, factory_number, material_to_produce, raw_material_dict):
    """
    :param factory_dict: factory dict
    :param factory_number: takes in the factory that its setting to a material
    :param material_to_produce: going to set a factory to build this material
    :param raw_material_dict: takes in the imported dict
    :return: nothing
    """
    #takes in the factory number form the factory class and calls it in the factory class
    temp = factory_dict[factory_number]
    temp.set_factory(material_to_produce, raw_material_dict)

def end_turn(mines_dict, factory_dict, stockpile, recipe_dict, factory_counter, mine_counter):
    """
    :param mine_dict: the mine dict
    :param factory_dict: the dict contaning all the factory
    :param stockpile: the stockpile dict
    :param recipe_dict: the dict containg all raw material and recipe
    :param factory_counter: takes in the number of factories
    :param mine_counter: takes in the number of mines
    :return: nothing
    """
    # loops trough all the mines
    for mine in mines_dict.keys():

        # if a a mine is mining a material that is not yet in stock and what its mining doesnt return None
        if mines_dict[mine].material_mined not in stockpile["materials"] and (mines_dict[mine].num_material_produced) != None:

            # add that material to the dict and set the number that it produces to the current ammount in the stockpile dict
            stockpile["materials"][mines_dict[mine].material_mined] = mines_dict[mine].num_material_produced

        # if a mine is mining a material that is in the stock pile and what its mining doesnt return None
        if mines_dict[mine].material_mined in stockpile["materials"] and (mines_dict[mine].num_material_produced) != None:

            # add that number it produces to the current stockpile of that item
            stockpile["materials"][mines_dict[mine].material_mined] +=  (mines_dict[mine].num_material_produced)

    # loop through all the the factories

    temp_factory = 0
    temp_mine = 0
    temp_recipe = 0

    for factory in factory_dict.keys():

        # loops through all the recipes
        for recipe in recipe_dict["recipes"].keys():

            # if factory is set to factory and the recipe is also set to factory
            if factory_dict[factory].producing == recipe:
                required_piece_counter = 0
                mat_removal_temp_list = []

                materials_needed = []
                for mat, num_mat in recipe_dict["recipes"][recipe]["parts"].items():
                    materials_needed.append(recipe_dict["recipes"][recipe]["parts"])

                    if mat in stockpile["materials"] and recipe_dict["recipes"][recipe]["parts"][mat] <= stockpile["materials"][mat]:

                        mat_removal_temp_list.append(mat)
                        required_piece_counter += 1

                        # if the required materials to build a factory is equal to the number of parts then
                        if required_piece_counter == len(recipe_dict["recipes"][recipe]["parts"]):

                            if recipe == "factory":
                                # adds the output of the factory to the count
                                temp_factory += int(recipe_dict["recipes"]["factory"]["output count"])

                            elif recipe == "mine":
                                # adds the output of the factory to the count
                                temp_mine += int(recipe_dict["recipes"]["mine"]["output count"])

                            else:
                                # varaible to store in the output count of the recipe we just made
                                temp_recipe += int(recipe_dict["recipes"][recipe]["output count"])

                                # if the material made is not in the stockpile dict then add it
                                if recipe not in stockpile["materials"]:
                                    stockpile["materials"][recipe] = temp_recipe

                                # if it is in there then add to the count of it
                                else:
                                    stockpile["materials"][recipe] += temp_recipe


                            # ensures it subtracts from the stockpile after it has build the factory

                            for i in range(len(mat_removal_temp_list)):
                                stockpile["materials"][mat_removal_temp_list[i]] = stockpile["materials"][mat_removal_temp_list[i]] - int(recipe_dict["recipes"][recipe]["parts"][mat_removal_temp_list[i]])

                            # adds the output to the total production in that factory
                            (factory_dict[factory].total_production) = (factory_dict[factory].total_production) + int(recipe_dict["recipes"][recipe]["output count"])

                    else:
                        # ensures it resets all the mat in the list`
                        mat_removal_temp_list = []

    # creates factories based on how much the recipe outputs
    for i in range(int(temp_factory)):
        # creates a new factory and increments the factory counter by 1
        factory_dict[str(factory_counter)] = Factory(None)
        factory_counter += 1

    # creates mines based on how much the recipe outputs
    for i in range(int(temp_mine)):

        # creates a new mine and increments the mine counter by 1
        mines_dict[str(mine_counter)] = Mines(None, None, False)
        mine_counter += 1


def recursive_func(raw_material, recipe, dict):
    """
    :param raw_material: the material we are looking for
    :param recipe: the recipe we are going to be searching in
    :param dict: the dict containg all the raw materials and recipe
    :return: how many x are in y
    """

    count_of_raw_material = 0

    # if the recipe every becomes a raw material return the count of raw material
    if recipe in dict["raw materials"]:
        return count_of_raw_material


    else:
        value_to_multiply = 1
        # iterates through the recipes dict
        for mat, num_mat in dict["recipes"][recipe]["parts"].items():

            # if we found what we are looking for add it to the count
            if mat == raw_material:
                count_of_raw_material += num_mat

            # if we find another recipe then set that recipe value to this the value to multiply variable
            if mat in dict["recipes"]:
                value_to_multiply = num_mat

                # returns the value to multiply times  whatever raw material is in the recipe that we will look into
                count_of_raw_material = count_of_raw_material + (value_to_multiply * (recursive_func(raw_material, mat , dict)))

        return count_of_raw_material

if __name__ == '__main__':
    # asks and loads the json file
    json_file = input("Enter SC Recipe File Name ")
    dict = load_file(json_file)

    stockpile = {"materials": {}}

    # dictionary containing what what we start out with
    mines_dict = {"0": Mines(None, None, False), "1": Mines(None, None, False)}
    factory_dict = {"0": Factory(None), "1": Factory(None)}

    end_turn_counter = 1


    next_action = input("Select Next Action>> ")
    EXIT_STRING = "quit"
    while next_action != EXIT_STRING:
        # constants
        last_word = 6
        third_word = 2
        fourth_word = 3

        # takes in the command
        list_of_action = next_action.split()
        first_word = list_of_action[0]
        second_word = list_of_action[1]

        if list_of_action[0] == "set" and list_of_action[1] == "mine":
            set_mines(mines_dict, list_of_action[third_word], list_of_action[fourth_word], dict)

        elif list_of_action[0] == "set" and list_of_action[1] == "factory":
            set_factories(factory_dict, list_of_action[third_word], list_of_action[fourth_word], dict)

        elif next_action.lower() == "display stockpile":
            display_stockpile(stockpile)

        elif next_action.lower() == "display recipes":
            display_recipes(dict)

        elif next_action.lower() == "display factories":
            display_factories(factory_dict)

        elif next_action.lower() == "display raw materials":
            display_raw_materials(dict)

        elif next_action.lower() == "display mines":
            display_mines(mines_dict)

        elif next_action.lower() == "end turn":
            end_turn_counter += 1
            end_turn(mines_dict, factory_dict, stockpile, dict, len(factory_dict), len(mines_dict))
            print("Mining ...")
            print("Making ...")
            print("turn {} complete".format(end_turn_counter))

        elif first_word.lower() == "how" and second_word.lower() == "many":

            material_word = list_of_action[third_word]
            search_word = list_of_action[last_word]

            # ensures we don't search a raw material
            if search_word in dict["raw materials"]:
                print("cant search that ")

            # recursive function
            else:
                print("There are {} {} in a {}".format(recursive_func(material_word, search_word, dict), material_word, search_word))

        else:
            print("Invalid Entery")

        next_action = input("Select Next Action>> ")




