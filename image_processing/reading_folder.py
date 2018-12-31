## German traffic signs from the web
import glob
image_names = glob.glob("./validate_images/*.ppm")
test_imgs = []
cropped_test_imgs = []
shapes = []
f, axes = plt.subplots(2, 5)
count = 0

for name in image_names:
    test_img=mpimg.imread(name)
    shape = test_img.shape
    croped_img = test_img[10:40, 10:40]
    shapes.append(test_img.shape)
    test_imgs.append(test_img)
    axes[0,count].set_title(count+1)
    axes[0,count].imshow(croped_img)
#     axes[1,count].set_title(count+1)
#     axes[1,count].imshow(croped_img)
    count = count + 1
print('image shape:', shapes)
# test_img1=mpimg.imread('./validate_images/00004.ppm')
# plt.figure(figsize=(1,1))
# plt.imshow(img)
# print(img.shape)
# # plt.figure(figsize=(1,1))
# # test_image = np.reshape(test_image,[32,32])
# # plt.imshow(test_image, cmap='gray')
