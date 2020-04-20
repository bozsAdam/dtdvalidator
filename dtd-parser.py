try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
from lxml import etree
import sys, getopt

def main(argv):
    xml_file = ''
    dtd_file = ''
    try:
        opts, args = getopt.getopt(argv, "x:d:", ["xmlfile=", "dtdfile="])
    except getopt.GetoptError:
        print('test.py -x <xmlfile> -d <dtdfile>')
        print("--------------OR-----------------")
        print('test.py -x <xmlfile> -d <dtdfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -x <xmlfile> -d <dtdfile>')
            print("--------------OR-----------------")
            print('test.py --xmlfile <xmlfile> --dtdfile <dtdfile>')
            sys.exit()
        elif opt in ("-x", "--xmlfile"):
            xml_file = arg
        elif opt in ("-d", "--dtdfile"):
            dtd_file = arg

    with open(dtd_file) as file:
        dtd_from_file = file.read()

    with open(xml_file) as file:
        xml_from_file = file.read()

    dtd = etree.DTD(StringIO(dtd_from_file))
    isValid = dtd.validate(etree.XML(xml_from_file))

    if(not isValid):
        with open("not_valid.txt") as file:
            not_valid_art = file.read();

        print("-------------------------------")
        print(not_valid_art)
        print("cause:")
        print(dtd.error_log.filter_from_errors()[0])
        print("-------------------------------")
    else:
        with open("valid.txt") as file:
            print(file.read())


if __name__ == "__main__":
    main(sys.argv[1:])
