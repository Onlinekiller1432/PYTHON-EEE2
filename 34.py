data=input("Enter the data you want to store in a file:")
try:
     with open('exampl.txt', 'w') as f:
         (f.write(data))
         f.close()
     print("data in the file is:")
     with open('exampl.txt','r') as f:
          print(f.read())
          f.close()
except IOError as e:
     print("open read error",e)
finally:
    print("\n\n\n Your data is successfully stored in a file")
