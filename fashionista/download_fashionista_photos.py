import os
import itertools
import urllib

photo_dir = os.path.join(os.getcwd(), 'photos')
images = [[line.rstrip().split("\t")[1] for line in open(os.path.join(photo_dir, f))] for f in os.listdir(photo_dir) if f.endswith('.txt')]
images = list(itertools.chain.from_iterable(images))

print('Downloading %s images to "./images" directory...' % len(images))

image_dir = os.path.join(os.getcwd(), 'images')
if not os.path.exists(image_dir):
  os.makedirs(image_dir)

for img in images:
  filename = img.split('/')[-1]
  image_filename = os.path.join(image_dir, filename)
  print("Fetching '%s' to '%s'..." % (img, image_filename))
  urllib.urlretrieve(img, image_filename)

