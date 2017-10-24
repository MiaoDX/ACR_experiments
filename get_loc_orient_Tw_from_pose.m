function [ loc, orient, Tw ] = get_loc_orient_Tw_from_pose( pose )
%UNTITLED 此处显示有关此函数的摘要
%   此处显示详细说明

loc = pose.loc;
orient = pose.orient;

Tw = eye(4);
Tw(1:3,1:3) = orient;
Tw(1:3,4) = loc;
end

