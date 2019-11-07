# cascadeAimbot

This repo is meant as a guide on using openCV cascades to interact with system operations, the repo also contains shell files to help a user build multiple cascades in parallel, as well as a single cascade generated using multiple positive images. Instructions below.

1. Create two text files called posURLS.txt and negURLS.txt and fill each with urls for your desired positive and negative images, and run the 'urlsDL.store_raw_images' function, which will pull the images and save them in pos/origSize, and neg/origSize folders depending on the argument passed ('pos' or 'neg'). Alternatively just fill these folders manually if you already have your images ready.
2. The images can be resized using resizeOrig.py, run the file changing the posOrNegString and resizeTuple variables as required. This will fill your pos or neg folder with the resized images.
3. Run bg_gen.py, which will create your bg.txt file, filled with paths to your background images.
4. Run the createPositives.sh shell file to impose your positive images on the negative images and store the results in the info folder, as well as create an lst file for your new positives.
5. Run the createVec.sh file to create a vector file for each data set in the info folder
6. Run createData.sh to create cascades for each of your positive images.

To generate a cascade from multiple positive images, complete steps 1-4 listed above then do the following.

1. Run createMasterLST.sh to create an LST file containing paths to all existing generated positive images
2. Run createMasterVec.sh to create your vector file.
3. Run createMasterCasc.sh to generate a cascade.xml file in data/master/.

For each of the shell files, be sure to examine the openCV command and adjust the parameters according to your needs.

The aimbot.py file screen_record function can be used with a generated cascade.xml. Rename your desired xml to 'target.xml' and place it in the same folder as aimbot.py. The provided file locates a training bot on the overwatch practice range, be sure to adjust the screen_height, screen_width, and sensitivity variables as needed. A video demonstrating this project is available [here](https://youtu.be/l3g4nig_8Vg).
