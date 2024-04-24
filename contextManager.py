#contex Manzager
#2 types -> Using Class, Using Function
#use anyone of it at at a time 


# USING CLASS
class file_open():
    def __init__(self,fname,mode):
        self.fname = fname
        self.mode = mode
    def __enter__(self):
        self.file = open(self.fname,self.mode)
        return self.file
    def __exit__(self,exec_type,exec_val,traceback):
        self.file.close()
        

with file_open("abc.txt","w") as file1:
    file1.write("hello")
    
print(file1.closed)    

##Using Function
# from contextlib import contextmanager

# @contextmanager
# def openfile(filename,mode):
#     file = open(filename,mode)
#     yield file
#     file.close()
    
# with openfile("abc.txt","w") as file1:
#     file1.write("hello")
    

# print(file1.closed)  
