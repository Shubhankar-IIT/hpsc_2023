""" Python code for calculating cube root using Newton's Method"""
def cuberootN(x,debug=False,specialCases=True):

	if specialCases:
		if x==0.:
			return 0
	tol=1.0e-14
	s=1.
	kmax=100
	for k in range(kmax):
		if debug:
			print("At iteration number %s, s=%20.15f" %(k,s))
		s0=s
		s=(1/3)*(2*s+(x/s**2))
		delta_s=s-s0
		if(abs(delta_s/x))<tol:
			 break
	if debug:
		print("After %s iterations, s=%20.15f" %(k+1,s))
	return s
	
	def test_main():
		from numpy import cbrt
		xvalues=[0.,-64,100,1.0e6]
		
		for x in xvalues:
			print("Testing with x=%20.15e" %x)
			s=cuberootN(x)
			s_numpy=cbrt(x)
			print("cuberootN s=%20.15e,numpy s=%20.15e" %(s,s_numpy))
			
	
