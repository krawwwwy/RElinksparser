import re
import requests

with open('input.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

pattern = re.compile(r'<a\s+href="(.*?)">')
matches = re.findall(pattern, html_content)

for match in matches:
    try:
        response = requests.get(match)
        if response.status_code == 200:
            print(match)
    except:
        pass
