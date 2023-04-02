n = input('Enter number of observations- ');
sum1=0;
for i=1:n
   x(i) = input('Enter values of x: ');
   sum1 = sum1+ x(i);
end
sum2=0;
for i=1:n
   y(i) = input('Enter value of y: ');
   sum2 = sum2 + y(i);
end
sum3=0
for i=1:n
   xy(i) = x(i)*y(i);
   sum3 = sum3 + xy(i);
end

sum4=0
for i=1:n
   x2(i) = x(i)*x(i);
   sum4 = sum4 + x2(i);
end

a = (sum2*sum4-sum3*sum1)/(n*sum4-sum1*sum1);
b = (sum2-n*a)/sum1;

disp('Equation of the straight line');
disp('of the form y = a + b*x is:');
fprintf('Y = %.2f + (%.2f)X', a,b);