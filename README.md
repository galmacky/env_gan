# env_gan
cs230 project repository

Training & Test data processing:
- raw: the original files
- matched: image files that are matched (before, fire, after)
- fire: image files that contain fire
  - firedetectionnet: curated samples from
https://www.pyimagesearch.com/2019/11/18/fire-and-smoke-detection-with-keras-and-deep-learning/ (only 6 meet our criteria out of the first 100 images (in total 1400+ images)
  - firenet: curated samples from https://github.com/OlafenwaMoses/FireNET

Data Collection Methodology for 'matched':
- Go to google.com and search 'california wildfire before and after'
- Save files as raw image files first, and add numbering.

- How to split image files:
- Go to pixlr.com and load the URL (or local image file)
- Choose 'crop' icon on the left, and set the 'width' as half of the original
  size.
- You don't need to execute 'apply', but can just save the selected part.
- Save as .png file format

