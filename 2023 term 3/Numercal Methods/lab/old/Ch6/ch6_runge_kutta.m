x0 = input('Enter x0 value - ');
y0 = input('Enter y0 value - ');
h = input('Enter h value - ');
xn = input('Enter xn value - ');

n=(xn-x0)/h;
x=x0;
y=y0;
for i=0:n
    k1=h*((x-y)/(x+y));
    k2=h*(((x+h/2.0)-(y+k1/2.0))/((x+h/2.0)+(y+k1/2.0)));
    k3=h*(((x+h/2.0)-(y+k2/2.0))/((x+h/2.0)+(y+k2/2.0)));
    k4=h*(((x+h)-(y+k3))/((x+h)+(y+k3)));
    k=(k1+(k2+k3)*2.0+k4)/6.0;
    fprintf('X=%f Y=%f \n', [x], [y]);
    x=x+h;
    y=y+k; 
end