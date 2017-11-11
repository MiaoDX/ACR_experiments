function h = DrawMatch(match1,match2,height,width)

error = (match2 - match1);

h = figure(1);
imagesc(ones(width,height,3));
hold on;

quiver(match1(1,:),match1(2,:),error(1,:), error(2,:), 'MaxHeadSize',0.05);
axis equal;

end

