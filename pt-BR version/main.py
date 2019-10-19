import random,sys,string

N = int(sys.argv[1])#numero de caracteres da senha
A = sys.argv[2]#alfabeto (y/n)
S = sys.argv[3]#caracteres especiais (y/n)
n = sys.argv[4]#numeros (y/n)
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
    total=list**N#permutações da repeticao N**r
    password=password*N
    print(total)
    b.write("\nGerando lista de senhas :-"+str(total)+"\n");
    final=set([]);#para armazenar uma lista de senhas
    j=0;
    print("processando...\n");
    while len(final)!=total:
    #a.write(random.sample(password,N)+"\n");

        final.add("".join(random.sample(password,N)))
    print(len(final))
    for i in final:
        a.write(i+"\n");
    b.write("\n\n\nSenha gerada... aproveite... Obrigado por usar os serviços do RoboMex!!!");
    a.close()
    b.close()
generate()
