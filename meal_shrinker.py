# This Python file uses the following encoding: utf-8
from fractions import Fraction
import re
import math

with open("recipe.txt") as my_recipe: 
	recipe = my_recipe.readlines()

def preprocess_vulgar(line):
	# Takes a line as a string and returns back the line but with vulgar unicode fractions replaced.
	line = line.replace('½', '1/2').replace('⅓', '1/3').replace('¼', '1/4').replace('¾', '3/4')
	return line

def preprocess_tight_fractions(line):
	if re.match(r'(\d)(\d/\d+)', line): # finds a digit next to a fraction w/o a space
		line = re.sub(r'(\d)(\d/\d+)',  r'\1 \2', line)  #adds a space between digit and fraction; \1 and \2 select groups with parenthesis in regex
	return line	

def preprocess_hyphen(line):
	if re.search(r'(\d+)(-)(\d+/\d+)', line):
		line = re.sub(r'(\d+)(-)(\d+/\d+)', r'\1 \3', line)
	return line

def find_digit_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL): #(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
		matched = re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL)
		matched_str_beginning = matched.group(1)
		return matched_str_beginning
	else:
		return False

def find_digit(match_str):
	# return found digit
	if re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL)
		matched_digit = Fraction(matched.group(2))
		return matched_digit
	else:
		return False

def digit_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(3)
		return matched_str_remainder
	else:
		return False

def find_digit_into(match_str):
	# finds out if the word "into" is before the digit
	if re.match(r'([^\d]*)(into\s\d+)(.*)', match_str, re.DOTALL):
		return True
	else:
		return False

def frac_str_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL)
		frac_str_1st = matched.group(1)
		return frac_str_1st
	else:
		return False

def find_fraction(match_str):
	# return found fraction
	if re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL)
		matched_frac = Fraction(matched.group(2))
		return matched_frac
	else:
		return False

def frac_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(3)
		return matched_str_remainder
	else:
		return False

def find_frac_into(match_str):
	# finds out if the word "into" is before fraction
	if re.match(r'([^\d]*)(into\s\d+/\d+)(.*)', match_str, re.DOTALL):
		return True
	else:
		return False

def mixed_num_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL)
		matched_num_1st = matched.group(1)
		return matched_num_1st
	else:
		return False

def find_mixed_num(match_str):
	# return found mixed num
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL)
		num_matched = Fraction(matched.group(2))
		matched = num_matched + Fraction(matched.group(3))
		return matched
	else:
		return False

def mixed_num_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(4)
		return matched_str_remainder
	else:
		return False

def find_mixed_num_into(match_str):
	# finds out if the word "into" is before found mixed num
	if re.match(r'([^\d]*)(into\s\d+\s\d+/\d+)(.*)', match_str, re.DOTALL):
		return True
	else:
		return False

def float_str_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL)
		matched_float_1st = matched.group(1)
		return matched_float_1st
	else:
		return False

def find_float(match_str):
	# return float
	if re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL)
		matched_float = matched.group(2)
		return float(matched_float)
	else:
		return False

def float_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+\.\d+)(.*)', match_str, re.DOTALL)
		matched_float_remainder = matched.group(3)
		return matched_float_remainder
	else:
		return False

def find_float_into(match_str):
	# finds out of the word "into" is before float
	if re.match(r'([^\d]*)into\s(\d+\.\d+)(.*)', match_str, re.DOTALL):
		return True
	else:
		return False

def halve_values(string):
	if find_float(string):
		string = str(find_float(string)/2)
	elif find_mixed_num(string):
		string = str(find_mixed_num(string)/2)
	elif find_fraction(string):
		string = str(find_fraction(string)/2) 
	elif find_digit(string):
		string = str(find_digit(string)/2)
	return string

def post_process_value(value):
	# if halve_values(value):
	value = Fraction(halve_values(value))
	if value.denominator == 1:
		return str(value.numerator)
	elif value.numerator > value.denominator:
		whole_num = int(math.floor(value)) # math.floor() gets the whole number out of the improper fraction; floor works by rounding down to the next whole number as a float
		frac_num = value - whole_num
		frac_num =  str(whole_num) + " " + str(Fraction(frac_num))
		return frac_num
	else:
		return str(value)


def replace_all(recipe):
	new_recipe = []
	for line in recipe:
		line = preprocess_vulgar(line)
		line = preprocess_tight_fractions(line)
		line = preprocess_hyphen(line)
		new_recipe.append(line)	
	return new_recipe  

recipe = replace_all(recipe)

recipe = "".join(recipe) # makes recipe a string again

def output(line):
	if find_float(line):
		if find_float_into(line):
			return float_str_1st_part(line) + str(find_float(line)) + output(float_str_remainder(line))
		else:
			return float_str_1st_part(line) + post_process_value(line) + output(float_str_remainder(line))
	elif find_mixed_num(line):
		if find_mixed_num_into:
			return mixed_num_1st_part(line) + str(find_mixed_num(line)) +  output(mixed_num_str_remainder(line)) #fix so that mixed num is returned, not improper frac
		else:
			return mixed_num_1st_part(line) + post_process_value(line) +  output(mixed_num_str_remainder(line))
	elif find_fraction(line):
		if find_frac_into(line):
			return frac_str_1st_part(line) + str(find_fraction(line)) +  output(frac_str_remainder(line))
		else:
			return frac_str_1st_part(line) + post_process_value(line) +  output(frac_str_remainder(line))
	elif find_digit(line):
		if find_digit_into(line):
			return find_digit_1st_part(line) + str(find_digit(line)) + output(digit_str_remainder(line))
		else:
			return find_digit_1st_part(line) + post_process_value(line) + output(digit_str_remainder(line))
	else:
		return line
print output(recipe)
