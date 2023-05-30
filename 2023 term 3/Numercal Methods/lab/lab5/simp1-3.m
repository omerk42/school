result = 1;

disp("Enter the range: ");
a = input("Lower limit a: ");
b = input("Upper limit b: ");
n = input("Enter subinterals: ");

h = (b-a)/n;
sum =0;
sum = (1/(1+(a*a)))+4*(1/(1+((a+h)*(a+h))))+(1/(1+(b*b)));

