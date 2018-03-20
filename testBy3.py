from subprocess import Popen,PIPE
ass_path = 'text2.ass'
gif_path = 'sorry.gif'
video_path = 'input.mp4'
cmd = "ffmpeg -i {video_path} -r 8 -vf ass={ass_path},scale=300:-1 -y {gif_path}" \
        .format(video_path=video_path, ass_path=ass_path, gif_path=gif_path)
print(cmd)
p = Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
p.wait()
if p.returncode==-1:
    print("error")
