# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
   ]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
    result = (weekday(day_number) + ': ')
    meal_count = len(meal_plan[day_number])
    for index in range(meal_count-1):
        result += meal_plan[day_number][index]
        result += ', '
    result += meal_plan[day_number][meal_count-1]
    return result
      
# Prints weekly meal plan
print('WEEKLY MEAL PLAN:\n(Breakfast,Lunch,Dinner)\n==========================')
for day in range(7):
   print(day_meal_plan(meal_plan, day))