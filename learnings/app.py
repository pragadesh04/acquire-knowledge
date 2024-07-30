import pyperclip as pc
import webbrowser as wb
import time as t
print(str)
print("The ultimate bing search bot".center(50, '='))
n = int(input("Enter how many searches: "))
i = 0
while(i <= n):
    str = pc.paste()
    url = "https://www.bing.com/search?pglt=163&q={}".format(str)
    wb.open(url)
    t.sleep(6)
    i+=1