import re

def build_match_and_apply_functions(pattern, search, replace): 
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (matches_rule, apply_rule)

rules = []
with open('plural-rules.txt', encoding='utf-8') as pattern_file:
	for line in pattern_file: 
		pattern, search, replace = line.split(None,3) #None refers to any whiltespace,tabs,blankspace...
		rules.append(build_match_and_apply_functions(pattern, search, replace))

def plural(noun):
	for matches_rule, apply_rule in rules:
		if matches_rule(noun):
			return apply_rule(noun)

print(plural('kid'))
print(plural('agency'))
print(plural('bass'))
print(plural('rash'))