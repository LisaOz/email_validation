import re # regular expressions

email = input("Please enter your email: ").strip() # promt to the user to enter email and strip beginning and trailing white space characters

"""
email pattern:
r - raw string
^ - beginning of the string
.+ one or more characters
\w - alpha-numeric character and an underscore
$ - end of the string
(\w+\.)? - this sequence of alphanumerical characters cold be used once or zero times

"""
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|org|net|gmail|com)$", email, re.IGNORECASE):
    print("Email is valid")

else:
    print("Email is invalid")