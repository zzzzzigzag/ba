import scipy.io as sio
# import numpy as np
import html

# np.set_printoptions(threshold=np.inf)

# load matlab data
obj_info = sio.loadmat('obj_info.mat')

frame_rate = obj_info['frame_rate'][0][0]
height = obj_info['height'][0][0]
width = obj_info['width'][0][0]
num_of_frames = obj_info['numFrame'][0][0]


frames = []
for k in range(1, int(num_of_frames)+1):
    frame = sio.loadmat('mats/'+format(str(k))+'.mat')['rawframe']
    frames.append(frame)


frames_text = []
it_ = 0
for frame in frames:
    it_ += 1
    if it_ % 100 == 0:
        print('loading.......%4.2f%%' % float(100 * it_ / num_of_frames))
    frame_text = ""
    for row in range(0, height):
        for col in range(0, width):
            pix = '#' if frame[row][col] else ' '
            frame_text += pix
        frame_text += '\n'
    frames_text.append(frame_text)

# # ## ### ####

# front_end :
# reference = 'http://www.jianshu.com/p/500dfe5b57e7'

# #### ### ## #

head = '''
<html>
<head>
</head>
<style>
pre {display:none;font-family:simsun;font-size:14px; line-height:14px}
</style>
<script>
window.onload = function(){
    var pres = document.getElementsByTagName('pre');
    var i = 0;
    var play = function(){
        if(i > 0){
            pres[i-1].style.display = 'none';
        }
        pres[i].style.display = 'inline-block';
        i++;
        if(i == pres.length){
            clearInterval(run)
        }
    }
    run = setInterval(play, '''+format(str(1000/frame_rate))+''')
}
</script>
<body>
'''
foot = '''
<video width="480" height="360" controls="controls" autoplay="autoplay">
  <source src="src.mp4" type="video/mp4" />
</video>
</body>
</html>
'''
# Why is the frame rate higher than it should be?

with open('output.html', 'w') as f:
    f.write(head)
    for frame_text in frames_text:
        f.write("<pre>")
        f.write(html.escape(frame_text))
        f.write("</pre>")
    f.write(foot)


