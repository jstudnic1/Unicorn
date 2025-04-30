#!/Users/jakubstudnicka/Documents/UnicornUni/AI/.venv-tf/bin/python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

# Load KITTI dataset using TensorFlow Datasets
# Note: This will download the dataset the first time it's run (approx. 12GB)
# It might take a while.
ds, info = tfds.load('kitti', split='train', with_info=True)

# TFDS loads data as a tf.data.Dataset. You'll likely need to process it.
# This example just takes the first batch to demonstrate loading.
# You will need to adapt this based on your specific needs for x_train/y_train.
for example in ds.take(1):  # Take one example from the dataset
    image = example['image']
    objects = example['objects']
    # You would typically extract x_train (image) and y_train (labels like bbox, type)
    # from the 'example' dictionary here and potentially batch them.
    print("Image shape:", image.shape)
    print("Object types:", objects['type'])
    # Assigning the first example's image and object types for demonstration
    # This is NOT equivalent to your original x_train, y_train split!
    x_train_example = image
    y_train_example = objects['type']


# The following lines using x_train, y_train will likely fail or need adjustment
# because the structure loaded by tfds is different.
# Commenting them out for now.
# print(x_train.shape)
# print(y_train.shape)

