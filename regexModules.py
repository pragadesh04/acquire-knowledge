import webbrowser as wb
import time as t

t.sleep(0.5)
wb.open('https://github.com/pragadesh04')
t.sleep(2)
wb.open('https://github.com')


print("Working directory".center(88, "-"))
import os
print(os.getcwd())

import clipboard as cb
import re
print("Number Matching".center(88, "-"))
import re._compiler
mob_ = re.compile(r'(\+\d\d) (\d\d\d\d\d\d\d\d\d\d)')
str = "my phone number is +91 8667749882"
# searching the str using mob_ using re package
mo = mob_.search(str)

print(mo.group(1))
print(mo.group(2))

print("String Matchin with |".center(88, "-"))
mob_ = re.compile(r'Batman|pragadesh|i am Batman')
str = "pragadesh says \"i am Batman\"we cant believe he is Batman"
mo = mob_.findall(str)
print(str, " ", mo)

print("value start with digits end with alphas".center(88, "-"))
mob_ = re.compile(r'\d+\s\w+')
str = "2 apples, 5 bananas, 8 drumstick, 9 tomatoes"
mo = mob_.findall(str)
print(mo)

print("matches the letter using [] ".center(88, "-"))
mob_ = re.compile(r'[aeiouAEIOU]')
mob_1 = re.compile(r'[^aeiouAEIOU]')
str = "Hard WORK and Confidence"
print("The vowel count is {}".format(len(mob_.findall(str))))
print("The consonant count is {}".format(len(mob_1.findall(str))))

print("using DOT to choose previous character".center(88, "-"))
mob_ = re.compile(r'.at')
str = "cat in the hat takes that pat"
print(mob_.findall(str))

print("Choosing all the elements".center(88, "-"))
mob_ = re.compile(r'first name: (.*) last name: (.*)')
str = "first name: pragadesh last name: ptg"
# str = ""
print(mob_.findall(str))

print("Non Greedy".center(88, "-"))
mob_ = re.compile(r'<.*?>')
str = "<html>is the scripting language.>"
print(mob_.search(str).group())

print("Greedy search".center(88, "-"))
mob_ = re.compile(r'<.*>')
str = "<html>is the scripting language.>"
print(mob_.search(str).group())

print("ignoreCase".center(88,"-"))
mob_ = re.compile(r'ABCD|small', re.I)
str = "abcd is alphabets SMALL"
print(mob_.findall(str))

print("Substituting the words".center(88, "-"))
mob_ = re.compile(r'Agent', re.I)
str = "agent says he is a fool"
print(mob_.sub("Confidential_Name",str))

print("email matching".center(88, "-"))
mob_ = re.compile(r'''(
    [a-xA-Z0-9._%+-]+
    @+
    [a-zA-Z0-9._%+-]+
    (\.[a-zA-Z]{2,4})+
    )''', re.VERBOSE)
str = "my email is pregaofficial004@gmail.com, trinitypraga123@gmail.com kirubakaran.c@gmail.com"
print(mob_.findall(str))

print("Practice Session".center(88, "-"))
print("21)".ljust(44, '_'),"Pg.no:171".ljust(44, '_'))
mob_ = re.compile(r'[A-Z][a-z]*\sSatoshi')
str = "Praga Satoshi, nakamoto Satoshi, Baddu Satoshi"
arr = mob_.findall(str)
print(arr)
