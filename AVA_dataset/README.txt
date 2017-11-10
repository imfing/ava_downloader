**************************************************************************
AVA Dataset - June 2012 Release

For detailed information, please refer to:

“AVA: A Large-Scale Database for Aesthetic Visual Analysis”. Naila Murray,
 Luca Marchesotti, Florent Perronnin, CVPR 2012.

Contacts:
Naila Murray (nmurray [at] cvc [dot] uab [dot] es)
Luca Marchesotti (Luca [dot] Marchesotti [at] xrce [dot] xerox [dot] com)
**************************************************************************

This package contains:

1. AVA.txt
2. tags.txt
3. challenges.txt
4. aesthetic image lists: lists of train and test images used for aesthetics
experiments.
5. style image lists: lists of train and test images used for style 
experiments.

**************************************************************************
Content of AVA.txt
**************************************************************************

Column 1: Index

Column 2: Image ID 

Columns 3 - 12: Counts of aesthetics ratings on a scale of 1-10. Column 3 
has counts of ratings of 1 and column 12 has counts of ratings of 10.

Columns 13 - 14: Semantic tag IDs. There are 66 IDs ranging from 1 to 66.
The file tags.txt contains the textual tag corresponding to the numerical
id. Each image has between 0 and 2 tags. Images with less than 2 tags have
a "0" in place of the missing tag(s).

Column 15: Challenge ID. The file challenges.txt contains the name of 
the challenge corresponding to each ID.

**************************************************************************
Aesthetics image Lists
**************************************************************************

The aesthetics_image_lists directory contains files with the IDs of images
used for training and testing generic aesthetics classifiers. There were:

1. small scale (ss) experiments with few training images.
2. large scale (ls) experiments with many training images.

The directory also contains lists of training and testing images used for
content (or category)-dependent classifiers. The categories are: animal,
architecture, cityscape, floral, food/drink, landscape, portrait, and 
still-life.

**************************************************************************
Style image Lists
**************************************************************************

The style_image_lists directory contains files with the IDs of images
used for training and testing photographic style classifiers. The files are:

1. train.jpgl - list of IDs of training images
2. test.jpgl  - list of IDs of testing images
3. styles.txt - numeric style IDs and their associated photographic styles.
4. train.lab  - annotations for images in train.jpgl consisting of numeric
style IDs.
5. test.multilab - binary annotations for images in test.jpgl. There are 14 
columns corresponding to the 14 possible styles so that, for example, a 1 
in column 3 means that the image has been labeled with the 3rd style listed 
in styles.txt

Note that the training images are single-labeled, but the test images are
multilabeled.

**************************************************************************
How to obtain the images?
**************************************************************************

The URLs for the images are constructed as:

    http://www.dpchallenge.com/image.php?IMAGE_ID=<Image_ID>

e.g.,

    http://www.dpchallenge.com/image.php?IMAGE_ID=359334


**************************************************************************
Copyright Considerations
**************************************************************************

Rights to all images are retained by the photographers/dpchallenge. This 
is why the image files are not included in the database. Please respect 
the copyright and refrain from redistributing images or data.
