result = 1;

disp("Enter the range: ");
a = input("Lower limit a: ");
b = input("Upper limit b: ");

n = input("Enter subinterals: ");

h = (b-a)/n;
sum =0;
sum = (1/(1+(a*a)))+4*(1/(1+((a+h)*(a+h))))+(1/(1+(b*b)));

for i=3:2:n-1
    sum = sum + 2*(1/(1+((a+(i-1)*h)*(a+(i-1)*h))))+ 4*(1/(1+((a+i*h)*(a+i*h))));
end

result = sum*h/3;
fprintf("Value of the intergal is %0.4f" , result);

