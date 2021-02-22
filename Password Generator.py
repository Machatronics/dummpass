import random

class Generator:
    def __init__(self,name,password):
        self.name = name 
        self.password = password
        
        
    def choice(self,xyz):
        print(int(xyz))    
        if(int(xyz) == 100):
            return "Letter"
        elif(int(xyz) == 110):
            return "Letter,Number"
        elif(int(xyz) == 111):
            return "Letter,Number,Special_Char"
        elif(int(xyz) == 101):
            return "Letter,Special_Char"
     
    def generate(self,request):

        stage = random.randint(7,11)
        pword = []
        current = 0
        if(request == "Letter" ):
            chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w"]
        elif(request == "Letter,Number" ):
            chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w","0","1","2","3","4","5","6","7","8","9"]
        elif(request == "Letter,Number,Special_Char"):
            chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w",",",".","!","+","%","/","0","1","2","3","4","5","6","7","8","9"]
        elif(request == "Letter,Special_Char"):
            chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w",",",".","!","+","%","/"]

        while(current <= stage):
            pword.append(random.choice(chars))
            print(pword)
            
            current += 1
        return pword       
abc = input()
i1 = Generator('Berkay',abc)
print(*i1.generate(i1.choice(abc)))
        
    