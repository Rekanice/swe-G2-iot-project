#!/usr/bin/python
content = []
src_file_name = 'xmaslist.txt'
with open(src_file_name, 'r') as f:
	content = f.readlines()

print('Hello, Jason.')
print('Xmas is coming soon. Here is your buy list:\n')
for item in content:
	print(' - ' + item)

answer = input('Do you want to edit the list? (y/n): ')
if(answer=='y'):
	answer = input('Add or Drop item (a/d): ')

	if(answer == 'a'):
		new = input('Enter the new item: ')
		with open(src_file_name, 'a+') as f:
			f.append(new)
			print('Here is the updated list:')
			print(f.readlines())

	if(answer == 'd'):
		new = input('Enter the to-be-drop item: ')
		with open(src_file_name, 'r+') as f:
			content = f.readlines()
			content.remove(new)
			f.write(content)
			print('Here is the updated list:')
			print(f.readlines())

elif(answer=='n'):
	pass

print('\nNow go forth & seize the day! Carpe fookin diem')
