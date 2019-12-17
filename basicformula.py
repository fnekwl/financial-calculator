import math
from IPython.display import clear_output

def future_value(pv,i,t,freq):
	clear_output()
	freq_dict = {'d':365,'m':12,'q':4,'s':2,'a':1}
	n = freq_dict[freq.lower()[0]]
	fv = int(pv*(1+(i/100)/n)**(t*n))
	print('The present value of your investment is {}'.format(fv))

def present_value(fv,i,t,freq):
	clear_output()
	freq_dict = {'d':365,'m':12,'q':4,'s':2,'a':1}
	n = freq_dict[freq.lower()[0]]
	pv = int(fv/(1+(i/100)/n)**(t*n))
	print('The present value of your investment is {}'.format(pv))

def rate(fv,pv,t,freq):
	clear_output()
	freq_dict = {'d':365,'m':12,'q':4,'s':2,'a':1}
	n = freq_dict[freq.lower()[0]]
	i = (fv/pv)**(1/(n*t)) - 1
	eff_rate = i*n*100
	print('Your money will grow from ${1:,.0f} into ${2:,.0f} in {3:,.0f} year(s) with {0:.2f}% effective annual rate'.format(eff_rate,pv,fv,t))

def years(fv,pv,i,freq):
	clear_output()
	freq_dict = {'d':365,'m':12,'q':4,'s':2,'a':1}
	n = freq_dict[freq.lower()[0]]
	t =  math.log((fv/pv),(1+(i/100)/n))
	year = t/n
	print('Your money will grow from ${1:,.0f} into ${2:,.0f} with {3:,.2f}% effective annual rate after {0:.1f} year(s)'.format(year,pv,fv,i))