import cv2
import sys
import os
import shutil


def create_path(dirname):
  if not os.path.exists(dirname):
    os.makedirs(dirname)


if __name__ == "__main__":
  print('Starting img processing...')
  input_dir = sys.argv[1]

  highres_dir = os.path.join(input_dir, 'highres')
  midres_dir = os.path.join(input_dir, 'midres')
  lowres_dir = os.path.join(input_dir, 'lowres')

  create_path(highres_dir)
  create_path(midres_dir)
  create_path(lowres_dir)

  high_res = []
  mid_res = []
  low_res = []

  for input_filename in os.listdir(input_dir):
    # Ignore directories
    if not os.path.isfile(os.path.join(input_dir, input_filename)):
      continue

    img = cv2.imread(os.path.join(input_dir, input_filename))
    if img.shape[0] >= 512 and img.shape[1] >= 512:
      high_res.append(input_filename)
      shutil.move(os.path.join(input_dir, input_filename),
                  os.path.join(highres_dir, input_filename))
    elif img.shape[0] >= 256 and img.shape[1] >= 256:
      mid_res.append(input_filename)
      shutil.move(os.path.join(input_dir, input_filename),
                  os.path.join(midres_dir, input_filename))
    else:
      low_res.append(input_filename)
      shutil.move(os.path.join(input_dir, input_filename),
                  os.path.join(lowres_dir, input_filename))

  print('# of High rez imgs (512x512 or larger):', len(high_res))
  print('# of Mid rez imgs (>= 256x256 and < 512x512):', len(mid_res))
  print('# of Low rez imgs (< 256x256):', len(low_res))

  print('High rez imgs (512x512 or larger):', high_res, '\n')
  print('Mid rez imgs (>= 256x256 and < 512x512):', mid_res, '\n')
  print('Low rez imgs (< 256x256):', low_res, '\n')
