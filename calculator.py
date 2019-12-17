import basicformula as bsf
import replay_prompt as rpl
from IPython.display import clear_output

print('Hi, welcome to your financial calculator!')

while True:
	clear_output()
	action = int(input('What can I help you here?\n1: Future Value, \n2: Present Value \n3. Effective annual rate\n4. Years'))

	if action == 1:
		pv = float(input('What is your present value? '))
		i = float(input('What percentage is your annual interest rate? (answer in %) '))
		t = float(input('How many years will your money be rolled with this interest? '))
		freq = input('How often is your money being charged with interest? (your answer may be annually, semi-annually, quarterly, monthly, or daily) ')
		bsf.future_value(pv,i,t,freq)

		input('Do you n')

	elif action == 2:
		fv = float(input('What is your expected future value? '))
		i = float(input('What percentage is your annual interest rate? (answer in %) '))
		t = float(input('How many years will your money be rolled with this interest? '))
		freq = input('How often is your money being charged with interest? (your answer may be annually, semi-annually, quarterly, monthly, or daily) ')
		bsf.present_value(fv,i,t,freq)

	elif action == 3:
		fv = float(input('What is your expected future value? '))
		pv = float(input('What is your present value? '))
		t = float(input('How many years will your money be rolled with this interest? '))
		freq = input('How often is your money being charged with interest? (your answer may be annually, semi-annually, quarterly, monthly, or daily) ')
		bsf.rate(fv,pv,t,freq)

	elif action == 4:
		fv = float(input('What is your expected future value? '))
		pv = float(input('What is your present value? '))
		i = float(input('What percentage is your annual interest rate? (answer in %) '))
		freq = input('How often is your money being charged with interest? (your answer may be annually, semi-annually, quarterly, monthly, or daily) ')
		bsf.years(fv,pv,i,freq)

	else:
		print('We do not have that function currently.')
		pass
		
	if not rpl.replay():
		print('Thank you for using this calculator!')
		break