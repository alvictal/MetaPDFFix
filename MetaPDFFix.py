import sys
import getopt
import fitz 
from os import path,walk,mkdir


def createDirIfNotExist(dirname):
    if path.isdir(dirname) == False:
        try:
            mkdir(dirname)
        except OSError:
            print ("Creation of the directory %s failed" % dirname)
            return False
    return True



def organizeMergedFiles(pdf, output_dir, filename):

    if (createDirIfNotExist(output_dir) == False):
        return

    pdf.save(path.join(output_dir,filename))    
    return


def mergeSignToPDFFiles(file_list=[], output_dir=None):    
    if output_dir == None:
        output_dir = "saved_new_files"

    for file_path, filename in file_list:
        pdf_handle = fitz.open(file_path)

        organizeMergedFiles(pdf_handle, output_dir, filename)
        
    return


def printHelp():
    print ("MetaPDFFix - is a simple tool to correct wrong pdf metadata that make some pdfreaders not open the a file")
    print ("--input-dir= : Directory containing the pdfs tha should be fixed")
    print ("--outut-dir= : Directory where the fixed pdfs will be save. If none was passed the app will create a new directory called saved_new_files inside thsi directory")
    print ("Example of usage: python MetaPDFFix.py --input-dir=<your_directory_here>")
    return



def getFilesInfo(mypath):
    f = []
    for (root, dirs, files) in walk(mypath):
        for filename in files:
            if ".pdf" in filename:
                f.append([path.join(root,filename), filename])
                
        
    return f



def main():
    maindir = None 
    outputdir = None
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"io:h",["help", "input-dir=","output-dir="])
    except getopt.GetoptError as e:
        print (str(e))
        sys.exit(2)

    print (myopts)
    for option,argument in myopts:
        if option in ("-h", "--help"):
            printHelp()
            sys.exit()
    
        elif option in ("-i","--input-dir"):
            maindir = argument

        elif option in ("-o", "--output-dir"):
            outputdir = argument
    

        else:
            printHelp()
            sys.exit()

    
    recl = getFilesInfo(maindir)
    mergeSignToPDFFiles(recl, outputdir)


if __name__ == "__main__":
    main()