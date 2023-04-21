import requests
import hashlib
from bs4 import BeautifulSoup

r = requests.get("http://challenges.ringzer0team.com:10013/")
soup = BeautifulSoup(r.content, 'html.parser')
div_element = soup.find('div', {"class":"message"})

# print(div_element.text)
div_text = (div_element.text).strip()

start_pos = div_text.find('----- BEGIN MESSAGE -----') + len('----- BEGIN MESSAGE -----')
end_pos = div_text.find('----- END MESSAGE -----')

msg_txt = div_text[start_pos:end_pos].strip()
m = hashlib.sha512(msg_txt.encode())
m = m.digest()
print("\n")

x = requests.get(f"https://ringzer0ctf.com/challenges/13/{m}")
print(x.text)

