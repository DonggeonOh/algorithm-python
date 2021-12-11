str = 'https://naver.com'

left = str[8:str.index('.')]
right = str[str.index('.') + 1:]

word = left[:3]
len = len(left)
ecount = left.count('e')

print(f'{word}{len}{ecount}!')