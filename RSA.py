print("RSA")
print("************************************************************************")

p=89
q=829
n=p*q
f_n=(p-1)*(q-1)
e=19
e_i=e
#**********************Algoritmo extendido de Euclides*******************************
a_i=e
b_i=f_n
q_lista=[]
x=[1,0]
y=[0,1]
i=0

q=e//f_n
q_lista.append(q)
r=e%f_n

while(r!=0):
  e=f_n
  f_n=r
  q=e//f_n
  q_lista.append(q)
  r=e%f_n
  i=i+1

for p in range (i):
  e=x[p]-(q_lista[p]*x[p+1])
  x.append(e)
  f_n=y[p]-(q_lista[p]*y[p+1])
  y.append(f_n)


d=x.pop()
#*****************************************************************************************************

dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'ñ':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27}
valores=list(dic.values())
claves=list(dic.keys())

frase=input("Ingrese la frase que desea encriptar: ")
frase=frase.lower()

print(frase)
listica= list(frase)

for i in range (len(listica)):
    if listica[i] in dic:
        listica[i]=dic[listica[i]]

for i in range (len(listica)):
  if isinstance(listica[i],int):
    listica[i]=(listica[i]**e_i)%n


print(*listica, sep=" ")

print("Desea desencriptar la frase(si o no): ")
op=input()

if op=="si":
  for i in range(len(listica)):
    if isinstance(listica[i],int):
      listica[i]=(listica[i]**d)%n
  
  for i in range(len(listica)):
    if listica[i] in valores:
      listica[i]=claves[listica[i]-1]
  
  print(print)
  
else:
  print("Fin del programa  :)")
  
