from PIL import Image, ImageDraw, ImageFont
import sys

print("use python 3 if you have multiple versions. PIL should be installed.")
if sys.argv[1] == '--h' or sys.argv[1] == 'help' or len(sys.argv) != 4:
    print("Use following format, where fullname is separated by _ rather than a space:\npython stamp_info.py img_file fullname contact\nie:\npython stamp_info mert.jpg Mert_Imre M.imre@tudelft.nl\nNote that fullname is split by _")

else:
    img_name = sys.argv[1]
    name = sys.argv[2]
    contact = sys.argv[3]

    img = Image.open(img_name)
    firstline_text = name.replace('_', ' ')
    secondline_text = contact

    width, height = img.size

    I1 = ImageDraw.Draw(img, 'RGBA')
    base_height = (11/16) * height
    margin = 5

    title_font = ImageFont.truetype('./fonts/US101.TTF', 20)
    width_first, height_first = I1.textsize(firstline_text, font=title_font)

    width_second, height_second = I1.textsize(secondline_text, font=title_font)

    I1.rectangle((0, base_height, width, base_height+height_first+height_second+margin), fill=(0, 0, 0, 127))

    I1.text(((width-width_first)/2, base_height), firstline_text, font=title_font, fill =(255, 255, 255))
    I1.text(((width-width_second)/2, base_height+height_first), secondline_text, font=title_font, fill =(255, 255, 255))

    img.save(img_name[:-4] + "_stamped.png")
