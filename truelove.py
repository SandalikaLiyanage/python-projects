print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total1=0
total2=0
combined_name=name1+name2
lower_case=combined_name.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
total1=t+r+u+e
total2=l+o+v+e
love_score=str(total1)+str(total2)
love_score=int(love_score)
if(love_score<10 or love_score>90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>40 and love_score<50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")