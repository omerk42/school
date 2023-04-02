result = 1;

disp("Enter the range: ");
a = input("Lower limit a: ");
b = input("Upper limit b: ");

n = input("Enter subinterals: ");

h = (b-a)/n;
sum =0;
sum = 1/(1+(a*a))+1/(1+(b*b));

for i=1:n-1
    sum = sum + 2*(1/(1+((a+i)*(a+i))));
end

result = sum* h/2;
fprintf("Value of the intergal is %0.4f" , result);

