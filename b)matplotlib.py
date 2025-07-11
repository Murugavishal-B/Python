import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
plt.plot(x, y, label='y = x^2')
plt.title('Annotated Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.annotate('Important Point', xy=(2, 4), xytext=(3, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(1, 20, 'Text Box Example', fontsize=12, color='red')
plt.grid(True)
plt.show()
