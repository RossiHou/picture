import matplotlib.pyplot as plt
x_value = [1,2,3,4,5]
y_value = [1,4,9,12,25]
plt.plot(x_value,y_value,linewidth=5)
plt.title("squres number", fontsize=24)
plt.xlabel("value", fontsize = 24)
plt.ylabel("squre of value", fontsize= 24)
plt.tick_params(axis='both', labelsize=14)
plt.show()
