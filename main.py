import random,sys,string

N = int(sys.argv[1])#number of password character
A = sys.argv[2]#alphabets (y/n)
S = sys.argv[3]#special characters (y/n)
n = sys.argv[4]#numbers (y/n)
def generate():
    a= open("wordlist"+str(N)+".txt",'w')
    b= open("log"+str(N)+".txt",'w')
    list=0;
    password=''
    if A=='y':
        list=list+52;
        password=password+string.ascii_letters
    if S=='y':
        list=list+32;
        password=password+string.punctuation
    if n=='y':
        list=list+10;
        password=password+string.digits
    total=list**N#permutation for repetition N**r
    password=password*N
    print(total)
    b.write("\nGenerating password list :-"+str(total)+"\n");
    final=set([]);#to store password list
    j=0;
    print("processing...\n");
    while len(final)!=total:
    #a.write(random.sample(password,N)+"\n");
        
        final.add("".join(random.sample(password,N)))
    print(len(final))
    for i in final:
        a.write(i+"\n");	
    b.write("\n\n\nPassword generated....enjoy..Thank you for using RoboMex Service!!!");           
    a.close()
    b.close()
generate()
