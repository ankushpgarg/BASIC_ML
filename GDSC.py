import matplotlib.pyplot as plt
import numpy as np
import csv

x=[]
y=[]
z=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
explode = (0, 0.1, 0, 0, 0, 0,0, 0.1, 0, 0, 0, 0)

#opening .csv file and creating data by storing values in respective arrays
with open('company_sales_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append((row[0])) #month_number
        y.append(int(row[8])) #total_profit
        z.append(int(row[7])) #total_units
        a.append(int(row[6])) #moisturizer
        b.append(int(row[5])) #shampoo
        c.append(int(row[4])) #bathingsoap
        d.append(int(row[3])) #toothpaste
        e.append(int(row[2])) #	facewash
        f.append(int(row[1])) #	facecream
        
        

#plotting data using line plot graph
plt.plot(x,y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "yearly profit")
  
plt.xticks(rotation = 45)
plt.xlabel('month')
plt.ylabel('profit')
plt.title('yearly profit', fontsize = 20)
plt.grid()
plt.legend()
plt.show()

#plotting data using multiline plot

plt.plot(x, a, label = "moisturizer")
plt.plot(x, b, label = "shampoo")
plt.plot(x, c, label = "bathing soap")
plt.plot(x, d, label = "toothpaste")
plt.plot(x, e, label = "facewash")
plt.plot(x, f, label = "facecream")
plt.legend()
plt.show()


#plotting data using subplots
plt.subplot(8,1,1)
plt.plot(x,y)
plt.title("total_profit")

plt.subplot(8,1,2)
plt.plot(x,z)
plt.title("total_units")

plt.subplot(8,1,3)
plt.plot(x,a)
plt.title("moisturizer")

plt.subplot(8,1,4)
plt.plot(x,b)
plt.title("shampoo")

plt.subplot(8,1,5)
plt.plot(x,c)
plt.title("bathing soap")

plt.subplot(8,1,6)
plt.plot(x,d)
plt.title("toothpaste")

plt.subplot(8,1,7)
plt.plot(x,e)
plt.title("facewash")

plt.subplot(8,1,8)
plt.plot(x,f)
plt.title("facecream")

plt.suptitle("COMPANY SALES DATA")
plt.show()


#plotting data using scatter plots

plt.scatter(x,y, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('MONTHS')
plt.ylabel('TOTAL_PROFIT')
plt.title('COMPANY SALES DATA', fontsize = 20)
  
plt.show()


plt.scatter(x,z, color = 'r',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('MONTHS')
plt.ylabel('TOTAL_UNIT')
plt.title('COMPANY SALES DATA', fontsize = 20)
  
plt.show()




#plotting data using stack plots

#making the label
plt.plot([], [], color ='r', 
         label ='moisturizer')
plt.plot([], [], color ='c',
         label ='shampoo')
plt.plot([], [], color ='b',
         label ='bathing soap')
plt.plot([], [], color ='g', 
         label ='toothpaste')
plt.plot([], [], color ='m',
         label ='facewash')
plt.plot([], [], color ='y',
         label ='facecream')



plt.stackplot(x,a,b,c,d,e,f,
              colors =['r', 'c', 'b', 'g','m','y'], )


plt.xlabel('month')
plt.ylabel('total units sold')
plt.title('total units sold')
plt.legend()
plt.show()


#plotting data using Pie chart

plt.pie(y,labels = x, explode=explode, autopct = '%1.2f%%', shadow=True)
plt.title('TOTAL PROFIT', fontsize = 15)
plt.show()





































