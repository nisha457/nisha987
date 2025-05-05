row=int(input("Enter No of Rows for 1st Matrix:"))
column=int(input("Enter No of column for 1nd Matrix:"))
row1=int(input("Enter No of Rows for 2st Matrix:"))
column1=int(input("Enter No of column for 2nd Matrix:"))
X = [[int(input(("Enter value for X[",i,"][",j,"]:")))
for j in range(column)] for i in range(row)]
Y = [[int(input(("Enter value for Y[",i,"][",j,"]:")))
for j in range(column1)] for i in range(row1)]
print("1st Matrix X:",X)
print("2st Matrix Y:",Y)
