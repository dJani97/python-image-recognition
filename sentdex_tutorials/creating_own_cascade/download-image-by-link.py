import urllib.request
import cv2
import numpy as np
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


def find_uglies():
    match = False
    for file_type in ['negative']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


find_uglies()

# store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513')
