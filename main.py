
import re
user= "niraj_kumar_25032001"
roll="12006047"
email="niraj2503kumar@gmail.com"
str=input().strip()
n=re.findall(r'\d+',str)
charls=re.findall(r'[a-zA-Z]+',str)
print("user_id:",user)
print("email:",email)
print("roll_number:",roll)
print("alphabets :",charls)
lis = n
res = [eval(i) for i in lis]
#print("Modified list is: ", res)


evenls=[]
oddls=[]
for i in range(len(res)):
  if res[i]%2==0:
    evenls.append(res[i])
  else:
    oddls.append(res[i])

print("even numbers :",evenls)
print("odd numbers :",oddls)


    
    

    
    
  