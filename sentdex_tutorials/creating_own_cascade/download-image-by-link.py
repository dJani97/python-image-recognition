import urllib.request
import cv2
import numpy
import os


def store_raw_images(negative_images_link):
    negative_image_urls = urllib.request.urlopen(negative_images_link).read().decode()

    if not os.path.exists('negative'):
        os.makedirs('negative')

    pic_num = 60000
    for i in negative_image_urls.split('\n'):
        try:
            print(str(i))
            file_name = 'negative/' + str(pic_num) + '.jpg'
            urllib.request.urlretrieve(i, file_name)
            img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (100, 100))
            cv2.imwrite(file_name, img)
            pic_num += 1

        except Exception as e:
            print(str(e))



# store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513')

store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n12992868')