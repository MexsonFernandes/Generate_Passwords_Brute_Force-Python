import sys
filename= input("Enter file name (wordlist3.txt) : - ");
try:
    r =open(filename,"r");
except:
    print("Error opening file..Program exiting!!!");
    sys.exit()
print("Word List that can be generated is : - " + str(int(filename[8:9])*2));
w = open("wordlist"+str(int(filename[8:9])*2)+".txt","w");

count=0;
print("Processing...");
i=0;
for lineRead in r:#take first line
    for lineWrite in r:#iterate through whole list
        if count == 0:
            w = open("wordlist"+str(int(filename[8:9])*2)+".txt","a");
        w.write(str(lineRead.rstrip())+str(lineWrite));#rstrip() to remove  \n
        i+=1;
        count+=1;
        if count == 1000:#buffer to file
            w.close();
            count =0;
        
print("Number of combination generated is "+ str(i));
