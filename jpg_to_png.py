from PIL import Image
import os
import argparse
import glob

            
if __name__ == "__main__":
  print('Starting image processing...')
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-i', '--input_dir', default='input', type=str, help='input directory')
  parser.add_argument('-o', '--output_dir', default='output', type=str, help='output directory')
  args = parser.parse_args()
  input_dir = args.input_dir
  output_dir = args.output_dir
  if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

  counter = 0
  listing = glob.glob(os.path.join(input_dir, '*.jpg'))
  for input_filename in listing:
    img = Image.open(input_filename)

    # Write to output png
    output_filename = 'a' + str(counter)+'.png'
    img.save(os.path.join(output_dir, output_filename))
    counter += 1

  print('Finished image processing!')
