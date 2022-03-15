"""
File:    recipe_maker.py
Author:  Abdel Nasser
Date:    05/10/2021
Section: 23
E-mail:  abdelrn1@umbc.edu
Description: silicon crises game
"""
import json

dict = {"raw materials" : {},
        "recipes" : {}}

def save_file(file_name, dict):
    """
    :param file_name: file name
    :param dict: dict being saved
    :return: None
    """
    write_json_file = open(file_name, 'w')

    string_to_write = json.dumps(dict)
    write_json_file.write(string_to_write)

    write_json_file.close()

if __name__ == '__main__':


    # while  this is true
    continue_asking = True
    while continue_asking == True:
        name_output = input("name the output? ")

        # takes in the ingredient and how much it produce
        rate_produced = (input("What is the rate at which it is output? "))
        ingredient = input("name the ingredient")

        # adds the name name output into a specific data structure
        dict["recipes"][name_output] = {"output": name_output, "output_count": rate_produced, "parts": {}}

        if ingredient == "stop":
            name_output = input("name the output? ")

        while ingredient != "stop":
            if ingredient == "done":

                # asks for user input of ingredient
                name_output = input("name the output? ")

                # if user inputs done then it stops both while loops from running
                if name_output == "done":
                    continue_asking = False
                    ingredient = "stop"
            else:
                # else it asks for the ingredient needed and appends that as a value in the ingreident key
                ingredient_needed = input("How much of that ingredient is needed? ")
                dict["recipes"][name_output]["parts"][ingredient] = int(ingredient_needed)
                ingredient = input("name the ingredient")


    #saves the file into json format
    file_name = input("what is the file name ")
    save_file(file_name, dict)


