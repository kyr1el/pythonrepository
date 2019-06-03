with open('referat.txt', 'r', encoding='utf-8') as text:
    content = text.read()
    content = content.replace('.', '!')
    print(content)
    print(len(content))
