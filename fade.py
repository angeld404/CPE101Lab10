import sys
import math

def calculate_values(height, row, point_row, width, col, column, rad, pixels):
    distance = math.sqrt(((height - row) - point_row)**2 + ((width - col) - column)**2)
    scaler = (rad - distance) / rad
    red = pixels.pop(0)
    green = pixels.pop(0)
    blue = pixels.pop(0) 
    if scaler < .2:
        scaler = .2
    scaled_red = float(red) * scaler
    scaled_green = float(green) * scaler
    scaled_blue = float(blue) * scaler
    return scaled_red, scaled_green, scaled_blue

def write_out(scaled_red, scaled_green, scaled_blue, faded):
    if scaled_red > 225:
        faded.write('225 ')
    else:
        faded.write(str(int(scaled_red)) + ' ')
    if scaled_green > 225:
        faded.write('225 ')
    else:
        faded.write(str(int(scaled_green)) + ' ')
    if scaled_blue > 225:
        faded.write('225 ')
    else:
        faded.write(str(int(scaled_blue)) + ' ')


def main():
    try:
        file = open(sys.argv[1], 'r')
        point_row = int(sys.argv[2])
        column = int(sys.argv[3])
        rad = int(sys.argv[4])
    except IndexError:
        print('Usage: python3 fade.py <image> <row> <column> <radius>')
        exit()
    except ValueError:
        print('Usage: python3 fade.py <image> <row> <column> <radius>')
        exit()
    except FileNotFoundError:
        print('Unable to open {0}'.format(sys.argv[1]))
        exit()

    faded = open('faded.ppm', 'w')

    faded.write(file.readline())

    wxh = (file.readline())
    wxh_list = wxh.split(' ')
    width = int(wxh_list[0])
    height = int(wxh_list[1])
    faded.write(wxh)

    faded.write(file.readline())
    







    pixel_string = file.readline()
    pixel_string.strip()
    pixel_list = pixel_string.split(' ')

    
    
    pixels = []
    for row in range(height):
        for col in range(width):


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




            scaled_red, scaled_green, scaled_blue = calculate_values(height, row, point_row, width, col, column, rad, pixels)
            
            write_out(scaled_red, scaled_green, scaled_blue, faded)

    file.close()
    faded.close()



if __name__ == '__main__':
    main()
