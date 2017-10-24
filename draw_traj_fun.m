function [ lim ] = draw_traj_fun( varargin )
%UNTITLED 此处显示有关此函数的摘要
%   此处显示详细说明
% Camera trajectory
% draw_traj_fun('json_file', 'result.json', 'start', 1, 'show_num', 3, 'cameraSize', 2, 'coor_lim', 30)

argvs = inputParser;

%接下来设定默认值，还可以指定是必须参数还是可选参数等。
argvs.addParameter('json_file', 'result.json');
argvs.addParameter('start', 10);
argvs.addParameter('show_num', 5);
argvs.addParameter('cameraSize', 0.1);
argvs.addParameter('coor_lim', 1);
argvs.addParameter('present_dir', 'present_dir');


%然后将输入的参数进行处理，如果有不同于默认值的那就覆盖掉
argvs.parse(varargin{:})
args = argvs.Results;
start = args.start;
show_num = args.show_num;
cameraSize = args.cameraSize;
coor_lim = args.coor_lim;
json_file = args.json_file;
present_dir = args.present_dir;

addpath('.')
addpath('jsonlab')

traj=loadjson(json_file);

[ref_loc, ~ , ref_Tw] = get_loc_orient_Tw_from_pose(traj.im_ref_pose);


% Visualize the point cloud in centimeters

figure('Name', present_dir)
%plotCamera('Size', cameraSize, 'Color', 'r', 'Label', '1', 'Opacity', 0);
% plotCamera('Location', ref_loc, 'Orientation', ref_orient, 'Size', cameraSize, ...
% 'Color', 'r', 'Label', 'ref', 'Opacity', 0);

%drawCam(ref_orient, ref_loc', 'gt', 1)
C = camstruct('f', 320, 'rows', 480, 'cols', 640, 'Tw_c', ref_Tw, 'label', 'ref');
plotcamera(C, cameraSize, [1,0,0])

hold on
grid on

num = traj.num;
end_num = min( start+show_num-1, num);
Cs = [];

for i = start:end_num
    pose = traj.poses{i};
    [~, ~, Tw] = get_loc_orient_Tw_from_pose(pose);
%     plotCamera('Location', loc, 'Orientation', orient, 'Size', cameraSize, ...
%     'Color', 'b', 'Label', int2str(i) , 'Opacity', i/num*0.1, 'AxesVisible', true);
    %drawCam(orient, loc', 'gt', 1)
    %drawCam(orient, loc')
    Cs =[Cs, camstruct('f', 320, 'rows', 480, 'cols', 640, 'Tw_c', Tw, 'label', int2str(i))];
  
    
end
plotcamera(Cs, cameraSize, '', 1)

lim = coor_lim;

xlim([ref_loc(1)-lim, ref_loc(1)+lim]);
ylim([ref_loc(2)-lim, ref_loc(2)+lim]);
zlim([ref_loc(3)-lim, ref_loc(3)+lim]);

% Label the axes
xlabel('x-axis (cm)');
ylabel('y-axis (cm)');
zlabel('z-axis (cm)')
title('Camera trjaectory');

end

