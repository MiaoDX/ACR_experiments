function [ AFD ] = AFD_two_ims_and_save_FDF( dir, ref_no_suffix, cur_no_suffix, out_dir )
%UNTITLED4 此处显示有关此函数的摘要
%   此处显示详细说明

%run('C:\Code\miaodx\ACR_experiments\ICASSP2018\AFD\vlfeat-0.9.20\toolbox\vl_setup')

%dir = 'F:\research&project\Our_Paper\PAMI2017_Camera6dRelocation\results\repairEvaluation\data\3\';
ref = [ref_no_suffix '.png'];
cur = [cur_no_suffix, '.png'];

srcImage = imread(fullfile(dir, ref));
dstImage = imread(fullfile(dir, cur));

[height,width, ~] = size(srcImage);
[match1, match2] = siftMatchWithRansac(single(rgb2gray(srcImage)), single(rgb2gray(dstImage)));
error = match1 - match2;
AFD = mean(sqrt(sum(error .^ 2,1)));

h = DrawMatch(match1,match2,width,height);
print(h,'-depsc',fullfile(out_dir, [cur_no_suffix, '_FDF.eps']));
close(h);

save(fullfile(out_dir, [cur_no_suffix, '_AFD.mat']),'AFD');

end

