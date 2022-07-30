import os

def listingAllFile(path):
    
    if os.path.exists(path):
        
        lista = os.listdir(path)
    
        for elem in lista:
            string = path+""+elem+""
            if os.path.isfile(string):
                print(elem)
            else:
                string2 = path+""+elem+"/"
                listingAllFile(string2)
                
    else:
        print("This path doesn't exist")
        
listingAllFile("/home/gianluca/Desktop/University/2°anno/SO/")