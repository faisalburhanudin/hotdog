import random
import shutil
from glob import glob

files = glob('/home/faisal/Downloads/food-101/images/*/*')
random.shuffle(files)

total = 0

for file in files:
    if 'hot_dog' in file:
        continue

    shutil.copy(file, '/home/faisal/hotdog/data/not_hot_dog')

    total += 1
    if total == 1001:
        break
