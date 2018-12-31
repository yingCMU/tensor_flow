import glob
from PIL import Image
image_names = glob.glob("./validate_images/*.ppm")
test_imgs = []
cropped_test_imgs = []
shapes = []
f, axes = plt.subplots(2, 5)
count = 0

for name in image_names:

    test_img = Image.open(name)

    test_img.thumbnail((32, 32), Image.ANTIALIAS)

    test_imgs.append(test_img)
    axes[count].set_title(count+1)
    axes[count].imshow(test_img)

    count = count + 1
print('image shape:', shapes)
