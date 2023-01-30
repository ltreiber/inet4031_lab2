#!/usr/bin/env python3
users = []
toprint = []
skipped = False
s = ""
with open("fileprocessor.input") as file:
	for line in file:
		users.append(line.rstrip())
	file.close()
for line in users:
	s = ""
	tempList = []
	for char in line:
		if char == ':':
			tempList.append(s)
			s = ""
		else:
			s += char
	tempList.append(s)
	toprint.append(tempList)

#Print Loop

for a in toprint:
	if(a[0][0] != "#"):
		print("The user " + a[0] + " has a password of " + a[1] + " and has userid " + a[2] + " and groupid " + a[3])
	else:
		user = a[0]
		print(user[1:] + " is skipped because it starts with a hashtag")
