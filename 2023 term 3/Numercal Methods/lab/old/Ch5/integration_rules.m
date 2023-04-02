disp('Enter the range: ');
a = input('Lower limit a: ');
b = input('Upper limit b: ');

n = input('Enter subinterals: ');
sum =0;
h = (b-a)/n;

if mod(n, 2) == 0
    disp('Simpson 1/3 used');
    sum = (1/(1+(a*a)))+4*(1/(1+((a+h)*(a+h))))+(1/(1+(b*b)));
    for i=3:2:n-1
        sum = sum + 2*(1/(1+((a+(i-1)*h)*(a+(i-1)*h))))+ 4*(1/(1+((a+i*h)*(a+i*h))));
    end
    result = sum*h/3;
    fprintf('Value of the intergal is %0.4f' , result);  

elseif mod(n, 3) == 0
    disp('Simpson 3/8 used');
    sum = 1/(1+(a*a))+1/(1+(b*b));
    for i=1:n-1
        if mod(i,3) ==0
            sum = sum + 2*(1/(1+((a+i*h)*(a+i*h))));
        else
            sum = sum + 3*(1/(1+((a+i*h)*(a+i*h))));
        end
    end
    result = sum *3* h/8;
    fprintf('Value of the intergal is %0.4f' , result);

else
    disp('Trapezoidal used');
    sum = 1/(1+(a*a))+1/(1+(b*b));
    for i=1:n-1
        sum = sum + 2*(1/(1+((a+i)*(a+i))));
    end
    result = sum* h/2;
    fprintf('Value of the intergal is %0.4f' , result);
end