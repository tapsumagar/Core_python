science=int(input('Enter the marks of Science'))
Math=int(input('Enter the marks of Math'))
social=int(input('Enter the marks of Social'))
Economics=int(input('Enter the marks of Economics'))
Education=int(input('Enter the marks of Education'))

sum=science+Math+social+Economics+Education
percentage=(sum/500)*100

if percentage== 100>90:
    print('A+')
elif percentage==80>90:
    print('A')
elif percentage==70>80:
    print('B+')
elif percentage==60>70:
    print('B')
elif percentage==80>90:
    print('A')
elif percentage==70>80:
    print('B+')
else:
    print('Pass')

