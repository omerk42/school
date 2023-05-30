Val = input('Enter values separated by spaces: ', 's');

valList = strsplit(Val, ' ');

numericVal = str2double(valList);

if any(isnan(numericVal))
    disp('Error: Invalid input. Please enter numeric Val only.');
    return;
end

modeCount = 0;
modeValue = [];
for i = 1:length(numericVal)
    count = sum(numericVal == numericVal(i));
    if count > modeCount
        modeCount = count;
        modeValue = numericVal(i);
    end
end

sortedVal = sort(numericVal);
medianIndex = ceil(length(sortedVal) / 2);
medianValue = sortedVal(medianIndex);

% smallestValue = min(numericVal);
smallestValue = 0;
for i = 1:length(numericVal)-1
  for j = i+1:length(numericVal)
    if numericVal(i) < numericVal(j)
      smallestValue = numericVal(i);
    else 
      smallestValue = numericVal(j);
    endif
  endfor
endfor  

% largestValue = max(numericVal);
largestValue = 0;
for i = 1:length(numericVal)-1
  for j = i+1:length(numericVal)
    if numericVal(i) > numericVal(j)
      largestValue = numericVal(i);
    else 
      largestValue = numericVal(j);
    endif
  endfor
endfor


meanValue = mean(numericVal);
varianceValue = sum((numericVal - meanValue).^2) / length(numericVal);

fprintf('Mode: %g\n', modeValue);
fprintf('Median: %g\n', medianValue);
fprintf('Smallest value: %g\n', smallestValue);
fprintf('Largest value: %g\n', largestValue);
fprintf('Variance: %g\n', varianceValue);