height = 1.85 
weight = 85

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
print(f"BMI: {bmi}", type(bmi))
if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi < 25:
    print("Normal weight")

else:
    print("Overweight")