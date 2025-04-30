# Project files

Due to the amount of files in the project, it was not possible to upload all of them. The instructions to run all 3 tests will be listed below

## Baseline + Transfer

To run the baseline and transfer classifiers you must first download the dataset from this link:
https://www.kaggle.com/datasets/l3llff/flowers

Extract the ZIP file and place the "flowers" folder in the same location as the three classifiers: "Basic_one.ipynb" "Basic_two.ipynb" and "Transfer.ipynb"

You may also need to create two files: "cnn_weights.best.weights.h5" and "cnn_weights_2.best.weights.h5"

Basic_one was abandoned early in the project in favor of Basic_two, so it may fail to run.

## Meta Learning

Download the code at the following link:
https://github.com/sicara/easy-few-shot-learning/tree/master.

Extract the ZIP file "easy-few-shot-learning-master", and open it in a code editor such as Visual Studio Code.

Firstly, go to "easy-few-shot-learning-master/easyfsl/datasets" and move the provided files "flowers.py", "flowers2.py", "flowers3.py", "flowers4.py", "flowers5.py" to this location.

Next, take the content of this repository's "notebooks" folder into the downloaded repository's "notebooks" folder.

After that, go to "easy-few-shot-learning-master/data" and move the 5 "Flowers" folders into this location.

Get the "flowers" folder downloaded from the link given in the Baseline + Transfer section, and copy it into each of the "Flowers" folders. Rename it to "images" in each one.

For each of the "rare" classes in the batch that you want to test, delete all but the first 18 images in the corresponding folder.

### Notes

It is highly recommended to run the meta learning code on a computer with a GPU, and ensure that CUDA is available. The code took 6 hours to run on the CPU, reduced to 1 hour on the same device using the GPU.
