weight = input('please type in kilogram: ')
height = input('please type in meter: ')
weight = float(weight)
height = float(height)
BMI = weight / height / height
if BMI >= 18.5 and BMI < 24:
    print('Normal')
elif BMI < 18.5	:
	print('Too light')
elif BMI >= 24 and BMI < 27:
	print('Too heavy')
elif BMI >= 27 and BMI < 30:
	print('Slightly fat')
elif BMI >= 30 and BMI < 35:
	print('A bit fat')
else:
	print('Too fat!!')