result = 1;

disp("Enter the range: ");
a = input("Lower limit a: ");
b = input("Upper limit b: ");

n = input("Enter subinterals: ");

h = (b-a)/n;
sum =0;
sum = 1/(1+(a*a))+1/(1+(b*b));

for i=1:n-1
    if mod(i,3) ==0
        sum = sum + 2*(1/(1+((a+i*h)*(a+i*h))));

    else
        sum = sum + 3*(1/(1+((a+i*h)*(a+i*h))));

    end
end

result = sum *3* h/8;
fprintf("Value of the intergal is %0.4f" , result);

