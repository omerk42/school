
n = int64(input('Enter the number of terms- '));

for i = 1:n
    mx(i) = input('Enter the value of x- ');
end

for j = 1:n
    my(j) = input('Enter the value of y- ');
end

x = input('Enter the value of x for which you want the value of y- ');


h=mx(2)-mx(1);

for i = 1:n-1
    diff(i,2)=my(i+1)-my(i);
end
for j = 3:5
    for i = 1:n-j
        diff(i,j)=diff(i+1,j-1)-diff(i,j-1);
    end
end

i=1;
while 1
    i=i+1;
    if ~(mx(i)>x)
        break;
    end
end
x0=mx(i);
sum=0;
y0=my(i);
fun=1;
p=(x-x0)/h;
sum=y0;

for k=1:4
    fun=(fun*(p-(k-1)))/k;
    sum=sum+fun*diff(i,k);
end
%{
fprintf('x0=%f',x0);
fprintf('p=%f',p);
fprintf('n=%f',n);

for i=1:n
    disp(mx(i), my(i));
end    
%}
    
fprintf('when x=%6.4f and y=%6.4f',[x],[sum]);