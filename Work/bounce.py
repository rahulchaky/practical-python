# bounce.py
#
# Exercise 1.5
'''
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell.
Write a program bounce.py that prints a table showing the height of the first 10 bounces.

Note: You can clean up the output a bit if you use the round() function. Try using it to round the output to 4 digits.
Your program should make a table that looks something like this:

1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
'''
h = 100
for i in range(1, 11):
    h *= 0.6
    print(f"{i} {round(h, 4)}")
