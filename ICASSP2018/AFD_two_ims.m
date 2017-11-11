function [ AFD ] = AFD_two_ims( ref_im_name, cur_im_name )
%UNTITLED4 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��

srcImage = imread(fullfile(ref_im_name));
dstImage = imread(fullfile(cur_im_name));

[match1, match2] = siftMatchWithRansac(single(rgb2gray(srcImage)), single(rgb2gray(dstImage)));
error = match1 - match2;
AFD = mean(sqrt(sum(error .^ 2,1)));

end

