import httpx
print('''
  _    _            _     
 | |  | |          (_)    
 | |__| | __ _ _ __ _ ___ 
 |  __  |/ _` | '__| / __|
 | |  | | (_| | |  | \__ 
 |_|  |_|\__,_|_|  |_|___/
                                            
Author: ! Haris#9999 and - ΛПS 🥀#2022                            
Website: https://harisxd.tk 
Github: https://github.com/Haris123346/Web-Skidder                           
''')
url = input("Enter your website URL: ")
r = httpx.get(url)

with open("code.txt", "a") as f:
    f.write(f"Website: {url}\n\nCode:\n{r.text}\n\n\n")