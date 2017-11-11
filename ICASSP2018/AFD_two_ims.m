function [ AFD ] = AFD_two_ims( ref_im_name, cur_im_name )
%UNTITLED4 此处显示有关此函数的摘要
%   此处显示详细说明

%run('C:\Code\miaodx\ACR_experiments\ICASSP2018\AFD\vlfeat-0.9.20\toolbox\vl_setup')

srcImage = imread(fullfile(ref_im_name));
dstImage = imread(fullfile(cur_im_name));

[match1, match2] = siftMatchWithRansac(single(rgb2gray(srcImage)), single(rgb2gray(dstImage)));
error = match1 - match2;
AFD = mean(sqrt(sum(error .^ 2,1)));

end

