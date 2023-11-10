import re

with open('input.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

pattern = re.compile(r'<a\s+href="(.*?)">')
matches = re.findall(pattern, html_content)

for match in matches:
    print(match)
roses = 'red'
if roses == 'red':
    print('2-nd commit!!!!!')