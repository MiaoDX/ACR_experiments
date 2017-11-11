clear all;
clc;

run('D:\Code\lib&Utility\vlfeat-0.9.20\toolbox\vl_setup');

baseDir = '..\scene5\theoretical\';
I1 = imread([baseDir '0.bmp']);
[height,width,dim] = size(I1);
allAFD = zeros(10,2);
for i =  1 : 10
    I2 = imread([baseDir num2str(i) '.bmp']);
    [match1, match2] = siftMatchWithRansac(single(rgb2gray(I1)), single(rgb2gray(I2)));
    h = DrawMatch(match1,match2,width,height);
    print(h,'-depsc',[baseDir  num2str(i) '.eps']);
    close(h);
    
    FDs = match1 - match2;
    AFD = mean(sqrt(sum(FDs .^ 2,1)));
    allAFD(i,:) = [i,AFD];
end

save([baseDir 'allAFD.mat'],'allAFD');