import sys
from groups import *

def write_out(red, outfile):
    if red >= 225:
        outfile.write('{0}\n'.format(str(225)))
        outfile.write('{0}\n'.format(str(225)))
        outfile.write('{0}\n'.format(str(225)))
    else:
        outfile.write('{0}\n'.format(str(red)))
        outfile.write('{0}\n'.format(str(red)))
        outfile.write('{0}\n'.format(str(red)))




def main():
    try:
        file = open(sys.argv[1], 'r')
    except IndexError:
        print('Usage: python3 decode.py <image>')
        exit()
    except FileNotFoundError:
        print('Unable to open {0}'.format(sys.argv[1]))
        exit()
    except PermissionError:
        print('Unable to open {0}'.format(sys.argv[1]))
        exit()

    outfile = open('outfile.ppm', 'w')
    outfile.write(file.readline())

    wxh = file.readline()
    wxh_list = wxh.split(' ')
    outfile.write(wxh)
    width = int(wxh_list[0])
    height = int(wxh_list[1])

    outfile.write(file.readline())
    pixel_string = file.readline()
    pixel_list = pixel_string.split(' ')

    for count in range(((width) * (height))):
        

        #pixels = groups_of_3(pixel_list)
        pixels = []

        while len(pixels) < 3:
            if len(pixel_list) == 0:
                pixel_string = file.readline()
                pixel_string.strip()
                pixel_list = pixel_string.split(' ')
            elif len(pixel_list) == 1 and pixel_list[0] == '':
                pixel_string = file.readline()
                pixel_string.strip()
                pixel_list = pixel_string.split(' ')
            else:
                pixels.append(pixel_list.pop(0))

        

        red = int(pixels[0]) * 10
        write_out(red, outfile)

    file.close()
    outfile.close()



if __name__ == '__main__':
    main()
