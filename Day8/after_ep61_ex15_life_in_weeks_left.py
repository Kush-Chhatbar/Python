def life_in_weeks(age):
    current_age = age
    total_weeks = 52
    
    age_left = 90 - int(current_age)
    total_weeks_left = age_left * total_weeks
    
    print(f"You have {total_weeks_left} weeks left.")
    
life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)
