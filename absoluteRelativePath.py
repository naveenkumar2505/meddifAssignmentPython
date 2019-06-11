class Path:
    def __init__(self, Original_path):
        self.current_path = Original_path

    def cd(self, new_path):
        i=0
        new_path=new_path.split('/')
        pathLength=len(new_path)
        path=self.current_path.split('/')

        if new_path[0]==' ':

            del path[:]
            path.append('/'+new_path[1])
            i=i+2

        while(i<pathLength):
            j=len(path)-1
            if new_path[i]=='..':

                path.pop(j)
            else:
                path.append(new_path[i])
            i=i+1
        self.current_path="/".join(path)
in_path=input("enter the path: ")
in_path=in_path.split('/')
in_path=''.join(in_path)
if in_path.isalpha():
    in_path='/'.join(in_path)
    path = Path(in_path)
    path.cd('../x')
    print(path.current_path)
else:
    print('Please Provide the alaphabets....or provide the correct formate')
