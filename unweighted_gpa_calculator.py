print('''
\n
Unweighted GPA Calculator
Designed by KalebJS
\n
''')

boolean = True
convert = {
	'a+' : 4.3,
	'a' : 4.0,
	'a-' : 3.7,
	'b+' : 3.3,
	'b' : 3.0,
	'b-' : 2.7,
	'c+' : 2.3,
	'c' : 2.0,
	'c-' : 1.7,
	'd+' : 1.3,
	'd' : 1.0,
	'd-' : .7,
	'e' : .3,
	'f' : 0
}
def input_grade(gradeType) :
	boolean = True
	grade = []
	print('Enter grade. When finished, press enter with an empty prompt')
	while boolean :

		if gradeType == 'l' :
			
			gradeInput = raw_input('Grade: ').lower()

			if gradeInput in convert :
				grade.append(convert[gradeInput])
			elif gradeInput == '' :
				boolean = False
			else :
				print('\nInvalid input. Try again.\n')

		elif gradeType == 'n' :
			gradeInput = raw_input('Grade: ')

			if gradeInput == '' :
				boolean = False
			elif float(gradeInput) >= 0 and float(gradeInput) <= 4.3 :
				grade.append(float(gradeInput))
			else :
				print('\nInvalid input. Try again.\n')

	print('\n\nYour grade is a ')
	print(sum(grade) / len(grade))



while boolean == True :
	dataType = raw_input('Input as letter grade or 4.0 scale (l/n): ')
	if dataType == 'l' or dataType == 'n' :
		boolean = False
		input_grade(dataType)
	else : 
		print('Please input either \"l\" or \"n\"')


print('''
\n\n
End Python Script
''')