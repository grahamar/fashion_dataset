import os
import itertools
import urllib
from joblib import Parallel, delayed

def download(img):
  # filename is (post_id)_(image_name)
  filename = img[0]+'_'+img[1].split('/')[-1]
  image_filename = os.path.join(image_dir, filename)
  print("Fetching '%s' to '%s'..." % (img, image_filename))
  urllib.urlretrieve(img[1], image_filename)

photo_dir = os.path.join(os.getcwd(), 'photos')
images = [[(line.rstrip().split("\t")[0], line.rstrip().split("\t")[1]) for line in open(os.path.join(photo_dir, f))] for f in os.listdir(photo_dir) if f.endswith('.txt')]
images = list(itertools.chain.from_iterable(images))

print('Downloading %s images to "./images" directory...' % len(images))

image_dir = os.path.join(os.getcwd(), 'images')
if not os.path.exists(image_dir):
  os.makedirs(image_dir)

# Download in parallel
Parallel(n_jobs=8)(delayed(download)(img) for img in images)
