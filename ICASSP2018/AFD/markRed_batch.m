dir = 'D:\Data\ÒÃºÍÔ°\Î÷±Ú\';
dirRed = [dir 'red\'];
if ~exist(dirRed,'dir')
    mkdir(dirRed);
end
ImageList = char('2-1','2-2','2-3','2-4','2-5','2-6','2-7','2-8');
extendName = '.bmp';

imageNum = size(ImageList,1);

GT = imread([dir 'GT.bmp']);
for i = 1:imageNum
    fullName = [dir ImageList(i,:) extendName];
    I = imread(fullName);
    Ired = markRed(I,GT);
    imwrite(Ired,[dirRed ImageList(i,:) '_red' extendName]);
end
