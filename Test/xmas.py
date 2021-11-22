#!/usr/bin/python
def printlist(ls):
	for item in ls:
		print(' - ' + item)

content = []
src_file_name = 'xmaslist.txt'
with open(src_file_name, 'r') as f:
	content = f.readlines()

print('Hello, Jason.')
print('Xmas is coming soon. Here is your buy list:\n')
printlist(content)

answer = input('Do you want to edit the list? (y/n): ')
if(answer=='y'):
	answer = input('Add or Drop item (a/d): ')

	if(answer == 'a'):
		new = input('Enter the new item: ')
		with open(src_file_name, 'a+') as f:
			f.writelines(new+'\n')
			
		with open(src_file_name, 'r') as f:
			print('\nHere is the updated list:')
			printlist(f.readlines())

	if(answer == 'd'):
		new = input('Enter the to-be-drop item: ')
		with open(src_file_name, 'r+') as f:
			content = f.readlines()
			f.seek(0)
			content.remove(new+'\n')
			content_stringed = ''.join(content)
			f.write(content_stringed)
			f.truncate()

		with open(src_file_name, 'r') as f:
			print('\nHere is the updated list:')
			printlist(f.readlines())

elif(answer=='n'):
	pass

print('\nNow go forth & seize the day! Carpe fookin diem!\n')
