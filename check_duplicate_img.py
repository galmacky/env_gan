from PIL import Image, ImageChops
import os
import argparse

# From http://effbot.org/zone/pil-comparing-images.htm
def is_duplicate(img1, img2):
  return ImageChops.difference(img1, img2).getbbox() is None

if __name__ == "__main__":
  print('Starting duplicate checking...')
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-d1', '--directory_1', default='d1', type=str, help='first directory')
  parser.add_argument('-d2', '--directory_2', default='d2', type=str, help='second directory')
  args = parser.parse_args()
  dir1 = args.directory_1
  dir2 = args.directory_2

  with_duplicates = []
  with_no_duplicates = []
  for img_filename_1 in os.listdir(dir1):
    duplicates = []
    img1 = Image.open(os.path.join(dir1, img_filename_1))

    for img_filename_2 in os.listdir(dir2):
      if 'png' not in img_filename_2 and 'jpg' not in img_filename_2 and 'jpeg' not in img_filename_2:
        continue

      img2 = Image.open(os.path.join(dir2, img_filename_2))
      if is_duplicate(img1, img2):
        duplicates.append(os.path.join(dir2, img_filename_2))
    
    if len(duplicates) == 0:
      print('No duplicates for', img_filename_1)
      with_no_duplicates.append(img_filename_1)
    else:
      print('Duplicates of', img_filename_1, ':', duplicates)
      with_duplicates.append(img_filename_1)

  print('Images with  duplicates:', with_duplicates)
  print('Images with no duplicates:', with_no_duplicates)
