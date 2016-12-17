import os
import subprocess
import argparse

office_exes = ["/Applications/LibreOffice.app/Contents/MacOS/soffice", "/WIN"]


def main():
    parser = argparse.ArgumentParser(prog='to_pdf', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--bin',   '-b', help="Libre Office binary")
    parser.add_argument('--files', '-f', default="*.odp", help="the files to convert")
    args = parser.parse_args()

    bin = args.bin
    if bin is None:
        for e in office_exes:
            exists = os.path.exists(e)
            if exists:
                bin = e
                break
    if bin:
        cmd = "{} --headless --convert-to pdf {}".format(bin, args.files)
        print cmd
        process = subprocess.call(cmd, shell=True)
    else:
        print "couldn't find a Libre Office binary to convert files to pdf"


if __name__ == '__main__':
    main()
