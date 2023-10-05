import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([A-Za-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/$", "", url)
print(f"Username: {username}")
'''