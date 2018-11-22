
# Projector input order

from PIL import Image
import math

test_image_list = '/Users/sal/projects/BalchLab/GenerativeVSP/2018-09-04/VSP_emb_548g_spritelist.tsv' # path to the image list
with open(test_image_list, 'r') as f:
    test_images = f.readlines()
    test_images = map(str.strip, test_images)

grid = int(math.sqrt(len(test_images))) + 1
image_height = 60 #int(8192 / grid)         # tensorboard supports sprite images up to 8192 x 8192
image_width = 70 #int(8192 / grid)

big_image = Image.new(
    mode='RGBA',
    size=(image_width * grid, image_height * grid),
    color=(0,0,0,0))  # fully transparent

for i in range(len(test_images)):
    row = i / grid
    col = i % grid
    img = Image.open(test_images[i])
#   img = img.resize((image_height, image_width), Image.ANTIALIAS)
    row_loc = row * image_height
    col_loc = col * image_width
    big_image.paste(img, (col_loc, row_loc)) # NOTE: the order is reverse due to PIL saving
    print(row_loc, col_loc)

big_image.save('sprite_image_551g.png')#, transparency=0)



# alphabetical order


test_image_list = '/Users/sal/projects/BalchLab/GenerativeVSP/2018-09-04/VSP_emb_548g_spritelist_alphabetic.tsv' # path to the image list
with open(test_image_list, 'r') as f:
    test_images = f.readlines()
    test_images = map(str.strip, test_images)

grid = int(math.sqrt(len(test_images))) + 1
image_height = 60 #int(8192 / grid)         # tensorboard supports sprite images up to 8192 x 8192
image_width = 70 #int(8192 / grid)

big_image = Image.new(
    mode='RGBA',
    size=(image_width * grid, image_height * grid),
    color=(0,0,0,0))  # fully transparent

for i in range(len(test_images)):
    row = i / grid
    col = i % grid
    img = Image.open(test_images[i])
#   img = img.resize((image_height, image_width), Image.ANTIALIAS)
    row_loc = row * image_height
    col_loc = col * image_width
    big_image.paste(img, (col_loc, row_loc)) # NOTE: the order is reverse due to PIL saving
    print(row_loc, col_loc)

big_image.save('sprite_image_alphabetical.png')#, transparency=0)




#img = Image.open(test_images[1])