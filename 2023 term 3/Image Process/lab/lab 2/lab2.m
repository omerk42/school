%ex1
a = imread(Untitled.jpeg)
%ex2
imshow(a)
%ex3
imwrite(a, gray(256), "b.bmp")
imshow("b.bmp")
%ex4
[r,c]=size(a)
%ex5
a(2,15)