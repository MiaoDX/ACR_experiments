function [Imout] = markRed(Imin,GT)
[height,width,dim] = size(Imin);
Imout = im2double(Imin);
GT = repmat(GT,[1 1 3]);
GT = (GT == 1);

allRed = zeros(height,width,dim);
allRed(:,:,1) = ones(height,width);
%imshow(allRed);
Imout(GT) = allRed(GT);

end

