clear;

% run('D:\Code\lib&Utility\vlfeat-0.9.20\toolbox\vl_setup');

dir = 'F:\research&project\Our_Paper\PAMI2017_Camera6dRelocation\results\repairEvaluation\data\1\';

srcImage = imread([dir 'image1.jpg']);
dstImage = imread([dir 'image2.jpg']);
[width, height, dim] = size(srcImage);
[match1, match2] = siftMatchWithRansac(single(rgb2gray(srcImage)), single(rgb2gray(dstImage)));
error = match1 - match2;
AFD = mean(sqrt(sum(error .^ 2,1)));

h = DrawMatch(match1,match2,width,height);
print(h,'-depsc',[baseDir  'FDF.eps']);
close(h);
    
save([dir 'AFD.mat'],'AFD');