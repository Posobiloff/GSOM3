for i in range(10):
    i *= 2
    print(i)
import matplotlib.pyplot as plt
xpoints = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
ypoints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(xpoints, ypoints)

def complexity_3(n):
    fff = 2
    for i in range(n):
        for j in range(n):
            for k in range(n):
                fff *= 2
                print(fff)