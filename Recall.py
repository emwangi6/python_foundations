print('Whats your name')
name =input('>')
print(f'Nice to meet you {name}')
print('Your name has a length of ' + str(len(name)) + ' letters')
print('How old are you')
age =int(input('>'))

if(age+1 < 18):
    print(f'You will be {age+1} next year not eligibale to vote')
else:
    print(f'You will be {age+1} next year eliigble to vote')