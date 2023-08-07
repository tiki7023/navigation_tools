with open("file.txt", "r",encoding='gb18030',errors='ignore') as f:
    lines = f.readlines()
    words = []
    for line in lines:
        words.append(line.strip().split())
    print(words)