age = 32

if age < 2:
    msg = "You are a baby"
elif 2 <= age < 4:
    msg = "You are a toddler"
elif 4 <= age < 13:
    msg = "You are a kid"
elif 13 <= age < 20:
    msg = "You are a teenager"
else:
    msg = "You are old. You get the point."

print(msg)