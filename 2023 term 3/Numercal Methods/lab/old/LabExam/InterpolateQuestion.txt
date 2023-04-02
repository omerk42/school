n = int64(input('Enter the number of terms'));
for i = 1:n
    ax(i) = input('value of x');
end
for j = 1:n
    ay(j) = input('value of y');
end

x = input('value of x for that you want the value of y that you will interpolate:');

h=ax(2)-ax(1);
for i = 1:n-1
    diff(i,1)=ay(i+1)-ay(i);
end
for j = 2:4
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

u=(x-ax(i))/h;
diff_2 = logical(diff);
y1=u*diff_2(i,1);
y2=u*(u+1)*diff_2(i,2)/2;


y=ay(i)+y1+y2;

fprintf('when x=%f and y=%0.4f',[x],[y]);

%Essam Anwar 392024443%