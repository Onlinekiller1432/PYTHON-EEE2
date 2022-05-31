# 26) Write a program that reads a list of temperatures from a file called temps.txt, converts those temperatures to Fahrenheit, and writes the results to a file calledftemps.txt.


fp1=open("temps.txt","r")
fp2=open("ftemps.txt","w")
for imp in fp1:
    fh=float(imp)*1.8+32
    fp2.writelines(str(fh)+'\n')
fp1.close()
fp2.close()
