I = imread('tree.jpg');
figure(1);
imshow(I);
J = rgb2gray(I);
K = histeq(J);
figure(2);
subplot(2,3,1),imshow(J),title('J image');
subplot(2,3,2),imshow(hist(J)),title('J hist');

subplot(2,3,1),imshow(K),title('K image');
subplot(2,3,2),imshow(hist(K)),title('K hist');

imwrite(K,'image K.png');
