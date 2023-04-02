image=imread('tree.jpg');
image_gray=rgb2gray (image);

subplot(2,3,1),imshow(image),title('Original image');
subplot(2,3,2),imshow(image_gray),title('Bulit-in grayscale')

redChannel = image(:, :, 1);
greenChannel = image(:, :, 2);
blueChannel = image(:, :, 3);

subplot(2,3,3),imshow(redChannel),title('Red channel')
subplot(2,3,4),imshow(greenChannel),title('Green channel')
subplot(2,3,5),imshow(blueChannel),title('Blue channel')

cus = 0.2989 * double(redChannel) + 0.5870 * double(greenChannel) + 0.1140 * double(blueChannel);
subplot(2,3,6),imshow(cus)
title('cus')