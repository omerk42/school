x0 = input('Enter x0 value - ');
y0 = input('Enter y0 value - ');
h = input('Enter h value - ');
xn = input('Enter xn value - ');
n=(xn-x0)/h+1;
for i=1:n
    y=y0+h*((x0-y0)/(x0+y0));
    x=x0+h;
    fprintf('X=%f Y=%f \n',[x0],[y0]);
    if(x<xn)
        x0=x;
        y0=y;
    end
end