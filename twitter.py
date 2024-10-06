import re
url = input("URL: ").strip()    
#username = url.removeprefix("https://twitter.com/")

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/[a-z0-9_]", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:
    print("URL is incorect")