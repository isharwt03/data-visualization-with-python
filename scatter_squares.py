import matplotlib.pyplot as plt
x_values = range(1,1001)
y_values =[x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax=plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.RdBu,s=10)                 
#set chart title and labels them .
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square of value",fontsize=14)
#set the range for each axis 
ax.axis([0,1100,0,1100000])
#set the sise of the tick labels.
ax.tick_params(axis='both',which='major', labelsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight')