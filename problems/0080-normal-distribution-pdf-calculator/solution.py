import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	var=(x-mean)**2
	v=2*std_dev**2
	p=-var/v
	num=math.exp(p)
	pi=math.pi
	denom=math.sqrt(2*pi*std_dev**2)
	val=num/denom
	return round(val,5)