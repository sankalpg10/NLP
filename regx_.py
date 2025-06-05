import re


#to match at the beginning of string ->match

res = re.match("pattern to match", "pattern to match in the given string")
print("res start: ",res.start())
print("res start: ",res.end())

#to match anywhere -> search

res = re.search(r"pattern","string pattern string pattern")
print("matchedv: ",res.group(0))

#to get all occurences -> findall

res = re.findall(r"pattern","string pattern string pattern")
print(res)

#to split string using a letter

res_ = re.split(r"y","analytics")
print(res_)

#to search a pattern and replace with a new sub string
res_ = re.sub(r"pattern","new","string pattern string pattern",)
print(res_)

#to match anywhere and returns an iterator yielding match objects matching the
# regex pattern in a string instead of a list.

target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with a scoring average of 26.12 points per game. Her weight is 51 kg."
res = re.finditer(r"\d{2}", target_string)