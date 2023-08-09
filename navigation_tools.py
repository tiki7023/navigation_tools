import re
import pandas as pd
sheets = ['常用网站','办公工具','视频网站','资源搜索','学校网站','学术网站','游戏相关','程序员','社交网站','数码跑分','导航页']
result_total = ''
for i in range(len(sheets)):
    df = pd.read_excel('option.xlsx',sheet_name = sheets[i])
    df.to_csv('.\website\{name}.txt'.format(name = sheets[i]), header=None, sep=' ', index=False)

    with open('.\website\{name}.txt'.format(name = sheets[i]), 'r',encoding='utf-8') as f:
        lines = f.readlines()
        options = []
        for line in lines:
            options.append(line.strip().split())
        print(options)

    with open("file.html", "r", encoding='utf-8') as f:
        content = f.read()
    html = ''

    for j in range(len(options)):
        selected_option = options[j][0]
        content = re.sub(r"'.*?', '_blank'", f"'{selected_option}', '_blank'", content)

        selected_option = options[j][0]
        content = re.sub(r'le=".*?">', f'le="{selected_option}">', content)


        selected_option = options[j][1]
        content = re.sub(r'src=".*?" class="', f'src="{selected_option}" class="', content)

        selected_option = options[j][2]
        content = re.sub(r"<strong>.*?</strong>", f"<strong>{selected_option}</strong>", content)

        selected_option = options[j][3]
        content = re.sub(r'overflowClip_2">.*?</p>', f'overflowClip_2">{selected_option}</p>', content)
        if html == '':
            html = content
        else:
            html = html + '\n' +content
    html = '\t\t\t'+'<h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id="'+sheets[i]+'"></i>'+sheets[i]+'</h4>'+'\n'+'\t\t\t'+'<div class="row">'+'\n'+html

    result_total =result_total+'\n'+html+'\n'+'</div>'
    print(html)

    with open(r'.\results\{name}.txt'.format(name = sheets[i]), 'w',encoding='utf-8') as f:
        f.write(html)
with open(r'head.html','r',encoding='utf-8') as f:
    head = f.read()
with open(r'foot.html','r',encoding='utf-8') as f:
    foot = f.read()
result_total = head + result_total + foot
with open(r'.\index.html', 'w',encoding='utf-8') as f:
    f.write(result_total)
