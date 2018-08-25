from PyPDF2 import PdfFileReader
import optparse


def PrintMeta(filename):
    pdfFile = PdfFileReader(filename)
    docInfo = pdfFile.getDocumentInfo()
    print("File: "+filename)
    for metaItem in docInfo:
        try:
            print("[+] "+metaItem+":"+str(docInfo[metaItem]))

        except:
            pass

def main():
    parser = optparse.OptionParser('usage:  PdfScan.py -H <target host> ')
    parser.add_option('-F', dest='filename', type='string', help='specify target File')
    (options, args) = parser.parse_args()
    fileName = options.filename
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        PrintMeta(fileName)
        exit(1)


if __name__ == '__main__':
    main()