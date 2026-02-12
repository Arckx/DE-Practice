#Challenge 1

#Validate the Quality and Correctness of Email values

email = "ahmed@gmail.com"
valid = True
#Clean the string
email = email.strip()
#email must not be empty
if email == "":
    print("Eamil cannot be empty")
    valid = False
#email must contain '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
#email must contain one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False
#email must end with '.com', '.org' or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("EMail must end with .com, .org or .net")
    valid = False
#emal must not be longer than 254
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False
#email must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")


#Inline IF ELSE
# if score > 90:
#     print("A")
# else:
#     print("F")
#      OR
# print("A" if score > 90 else "F")
#Each if will need else, cannot use elif here.
#For simple logic only