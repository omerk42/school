x = [];
y= [];
yc = [];
x(1) = input('Enter x[1] value: ');
y(1) = input('Enter y[1] value: ');
h = input('Enter h value: ');
xn = input('Enter xn value: ');

yp=y(1)+h*((x(1)-y(1))/(x(1)+y(1)));
itr=(xn-x(1))/h;

fprintf('X=%f Y=%f\n',[x(1)],[y(1)]);
for i=1:itr
   x(i+1)=x(i)+h; 
   for n=1:50
        yc(n+1)=y(i)+(h/2.0)*((x(i)-y(i))/(x(i)+y(i))+((x(i+1)-yp)/(x(i+1)+yp)));
        fprintf('N=%f Y=%f',[n],[yc(n+1)]);
        p=yc(n+1)-yp
        if(abs(p)<0.0001)
            y(i+1)=yc(n+1);
            fprintf('X=%f Y=%f\n',[x(i+1)], [yp]);
        else
            yp=yc(n+1);
        end
        
   end
end