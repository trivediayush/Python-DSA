str1 = "Roman"
str2 = "Reigns"

print(f'String concatenation: {str1 + " " + str2}')
print(f'Length of string "{str1}": {len(str1)}')
print(f'Capitalize the string "{str1}": {str1.capitalize()}')
print(f'Upper the string "{str1}": {str1.upper()}')
print(f'Lower the string "{str1}": {str1.lower()}')
print(f'Replace the string "{str2}": {str2.replace("Reigns", "Empire")}')
print(f'Split the string "{str2}": {str2.split(" ")}')
print(f'Find in the string "{str1}": {str1.find("Ro")}')
print(f'Check if "{str1}" starts with "Ro": {str1.startswith("Ro")}')
print(f'Check if "{str1}" ends with "an": {str1.endswith("an")}')
print(f'Count occurrences of "a" in "{str1}": {str1.count("a")}')
print(f'Join strings with "-": {"-".join([str1, str2])}')
print(f'First character of "{str1}": {str1[0]}')
print(f'Slice the string "{str1}" from index 1 to 3 : {str1[1:3]}')
print(f'Get the last character of "{str1}": {str1[-1]}')