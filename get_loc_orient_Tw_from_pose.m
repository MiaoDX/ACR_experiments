function [ loc, orient, Tw ] = get_loc_orient_Tw_from_pose( pose )
%UNTITLED �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��

loc = pose.loc;
orient = pose.orient;

Tw = eye(4);
Tw(1:3,1:3) = orient;
Tw(1:3,4) = loc;
end

