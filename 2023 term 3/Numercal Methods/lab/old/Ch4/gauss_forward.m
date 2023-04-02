n = int64(input('Enter the number of terms- '));
for i = 1:n
    ax(i) = input('Enter the value of x- ');
end
for j = 1:n
    ay(j) = input('Enter the value of y- ');
end
x = input('Enter the value of x for which you want the value of y- ');

h=ax(2)-ax(1);
for i = 1:n-1
    diff(i,2)=ay(i+1)-ay(i);
end
for j = 3:5
    for i = 1:n-j
        diff(i,j)=diff(i+1,j-1)-diff(i,j-1);
    end
end
i=1;
while 1
    i=i+1;
    if ~(ax(i)<x)
        break;
    end
end
i=i-1;
p=(x-ax(i))/h;
y1=p*diff(i,2);
y2=p*(p-1)*diff(i-1,3)/2;
y3=(p+1)*p*(p-1)*diff(i-2,4)/6;
y4=(p+1)*p*(p-1)*(p-2)*diff(i-3,5)/24;

y=ay(i)+y1+y2+y3+y4;
fprintf('when x=%6.4f,y=%6.8f',[x],[y]);