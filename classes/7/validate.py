import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov)$", email, re.IGNORECASE):   #or ("..*@..*, email") bcs + = .* and \w = [a-zA-Z0-9_]
    print("Valid")
else:
    print("Invalid")