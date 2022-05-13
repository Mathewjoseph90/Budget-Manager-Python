# PROGRAM FOR BUGECT MANAGEMENT


class Budget:  #class creation
    def __init__(self,money,spending_food,spending_rent,spending_entertainment):

        self.money = money
        self.spending_food = spending_food
        self.spending_entertainment = spending_entertainment
        self.spending_rent = spending_rent
        budget_all = money // 3
        self.budget_all = budget_all

    def food(self):
        
        return self.budget_all - self.spending_food
    
    def rent(self):

        return self.budget_all - self.spending_rent
    
    def entertainment(self):

        return self.budget_all - self.spending_entertainment

# code outside the class

y = 1 # control variable 

while y==1: # looping so that it runs multiple times
    print("--Budget Manager--")
    print('')
    
    money = int(input("Enter the total budget :"))

    spending_food = int(input("Enter the money spend on food :"))
    print(f"The money spend on Food = {spending_food}")
    print(' ')

    spending_rent = int(input("Enter the money paid on rent :"))
    print(f"The money paid as rent = {spending_rent}")
    print(' ')
    
    spending_entertainment = int(input("Enter the money spend on entertainment :"))
    print(f"The money spend on entertaiment :{spending_entertainment}")
    print(' ')

    print('-'*20)
# creating an object and passing all the parameters
    
    obj = Budget(money,spending_food,spending_rent,spending_entertainment) 

# Budget of food
    print(f"Budget for food = {obj.budget_all}")
    food_budget = obj.food()
    if food_budget < 0 :
        print(f"The money spend over the budget on food = {obj.food()}")
    else:
        print(f"The money left after deduction = {obj.food()}")
    print(' ')


    print('-'*20)

# budget of rent
    
    print(f"Budget for rent = {obj.budget_all}")
    rent_budget = obj.rent()
    if rent_budget < 0 :
        print(f"The money spend over the budget on rent = {obj.rent()}")
    else:
        print(f"The money left after deduction = {obj.rent()}")
    print(' ')


    print('-'*20)
# budget of entertainment 
    
    print(f"Budget for entertainment = {obj.budget_all}")
    entertaiment_budget = obj.entertainment()
    if entertaiment_budget < 0 :
        print(f"The money spend over the budget on entertainment = {obj.entertainment()}")
    else:
        print(f"The money left after deduction = {obj.entertainment()}")
    print(' ')

    
    print('-'*20)
# Calculating total money spend 

    total_money_spend = spending_food + spending_rent + spending_entertainment
    print(f"Total money spend = {total_money_spend}")
    print(' ')
    
    print("-"*20)
# calculatingt if the user was over the budget or on budget

    if total_money_spend > money :
        print("Spendings over the budget ")
    else:
        print("On budget")
    
    print('-'*20)
    y = int(input("DO you want to restart (1 = Yes , 0 = No) :"))

print("Thank you")