from StringIO import StringIO

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

    print("dtd : " + dtd_file)
    print("xml : " + xml_file)

    with open(dtd_file) as file:
        dtd_from_file = file.read()

    print("------------------------------------")
    print(dtd_from_file)
    print("------------------------------------")

    with open(xml_file) as file:
        xml_from_file = file.read()

    dtd = etree.DTD(StringIO(dtd_from_file))
    isValid = dtd.validate(etree.XML(xml_from_file))

    print(isValid)


if __name__ == "__main__":
    main(sys.argv[1:])