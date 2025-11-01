age = int(input())
person = ""
if age <= 14:
    person = "kid"
    print("drink toddy")
elif age <= 18:
    person = "teen"
    print("drink coke")
elif age <= 21:
    person = "young adult"
    print("drink beer")
else:
    person = "adult"
    print("drink whisky")
