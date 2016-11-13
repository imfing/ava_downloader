# AVA dataset downloader

**AVA: A Large-Scale Database for Aesthetic Visual Analysis**

[http://www.lucamarchesotti.com/](http://www.lucamarchesotti.com/)

AVA is a large-Scale database for aesthetic visual analysis containing 250000+ photos from dpchallenge.com.
However, the downloaded pakage only has image list and annotations. You may need the script to download AVA images from website.

## Usage

1. Download ava_downloader.py to any directory you like.

2. Make sure you have downloaded AVA Database (zip, 4.2 MB) from the [site](http://www.lucamarchesotti.com/ava/download/start_download.html).

3. Unzip AVA_dataset.zip and place AVA.txt under the same directory as the script. Also create a folder 'image'

4. Run the script with command $python ava_downloader.py *beginIndex endIndex*

5. **Tips:** Note that *beginIndex* and *endIndex* both range from 1 to 25553. Downloading all the images would **consume a lot of time**. It is recommended you download a small amount once a time.

## More

- [ ] Multithreading download
- [ ] Catch errors

Happy downloading~ :sunglasses:

Fing

2016-11-13