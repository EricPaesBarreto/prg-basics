height = int(input("please enter your height in cm"))
weight = int(input("please enter your weight in kg"))
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi, 'Check on the Internet if your BMI is ok!! (keep in mind that it is not verry accurate, and only gives you an idea of your health. Stay health consious!)')