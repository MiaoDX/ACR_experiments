function [ I ] = merge_fig( f1, f2 )
%UNTITLED 此处显示有关此函数的摘要
%   此处显示详细说明

%fig1 = open('tmp/b_1.fig');
%fig2 = open('tmp/1.fig');

fig1 = open(f1);
fig2 = open(f2);


ax1 = get(fig1, 'Children');
ax2 = get(fig2, 'Children');
%Now copy the hangle graphics objects from ax2 to ax1. The loop isn't neccesary if your figures only have a single axes

for i = 1 : numel(ax2) 
   ax2Children = get(ax2(i),'Children');
   copyobj(ax2Children, ax1(i));
end

I = 0;

end

