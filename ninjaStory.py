amount = int(input("Enter the amount of money the ninja have with him :   "))
cost = int(input("Enter the cost of each story that the storyteller charges :  "))
offer = int(input("Enter the number of stories that the ninja has to buy so that he gets a story for free :  "))
no_of_story_could_be_bought = amount/cost
offer_story = no_of_story_could_be_bought/offer
total = no_of_story_could_be_bought + offer_story
print("The total number of stories the Ninja could hear are :  ",total)