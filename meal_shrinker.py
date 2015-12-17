# This Python file uses the following encoding: utf-8
import fractions
import re
import math

with open("test_recipe2.txt") as my_recipe: 
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
	if re.search(r'(\d+)(-)', line): # removes dash if it comes after a digit
		line = re.sub(r'(\d+)(-)()', r'\1 \3', line)
	return line

def find_digit_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL)
		matched_str_beginning = matched.group(1)
		return matched_str_beginning
	else:
		return False

def find_digit(match_str):
	# return found digit
	if re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL)
		matched_digit = fractions.Fraction(matched.group(2))
		return matched_digit
	else:
		return False

def digit_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(3)
		return matched_str_remainder
	else:
		return False

def frac_str_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		frac_str_1st = matched.group(1)
		return frac_str_1st
	else:
		return False

def find_fraction(match_str):
	# return found fraction
	if re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		matched_frac = fractions.Fraction(matched.group(2))
		return matched_frac
	else:
		return False

def frac_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(3)
		return matched_str_remainder
	else:
		return False

def mixed_num_1st_part(match_str):
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		matched_num_1st = matched.group(1)
		return matched_num_1st
	else:
		return False

def find_mixed_num(match_str):
	# return found mixed num
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		num_matched = fractions.Fraction(matched.group(2))
		matched = num_matched + fractions.Fraction(matched.group(3))
		return matched
	else:
		return False

def mixed_num_str_remainder(match_str):
	if re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL):
		matched = re.match(r'([^\d]*)(\d+)\s(\d+/\d+)\s(.*)', match_str, re.DOTALL)
		matched_str_remainder = matched.group(4)
		return matched_str_remainder
	else:
		return False

# def find_float(line):

def halve_values(string):
	if find_mixed_num(string):
		string = str(find_mixed_num(string)/2)
	elif find_fraction(string):
		string = str(find_fraction(string)/2) 
	elif find_digit(string):
		string = str(find_digit(string)/2)
	return string

def post_process_value(value):
	value = fractions.Fraction(halve_values(value))
	if value.denominator == 1:
		return str(value.numerator)
	elif value.numerator > value.denominator:
		whole_num = int(math.floor(value))
		frac_num = value - whole_num
		frac_num =  str(whole_num) + " " + str(fractions.Fraction(frac_num))
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
	if find_mixed_num(line):
		return mixed_num_1st_part(line) + post_process_value(line) + " " + output(mixed_num_str_remainder(line))
	elif find_fraction(line):
		return frac_str_1st_part(line) + post_process_value(line) + " " + output(frac_str_remainder(line))
	elif find_digit(line):
		return find_digit_1st_part(line) + post_process_value(line) + " " + output(digit_str_remainder(line))
	else:
		return line
print output(recipe)


