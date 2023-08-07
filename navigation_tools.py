import re

with open("file.html", "r",encoding='utf-8') as f:
    content = f.read()
############
# pattern = re.compile(r"<strong>(.*?)</strong>")
# match = pattern.search(content)
# if match:
#     title = match.group(1)
#
# options = [["Option 1", "Option 2", "Option 3"], ["Option A", "Option B", "Option C"]]
# selected_option = options[0][0]
#
# content = re.sub(r"<strong>.*?</strong>", f"<strong>{selected_option}</strong>", content)

###########
pattern = re.compile(r"'(.*?)', '_blank'")
match = pattern.search(content)
if match:
    title = match.group(1)

options = [["Option 1", "Option 2", "Option 3"], ["Option A", "Option B", "Option C"]]
selected_option = options[0][0]

content = re.sub(r"'.*?', '_blank'", f"'{selected_option}', '_blank'", content)

content = content+'\n'+content

print(content)