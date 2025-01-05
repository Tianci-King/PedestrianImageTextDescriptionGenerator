# Pedestrian Image Text Description Generator
## Introduction

A Pedestrian Image Text Description Generator, powered by GPT-4o, utilizes Prompt Chaining technology to enhance recognition accuracy.



![Project Framework](https://raw.githubusercontent.com/Tianci-King/PicGo/main/img/image-20250106011122267.png)



--------

## Installation

We have provided a `requirements.txt` file detailing the specific dependency versions. Use the following command to install the required libraries.



```bash
pip install -r requirements.txt
```



-----------

## Datasets

The **Market-1501** dataset was collected on the Tsinghua University campus, filmed in the summer, and was constructed and made publicly available in 2015. It includes 1,501 pedestrians and 32,668 detected pedestrian bounding boxes captured by 6 cameras (5 high-definition cameras and 1 low-definition camera). Each pedestrian is captured by at least 2 cameras, and multiple images of the same person may be available from a single camera. The training set contains 751 individuals, with 12,936 images, averaging 17.2 images per person for training; the test set contains 750 individuals, with 19,732 images, averaging 26.3 images per person for testing. The 3,368 query images' pedestrian bounding boxes are manually annotated, while the bounding boxes in the gallery are detected using a DPM detector. The dataset provides a fixed number of training and test sets, which can be used in both single-shot and multi-shot test settings.



### Dataset directory

1. **"bounding_box_test"** — For the 750 people in the test set, containing 19,732 images. The prefix "0000" indicates images where the DPM detector made an error during the extraction process (these images may belong to the same person as the query), and "-1" indicates images where other people are detected (not belonging to these 750 people).
2. **"bounding_box_train"** — For the 751 people in the training set, containing 12,936 images.
3. **"query"** — One image is randomly selected from each camera for each of the 750 people to serve as the query. Therefore, each person may have up to 6 queries, with a total of 3,368 images.
