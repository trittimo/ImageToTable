from PIL import Image
import sys
import os

def convert(image, outpath):
    with open(outpath, "w") as outfile:
        outfile.write("<table name=\"image\">")

        pixels = image.getdata()
        width = image.width
        index = 1
        needswrite = True
        for color in pixels:
            if needswrite:
                outfile.write("<tr style=\"height: 10px; width: 10px;\">")
                needswrite = False
            outfile.write("<td style=\"height: 10px; width: 10px; background-color: #%02x%02x%02x;\"></td>" % (color[0], color[1], color[2]))
            if index % width == 0:
                outfile.write("</tr>")
                needswrite = True
            index += 1
        outfile.write("</table>")


if __name__ == '__main__':
    for infile in sys.argv[1:]:
        file, extension = os.path.splitext(infile)
        outfile = file + ".html"
        if infile != outfile:
            try:
                convert(Image.open(infile), outfile)
            except IOError:
                print("Unable to open image: " + infile)