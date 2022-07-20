import numpy as np
import matplotlib.pyplot as plt
import math


f = open('data.txt', 'r')
d = open('dawlw.txt', 'w')

with f as file:
    w=file.read()

with d as file:
    file.write(w)
print(w)
f.close()
d.close()