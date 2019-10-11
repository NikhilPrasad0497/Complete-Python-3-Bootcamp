'''files input output'''
'''only works in jupyter notebook
%%writefile myfile.txt
Hello this is a text file
this is 2nd line
this is 3rd line'''

'''myfile= open("C:\\Users\\Dell\\Desktop\\Professional\\Complete-Python-3-Bootcamp\\PythonWorkspace\\Test.txt")
myfile.read()'''

with open("C:\\Users\\Dell\\Desktop\\Professional\\Complete-Python-3-Bootcamp\\PythonWorkspace\\Test.txt", mode='a') as my_newfile:
    contents=my_newfile.write('')
    print(contents)

''' differernt modes
mode='r' read mode only
mode='w' write mode only
mode='a' append mode only
mode='r+' read and write mode
mode='w+' writing and reading (overwrites a new file or create a new file)'''