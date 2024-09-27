import pyautogui as pg
import time as t

t.sleep(5)

content = """import math
def distance(x1, y1, x2, y2):
return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def polygon_perimeter(vertices):
n = len(vertices)
perimeter = 0.0
for i in range(n):
next_i = (i + 1) % n
perimeter += distance(vertices[i][0], vertices[i][1], vertices[next_i][0], vertices[next_i][1])
return perimeter
n, start_x, start_y = map(int, input().split())
vertices = [tuple(map(int, input().split())) for _ in range(n)]
perimeter = polygon_perimeter(vertices)
print(f"{perimeter:.2f}")
"""

pg.typewrite(content, interval=0.01)