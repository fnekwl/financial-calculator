from IPython.display import clear_output

def replay():
	return input('Do you need anything else? (Y/N)?').lower().startswith('y')
	clear_output()