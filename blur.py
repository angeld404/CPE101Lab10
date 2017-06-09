import sys
import math

def pix_rows(pixels, width, height):
    pixel_list = []
    for num in range(height):
        pixel_list.append(pixels[width * num: width * (num + 1)])
    return pixel_list


def pix_cols(pix_rows, width):
    pixel_list = []
    for num in range(len(pix_rows[0])):
        pix = []
        for idx in range(len(pix_rows)):
            pix.append(pix_rows[idx][num])
        pixel_list.append(pix)
    return pixel_list
    
def cols_to_rows(pixels):
    pixel_list = []
    for num in range(len(pixels[0])):
        pix = []
        for idx in range(len(pixels)):
            pix.append(pixels[idx][num])
        pixel_list.append(pix)
    return pixel_list



def main():
    try:
        file = open(sys.argv[1], 'r')
        blur_factor = int(sys.argv[2])
    except IndexError:
        blur_factor = 4
    except ValueError:
        print('Usage: python3 blur.py <image> [<reach>]')
        exit()
    except FileNotFoundError:
        print('Unable to open {0}'.format(sys.argv[1]))
        exit()

    blurred = open('blurred.ppm', 'w')

    blurred.write(file.readline())

    wxh = (file.readline())
    wxh_list = wxh.split(' ')
    width = int(wxh_list[0])
    height = int(wxh_list[1])
    blurred.write(wxh)

    blurred.write(file.readline())
    

    pixel_string = file.readline()
    pixel_string.strip()
    pixel_list = pixel_string.split(' ')

    
#GROUP PIXELS
#=============================================================

    pixels = []
    for row in range(height):
        for col in range(width):
            pixel = []

            while len(pixel) < 3:
                if len(pixel_list) == 0:
                    pixel_string = file.readline()
                    pixel_string.strip()
                    pixel_list = pixel_string.split(' ')
                elif len(pixel_list) == 1 and pixel_list[0] == '':
                    Pixel_string = file.readline()
                    pixel_string.strip()
                    pixel_list = pixel_string.split(' ')
                else:
                    pixel.append(pixel_list.pop(0))


            #distance = math.sqrt(((height - row) - point_row)**2 + ((width - col) - column)**2)
            #scaler = (rad - distance) / rad
            red = int(pixel.pop(0))
            green = int(pixel.pop(0))
            blue = int(pixel.pop(0))
            #if scaler < .2:
            #    scaler = .2
            #scaled_red = float(red) * scaler
            #scaled_green = float(green) * scaler
            #scaled_blue = float(blue) * scaler
            pixel = [red, green, blue]
            pixels.append(pixel)
 


    pixel_rows = pix_rows(pixels, width, height)
    max_pixels = ((blur_factor * 2) + 1) ** 2
    for row in range(height):
        print(row)
        for col in range(width):
            in_range = []

#REMOVE UNEEDED ROWS
#===============================================================

            for idx in range(len(pixel_rows[:row + blur_factor])):
                if abs(row - idx) <= blur_factor:
                    in_range.append(pixel_rows[idx])

            pixel_cols = pix_cols(in_range, width)
            in_range1 = []

#REMOVE UNEEDED COLUMNS
#================================================================

            for idx in range(len(pixel_cols)):
                if abs(col - idx) <= blur_factor:
                    in_range1.append(pixel_cols[idx])

            pixel_rows1 = cols_to_rows(in_range1) 

#LIST OF TOTAL VALUES PER COLOR
#=================================================================

            total_val = [0, 0, 0]
            for item in range(len(pixel_rows1)):
                for pixel in range(len(pixel_rows1[0])):
                    total_val[0] += pixel_rows1[item][pixel][0]
                    total_val[1] += pixel_rows1[item][pixel][1]
                    total_val[2] += pixel_rows1[item][pixel][2]
#CALCULATE AVG VALUES
#=================================================================
            avg_val = [0, 0, 0]
            for idx in range(3):
                avg_val[idx] = total_val[idx] / max_pixels

#WRITE TO BLURRED
#=================================================================

            for item in avg_val:
                blurred.write(str(int(item)) + ' ')




    file.close()
    blurred.close()



if __name__ == '__main__':
    main()
