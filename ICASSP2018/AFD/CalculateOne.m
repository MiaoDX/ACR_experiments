function CalculateOne(dir)
    %dir = 'F:\research&project\Our_Paper\PAMI2017_Camera6dRelocation\results\repairEvaluation\data\3\';
    srcImage = imread(fullfile(dir,'image1.jpg'));
    dstImage = imread(fullfile(dir,'image2.jpg'));
    % srcImage = imresize(srcImage,0.3);
    % dstImage = imresize(dstImage,0.3);
    [height,width, dim] = size(srcImage);
    [match1, match2] = siftMatchWithRansac(single(rgb2gray(srcImage)), single(rgb2gray(dstImage)));
    error = match1 - match2;
    AFD = mean(sqrt(sum(error .^ 2,1)));

    h = DrawMatch(match1,match2,width,height);
    print(h,'-depsc',fullfile(dir, 'FDF.eps'));
    close(h);

    save(fullfile(dir,'AFD.mat'),'AFD');
end

