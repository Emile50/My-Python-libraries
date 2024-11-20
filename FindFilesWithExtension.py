def findFilesWithExtension(path, extension = ".txt"):
    
    filesFound = [] #Contains paths to text files found. This is passed by reference to the recursive function
    
    recursiveFileDepthSearch(path, filesFound, 0, extension)
    
    return filesFound


        
def recursiveFileDepthSearch(path, FilesFoundList, depth, extension):
    print("--------------------------------")
    print("Files in:" + path)
    print("--------")
    
    for fileName in os.listdir(path):
        print("file name: " + fileName)
        
        filePath = os.path.join(path, fileName)#better than doing string concatenation, becaue the slash character also causes python to ignore the next character, so you have to double it, and then that might cause compatibility and readability issues
        print()
        
        if os.path.isdir(filePath): #Case 1: file is a directory. Recursive depth search
            recursiveFileDepthSearch(filePath, FilesFoundList, depth+1, extension)
            
        elif (fileName.endswith(extension)): #Case 2 : file is a potential password text file
            #add it to some list we return
             FilesFoundList.append(filePath)

             "we could process text files here, but for code cohesion we don't"
            
        else: #Case 3: file is not a dir or a text file. We do nothing
            pass
