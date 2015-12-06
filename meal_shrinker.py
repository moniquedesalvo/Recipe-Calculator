# This Python file uses the following encoding: utf-8
import fractions
import re
import math


with open("test_recipe2.txt") as my_recipe: 
	recipe = my_recipe.readlines()


def replace_all(recipe):
	new_recipe = []
	# replaces unicode fractions, also adds space between whole number and fraction
	for line in recipe:
		line = line.replace('½', '1/2').replace('⅓', '1/3').replace('¼', '1/4').replace('¾', '3/4') # returns fractions in plain string format

		if re.match('(\d)(\d/\d+)', line): # finds a digit next to a fraction w/o a space
			line = re.sub(r'(\d)(\d/\d+)',  r'\1 \2', line)  #adds a space between digit and fraction; \1 and \2 select groups with parenthesis in regex
			
		new_recipe.append(line)	
		
	return new_recipe
	
recipe = replace_all(recipe)



def find_digit(recipe):
	# searches through each line of the file to find a match on the beginning of a line
	for line in recipe:

		# double check below regex... might be wrong \D
		if re.match('^(\d+)\s(\D.*)', line): # starts search at the beginning of string; looks for a number, space, words
			found_digit = re.match('^(\d+)\s(\D.*)', line)

			digit_matched = fractions.Fraction(found_digit.group(1)) # the first set of parenthesis in re.match are .group(1) 
			remainder_of_string = found_digit.group(2) # the second set of parenthesis in re.match are .group(2); everything after the digits

			new_frac = digit_matched/2 # divides digit by 2
			
			if new_frac.numerator > new_frac.denominator: # if there's an improper fraction, changes item into mixed fraction

				whole_num = int(math.floor(new_frac)) # math.floor() gets the whole number out of the improper fraction; floor works by rounding down to the next whole number as a float
				frac_num = new_frac - whole_num # whole number subtracted from floor gives you the fraction portion 
				frac_num =  fractions.Fraction(frac_num) # makes frac_num into fraction format

				print whole_num, frac_num, remainder_of_string 

			else:
				print new_frac, remainder_of_string

find_digit(recipe)



def find_fraction(recipe):
	# finds fractions in recipe 
	for line in recipe:

		if re.match('^(\d+/\d+)\s(.*)', line): # starts at the beginning of string, looks for number, backslash, number, space, words

			found_fraction = re.match('^(\d+/\d+)\s(.*)', line)

			fraction_matched = fractions.Fraction(found_fraction.group(1))
			remainder_of_string = found_fraction.group(2)

			new_frac = fraction_matched/2

			if new_frac.numerator > new_frac.denominator:

				whole_num = int(math.floor(new_frac))
				frac_num = new_frac - whole_num 
				frac_num =  fractions.Fraction(frac_num)

				print whole_num, frac_num, remainder_of_string

			else:
				print new_frac, remainder_of_string

find_fraction(recipe)



def find_mixed_number(recipe):
	# finds mixed fractions 
	for line in recipe:

		if re.match('^(\d+)\s(\d+/\d+)\s(.*)', line): # starts at the beginning of string, looks for number, space, number, backslash, number, space, words
			found_mixed_number = re.match('^(\d+)\s(\d+/\d+)\s(.*)', line)

			num_matched = int(found_mixed_number.group(1))
			fraction_matched = fractions.Fraction(found_mixed_number.group(2))
			remainder_of_string = found_mixed_number.group(3)

			added = num_matched + fraction_matched

			new_frac = fractions.Fraction(added/2)

			if new_frac.numerator > new_frac.denominator:

				whole_num = int(math.floor(new_frac))
				frac_num = new_frac - whole_num 
				frac_num =  fractions.Fraction(frac_num)

				print whole_num, frac_num, remainder_of_string
			else:
				print new_frac, remainder_of_string

find_mixed_number(recipe)

