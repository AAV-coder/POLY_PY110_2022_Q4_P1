def human_cat_dog_age(HumanYears: int):


  if 0 < HumanYears <= 1:
    cat_years = 15
    dog_years = 15
  elif 1 < HumanYears <= 2:
    cat_years = 15 +9 
    dog_years = 15 + 9
  else:
    cat_years = 24 + HumanYears * 4
    dog_years = 24 + HumanYears * 5
    
  return [HumanYears, cat_years, dog_years]
  
  
print(human_cat_dog_age(1))
print(human_cat_dog_age(2))
print(human_cat_dog_age(10))


