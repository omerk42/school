data = input('Enter number of data points- ');
for i=1:data
   x(i) = input('Enter values of x: ');
end

for i=1:data
   y(i) = input('Enter values of f(x): ');
end
sum1=0;
sum2=0;
sum3=0;
sum4=0;

for i=1:data
   xy(i)=x(i)*y(i);
   x2(i)=x(i)*x(i);
   sum1 = sum1 + xy(i);
   sum2 = sum2 + x2(i);
   sum3 = sum3 + x(i);
   sum4 = sum4 + y(i);
end

sum3 = sum3/2;
sum4 = sum4/2;
sum1=(sum1/sum2);
z= (sum1*sum3)-sum4;
fprintf('The reggression line of y on x is: \n');
fprintf('y=%.2f *x - (%.2f)',sum1,z);