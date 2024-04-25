import re
P = "110000"
# P = "101"
# match when you dont see it
# regex_integer_in_range = r"^(?!\d{6,6}$).*"
# match when you see it
regex_integer_in_range = r"\d{6,6}$"
# match when you dont see it
regex_alternating_repetitive_digit_pair = r"(.)(.)\1\2+"
# match when you see it
# negative_regex_alternating_repetitive_digit_pair = r"(.).\1{1,}"

in_range =bool(re.match(regex_integer_in_range, P))
repeat = len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
matches =  in_range and repeat

print(in_range, repeat, matches)
print("matches:", len(re.findall(regex_alternating_repetitive_digit_pair,P)))
