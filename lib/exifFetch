from PIL import Image
from PIL.ExifTags import TAGS
import optparse


def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    try:
        img = Image.open(fname)
        if hasattr(img, '_getexif'):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    if str(decoded) == "MakerNote" or str(decoded) == "UserComment":
                        continue
                    print(str(decoded)+":"+str(value))
    except IOError:
        print('IOERROR ' + fname)


def main():
    parser = optparse.OptionParser('usage:  exifFetch.py -F <target file> ')
    parser.add_option('-F', dest='filename', type='string', help='specify target File')
    (options, args) = parser.parse_args()
    fileName = options.filename
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        get_exif_data(fileName)
        exit(1)


if __name__ == '__main__':
    main()

