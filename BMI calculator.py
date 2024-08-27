print("Welocme to the BMI calculator : ")
weight=float(input("Please enter your weight : "))
height=float(input("Please enter your height : "))
bmi=round(weight/(height*height))
if bmi < 18.5 :
    print(f"Your BMI is {bmi},your slightly underweight ")
elif 18.5 < bmi < 26 :
    print(f"Your BMI is  {bmi},You have normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is  {bmi},Your slightly overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is  {bmi},Your obese")
else:
    print(f"your BMI {bmi},your clinically obese")