import os, os.path, sys
import linecache, re 
 

class Fileanalyzer:
    def __init__(self):

        try:
            self.dir = sys.argv[1]
        except:
            print("Folder is not defined - exiting")
            exit()
        self.files={}
        count=0
    def setFolder(self):
        try:
            directory = str(sys.argv[1])
            self.dir=directory
        except:
            print("Folder is not defined - exiting")
            exit()

    def getExtension(self,file):
        extension = os.path.splitext(file)[1][1:]
        return extension

    def getlastline(self,file):
        file=os.path.abspath(file)
        last_line="No text file"
        if self.getExtension(file) == "txt":
            try:
                fileHandle = open ( file,"r" )
                lineList = fileHandle.readlines()
                fileHandle.close()
                last_line=lineList[len(lineList)-1]
            except:
                last_line="File cannot be open"
                return last_line
           
        return last_line

    def list_files(self):
        files = {}
        self.count=0
        for r, d, f in os.walk(self.dir):
            for file in f:
                self.count += 1
                lastline = self.getlastline(os.path.relpath(file))
                extension = self.getExtension(file)
                files[file] = {'id': self.count,'type': extension, 'last_line':lastline} 
        self.files=files
        return files

    def count_file_types(self):
        type_list={}

        for file,attributes in self.files.items():
            for keys in attributes: 
               type_list[self.files[file]['type']] = 0
        for file,attributes in self.files.items(): 
               type_list[self.files[file]['type']] = (type_list[self.files[file]['type']] + 1)
        print("================================")
        print("File types count:")
        print(type_list)

    def print_into_file(self):
        output_file = open(self.dir +'\\output.txt', 'w') 
        print(analysis.list_files(), file = output_file) 
        output_file.close() 
        print("Output file created in analysed directory:"+ self.dir +"\\output.txt")

analysis = Fileanalyzer()
print(analysis.list_files())
print("================================")
print("Directory analysed: " + analysis.dir)
print("Over all count of files is " + str(analysis.count))
analysis.count_file_types()
analysis.print_into_file()
analysis.setFolder()


