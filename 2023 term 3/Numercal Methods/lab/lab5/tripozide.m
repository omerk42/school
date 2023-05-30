a = input("Input Lower limit a ");
b = input("Input Upper Limit b ");
n = input("Input number of sub intervals ");

h = (b-a)/n;

funA = funct(a);
funB = funct(b);
sum = funA+funB;

for i=1:n-1
    % a+(i*h) is x's between first and last x
    funi = funct(a+(i*h));
    sum = sum + 2*funi;
end

result = sum*(h/2);
fprintf("Value of the intergal is %6.4f \n" , result);

% fun is doing the opreation to find f(x)
% it depend on the question
function fun = funct(x)
  fun = x^3;
end  
