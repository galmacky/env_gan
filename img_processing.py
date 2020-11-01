from PIL import Image
import os
import argparse
            
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
  for input_filename in os.listdir(input_dir):
    img = Image.open(os.path.join(input_dir, input_filename))

    # Write to output png
    output_filename = str(counter)+'.png'
    img.save(os.path.join(output_dir, output_filename))

    # Rotate image
    rotate_ccw_img = img.rotate(10, expand=True)
    rotate_cw_img = img.rotate(-10, expand=True)
    rotate_ccw_img.save(os.path.join(output_dir, str(counter)+'_ccw10.png'))
    rotate_cw_img.save(os.path.join(output_dir, str(counter)+'_cw10.png'))

    # Flip image horizontally
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_ccw_img = rotate_ccw_img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_cw_img = rotate_cw_img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img.save(os.path.join(output_dir, str(counter)+'_flipped.png'))
    flipped_ccw_img.save(os.path.join(output_dir, str(counter)+'_ccw10_flipped.png'))
    flipped_cw_img.save(os.path.join(output_dir, str(counter)+'_cw10_flipped.png'))

    counter += 1

  print('Finished image processing!')
