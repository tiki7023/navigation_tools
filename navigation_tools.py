import re
import pandas as pd

df = pd.read_excel('option.xlsx')
df.to_csv('option.txt', header=None, sep=' ', index=False)

with open('option.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()
    options = []
    for line in lines:
        options.append(line.strip().split())
    print(options)

with open("file.html", "r", encoding='utf-8') as f:
    content = f.read()

html = ''

for i in range(len(options)):
    selected_option = options[i][0]
    content = re.sub(r"'.*?', '_blank'", f"'{selected_option}', '_blank'", content)

    selected_option = options[i][0]
    content = re.sub(r'le=".*?">', f'le="{selected_option}">', content)


    selected_option = options[i][1]
    content = re.sub(r'src=".*?" class="', f'src="{selected_option}" class="', content)

    selected_option = options[i][2]
    content = re.sub(r"<strong>.*?</strong>", f"<strong>{selected_option}</strong>", content)

    selected_option = options[i][3]
    content = re.sub(r'overflowClip_2">.*?</p>', f'overflowClip_2">{selected_option}</p>', content)
    if html == '':
        html = content
    else:
        html = html + '\n' +content

print(html)

with open('result.txt', 'w',encoding='utf-8') as f:
    f.write(html)