obj = VideoReader('src.mp4');
save('obj.mat', 'obj');

numFrame = obj.NumberOfFrames;
height = 43;
width = 116;
frame_rate = obj.FrameRate;
save('obj_info.mat', 'frame_rate','width','height','numFrame');

outline = 0;
for fr = 1:numFrame
    frame = read(obj,fr);
    grayframe = rgb2gray(frame);
    bwframe = im2bw(grayframe);
    if(outline)
        bwframe = xor(bwframe(:, 1:end - 1), bwframe(:, 2:end));
    end
    % imwrite(bwframe,strcat('frames\',num2str(fr),'.jpg'),'jpg');
    rawframe = imresize(bwframe, [height, width]);
    save(strcat('mats\',num2str(fr),'.mat'),'rawframe');
    if(mod(fr,100) == 0)
        fprintf('loading....%4.2f%%\n',double(fr*100)/numFrame);
    end
end