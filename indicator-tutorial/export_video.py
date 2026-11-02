from pathlib import Path
import json,subprocess,math,concurrent.futures
p=Path(__file__).parent;t=json.loads((p/'timing.json').read_text()); scenes=json.loads((p/'scenes.json').read_text());seg=p/'segments';seg.mkdir(exist_ok=True)
def run(i):
 x=t[i];d=math.ceil(x['duration']*24)/24;png=next((p/'delivery-frames').glob(f'frame-{i:02}-at-*.png'));o=seg/f'{i:02}.mp4';log=seg/f'{i:02}.log'
 # Fade through the light canvas at each scene boundary. Audio begins 0.8s into each scene.
 vf=f'fade=t=in:st=0:d=0.3:color=0xf4f7fa,fade=t=out:st={d-.3}:d=0.3:color=0xf4f7fa,format=yuv420p'
 args=['ffmpeg','-hide_banner','-loglevel','error','-y','-loop','1','-framerate','24','-i',str(png),'-i',str(p/'assets'/f'voice-{i:02}.wav'),'-vf',vf,'-af','adelay=800,apad,alimiter=limit=0.9:level=false','-t',str(d),'-c:v','libx264','-preset','veryfast','-tune','stillimage','-crf','19','-threads','2','-c:a','aac','-b:a','128k','-ar','48000','-ac','1','-movflags','+faststart',str(o)]
 with open(log,'w') as f:subprocess.run(args,stdout=f,stderr=f,check=True)
 print(f'Encoded scene {i+1}/{len(t)}',flush=True);return d
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: ds=list(ex.map(run,range(len(t))))
(seg/'concat.txt').write_text(''.join(f"file '{i:02}.mp4'\n" for i in range(len(t))))
meta=[';FFMETADATA1','title=HVI × ST1 × ST2 — Hướng dẫn sử dụng','comment=Sơ đồ minh họa theo mô tả của tác giả. Thuyết minh Việt tổng hợp ngoại tuyến.'];pos=0
for s,d in zip(scenes,ds):
 meta+=['[CHAPTER]','TIMEBASE=1/1000',f'START={round(pos*1000)}',f'END={round((pos+d)*1000)}','title='+s[0]];pos+=d
(seg/'chapters.ffmeta').write_text('\n'.join(meta))
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(seg/'concat.txt'),'-i',str(seg/'chapters.ffmeta'),'-map_metadata','1','-map_chapters','1','-c','copy','-movflags','+faststart',str(p/'huong-dan-HVI-ST1-ST2.mp4')],check=True)
print('DONE',pos,flush=True)
