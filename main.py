from trees_module import *
from growing_trees import *
from graph_module import *
from drawing_graphs import *


def welcome():
    print("              ===================")
    print("             =====================")
    print("      _____ //                   \\\\")
    print("    ||____ //                     \\\\")
    print("    ||    //                       \\\\")
    print("    ||   //                         \\\\")
    print("    ||  //                           \\\\")
    print("    || //                             \\\\")
    print("    ||//                               \\\\")
    print("     //                                 \\\\")
    print("    //                                   \\\\")
    print("   //                                     \\\\")
    print("  //                                       \\\\")
    print(" //                                         \\\\")
    print("//                                           \\\\")
    print("===============================================")
    print("   **                                     **")
    print("   **                                     **")
    print("   **                                     **")
    print("   **                                     **")
    print("   **                                     **")
    print("   **  Welcome to Yinnie's Body Shop 😊   **")
    print("   **                                     **")
    print("   **                                     **")
    print("   **             ___________             **")
    print("   **            ||    ❤️   ||            **")
    print("   **            ||    ❤️   ||            **")
    print("   **            ||    ❤️   ||            **")
    print("   **            ||    ❤️   ||            **")
    print("   =========================================")
    print("   =========================================")
    print("")
    print("")

welcome()
customer_name = input("What is your name? ")

def personalized_greeting():
    print(f"How may we be of service to you today, {customer_name}?")
    print("")
    print("")

def get_response():
    greet_response = input(f"""Will you like to access our Clothing section, {customer_name}? 
                            Enter - Y - for Yes or - N - for No: """)
    print("")
    print("")
    if greet_response.lower() == 'n':
        print(f"Thank you for visiting Yinnie's Body Shop, {customer_name}!")
        print("We hope to see you soon. 😊")
    elif greet_response == 'y':
        get_category()
        thank_you()
    else:
        print("Choose one between Y for Yes and N for No")
        print("")
        get_response()


#Get the user response, match with the major clothing categories, and print the closest matching major categories available.
def get_category():
    available_clothing_categories = ['Bags', 'Dresses', 'Footwear', 'Accessories', 'Tops', 'Skirts', 'Jeans_trousers']
    response_1 = input(f"What type of clothing item will you like to get today?: ")
    print("")
    result_dict = {}
    matching_categories = []
    for string1 in available_clothing_categories:
        grid = [[0 for char in range(0, len(response_1)+1)] for char in range(0, len(string1)+1)]
        for row in range(1, len(string1)+1):
            for col in range(1, len(response_1)+1):
                if string1.lower()[row-1] == response_1.lower()[col-1]:
                    grid[row][col] = grid[row - 1][col - 1] + 1
                else:
                    grid[row][col] = max(grid[row-1][col], grid[row][col-1])
        longest_subsequence = grid[-1][-1]
        result_dict[string1] = longest_subsequence
    max_value = max(result_dict.values())
    # print(result_dict)
    for category, value in result_dict.items():
        if value == max_value:
            matching_categories.append(category)
    print("Based on your response, the available types of clothing are:", end=" ")
    print(matching_categories)
    print("")
        # print(longest_subsequence)
        # result = []
        # while row > 0 and col > 0:
        #     if string1.lower()[row - 1] == response_1.lower()[col - 1]:
        #         result.append(string1[row - 1])
        #         row -= 1
        #         col -= 1
        #     elif grid[row - 1][col] > grid[row][col - 1]:
        #         row -= 1
        #     else:
        #         col -= 1
        # result.reverse()
        # longest_match = "".join(result)
        # # print(longest_match)

# Allow the user choose out of the available major clothing categories. Match the user response with ONE major clothing category.
    matching_cat_dict = {}
    winning_category = []
    response_2 = input("Which of these type(s) of clothing do you seek to purchase?: ")
    print("")
    for string2 in matching_categories:
        grid = [[0 for char in range(0, len(response_2)+1)] for char in range(0, len(string2)+1)]
        for row in range(1, len(string2)+1):
            for col in range(1, len(response_2)+1):
                if string2.lower()[row-1] == response_2.lower()[col-1]:
                    grid[row][col] = grid[row - 1][col - 1] + 1
                else:
                    grid[row][col] = max(grid[row-1][col], grid[row][col-1])
        longest_subsequence = grid[-1][-1]
        matching_cat_dict[string2] = longest_subsequence
    max_value = max(matching_cat_dict.values())
    # print(sub_cat_dict)

#Print the chosen major category alogside its subcategories.
    for category, value in matching_cat_dict.items():
        if value == max_value:
            winning_category.append(category)
    print(f"Based on your chosen clothing category, {winning_category[0]}, the available types of {winning_category[0]} are:")
    print("")
    if winning_category[0] == 'Bags':
        selection_list = ['Backpacks', 'Bum bags', 'Wallets', 'Clutch bags', 'Sling bags']
    elif winning_category[0] == 'Dresses':
        selection_list = ['Wrap dresses', 'Trapeze dresses', 'Bandeau dresses', 'Fish tail dresses', 'Jumper dresses']
    elif winning_category[0] == 'Footwear':
        selection_list = ['Sneakers', 'Sandals', 'Heels', 'Chelsea boots', 'Loafers']
    elif winning_category[0] == 'Accessories':
        selection_list = ['Neckpieces', 'Scarves', 'Finger Rings', 'Earrings', 'Anklets']
    elif winning_category[0] == 'Tops':
        selection_list = ['Polo Shirts', 'Crop Tops', 'Corset Tops', 'Kimonos', 'Bodies']
    elif winning_category[0] == 'Jeans_trousers':
        selection_list = ['Skinny Jeans', 'High waisted Jeans', 'Shorts', 'flared Jeans', 'Ripped Jeans']
    else:
        selection_list = ['Pleated Skirts', 'A Line Skirts', 'Bodycon Skirts', 'Mini Skirts', 'Jipsy Skirts']
    print(selection_list)
    print("")
    print("")

    #Ask the user if they will like to see all available subcategories for the major category chosen, or just a specific child item. 
    def get_child_category():
        print(f"Will you like to view all the available {winning_category[0]}? Or just a specific type?")
        print("")
        response_3 = input(f"Enter - 1 - to view all the types of {winning_category[0]} or - 2 - to view just a specific type: ")
        print("")
        #If they want to see ALL - print the Node for that subcategory.
        selection_list = []
        if int(response_3) == 1:
            print(f"The available {winning_category[0]} for purchase are: ")
            if winning_category[0] == 'Bags':
                print(bags)
            elif winning_category[0] == 'Dresses':
                print(dresses)
            elif winning_category[0] == 'Footwear':
                print(footwear)
            elif winning_category[0] == 'Accessories':
                print(accessories)
            elif winning_category[0] == 'Tops':
                print(tops)
            elif winning_category[0] == 'Jeans_trousers':
                print(jeans_trousers)
            elif winning_category[0] == 'Skirts':
                print(skirts)
            else:
                print("Sorry, We do not have what you need at this time. Please check back soon.")
        #If not, ask for the specific child item they want to see
        elif int(response_3) == 2:
            print('Which of these will you like to proceed with?')
            print("")
            if winning_category[0] == 'Bags':
                selection_list = [backpacks, bum_bags, wallets, clutch_bags, sling_bags]
            elif winning_category[0] == 'Dresses':
                selection_list = [wrap_dresses, trapeze_dresses, bandeau_dresses, fish_tail_dresses, jumper_dresses]
            elif winning_category[0] == 'Footwear':
                selection_list = [sneakers, sandals, heels, chelsea_boots, loafers]
            elif winning_category[0] == 'Accessories':
                selection_list = [neckpieces, scarves, finger_rings, earrings, anklets]
            elif winning_category[0] == 'Tops':
                selection_list = [polo_shirts, crop_tops, corsets, kimonos, bodies]
            elif winning_category[0] == 'Jeans_trousers':
                selection_list = [skinny_jeans, high_waisted, shorts, flared_jeans, ripped_jeans]
            else:
                selection_list = [pleated_skirts, a_line_skirts, bodycon_skirts, mini_skirts, jipsy_skirts]
            count = 0

            for item in range(0, len(selection_list)):
                count += 1
                print("Enter " + str(count) + " for " + selection_list[item].value)
                print("")

            def get_child_items():
                response_4 = input("Choose one between options 1 to 5: ")
                print("")
                if ((int(response_4) - 1) > (len(selection_list) - 1)) or ((int(response_4) - 1) < 0):
                    get_child_items()
                print(f"The available {selection_list[int(response_4) - 1].value} for purchase are: ")
                print(selection_list[int(response_4) - 1])
            get_child_items()
        else:
            print("Choose - 1 - to view all types and - 2 - to view a specific type.")
            get_child_category()
        
    get_child_category()




def thank_you():
    print(f"Thank you for your purchase, {customer_name}!")
    print("We hope you visit us for more purchases soon! 😊🌹")


def yinnie_body_shop():
    personalized_greeting()
    get_response()


yinnie_body_shop()


# Bags = ['Backpacks', 'Bum bags', 'Wallets', 'Clutch bags', 'Sling bags']
# Dresses = ['Wrap dresses', 'Trapeze dresses', 'Bandeau dresses', 'Fish tail dresses', 'Jumper dresses']
# Footwear = ['Sneakers', 'Sandals', 'Heels', 'Chelsea boots', 'loafers']
# Accessories = ['Neckpieces', 'Scarves', 'Finger Rings', 'Earrings', 'Anklets']
# Tops = ['Polo Shirts', 'Crop Tops', 'Corset Tops', 'Kimonos', 'Bodies']
# Jeans_trouser = ['Skinny Jeans', 'High waisted Jeans', 'Shorts', 'flared Jeans', 'Ripped Jeans']
# Skirts = ['Pleated Skirts', 'A Line Skirts', 'Bodycon Skirts', 'Mini Skirts', 'Jipsy Skirts']

