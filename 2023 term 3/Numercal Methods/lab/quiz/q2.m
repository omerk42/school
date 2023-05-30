list1 = input('Enter the list1, separated by spaces: ', 's');
list1Values = strsplit(list1, ' ');
list2 = input('Enter the list2, separated by spaces: ', 's');
list2Values = strsplit(list2, ' ');
hasSameData = true;

if length(list1Values) ~= length(list2Values)
    hasSameData = false;
else
    for i = 1:length(list1Values)-1
      for j = 1:length(list1Values)
        if strcmp(list1Values{i}, list2Values{j})
            hasSameData = true;
            break;
        end
      end
    end
end

% Display the result
if hasSameData
    disp('The list1 and list2 have the same data.');
else
    disp('The list1 and list2 do not have the same data.');
end
