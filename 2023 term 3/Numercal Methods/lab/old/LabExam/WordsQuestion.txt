m = input("Enter the number of the words do you want to store: ")
for i = 1:m
    words(i) = input('Enter a word:','s');
end
%words = ["Mohammed","Essam","Essam","Essam"];

count =0;
for i = 1:m
    if (words(i) == "Essam")
      count = count +1;  
    end
end

disp(count);

%Essam Anwar  392024443%