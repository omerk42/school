
words = input('Enter values separated by spaces: ', 's');
wordList = strsplit(words, ' ');
target = input('Enter word to count: ', 's');

wordCount = 0; 

for i = 1:length(wordList)
    if strcmp(wordList(i), target)
        wordCount = wordCount + 1;  
    end
end

disp(['The word "', target, '" appears ', num2str(wordCount), ' times.']);

