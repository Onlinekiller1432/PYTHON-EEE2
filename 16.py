#Write a program that asks the user to enter a length in feet. The program should
#then give the user the option to convert from feet into inches, yards, miles,
#millimeters, centimeters, meters, or kilometers.



print("""1-inches
         2-yards
         3-miles
         4-millimeters
         5-centimeters
         6-meters
         7-kilometers""")
ch=int(input("enter choice"))
feet=int(input("enter length in feet"))
inch=feet*12
yards=feet*0.333
miles=feet*0.000189
mm=feet*304.8
cm=feet*30.48
m=feet*0.3048
km=feet*0.0003048
res=[feet,inch,yards,miles,mm,cm,m,km]
print(res[ch])
