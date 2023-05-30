I = imread('tree.jpg');
figure();
imshow(I);
axis on;
A = [cos(45) sin(45) 0; -sin(45) cos(45) 0; 0 0 1];
tform = affinetform2d(A)
J = imwarp(I,tform);
imshow(J);
hold off;
axis on;