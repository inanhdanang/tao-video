exec(open('/workspace/indicator-tutorial/build.py').read().split("E='/workspace")[0])
T=json.loads((P/'timing.json').read_text()); total=T[-1]['start']+T[-1]['duration']
esc=html.escape
BUY='#087f55';SELL='#c9364c';BLUE='#2859c5';ORANGE='#b56700';INK='#142d42'
def text(x,y,s,color=INK,size=24,weight=400): return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}">{esc(s)}</text>'
def chart(kind):
 out=['<svg viewBox="0 0 1120 660" width="1120" height="660" xmlns="http://www.w3.org/2000/svg">','<rect width="1120" height="660" rx="20" fill="white"/>']
 for x in range(55,1100,60): out.append(f'<path d="M{x} 60 V590" stroke="#e8edf1"/>')
 for y in range(70,590,50): out.append(f'<path d="M35 {y} H1090" stroke="#e8edf1"/>')
 out.append(text(35,38,'SƠ ĐỒ MINH HỌA • KHÔNG PHẢI DỮ LIỆU GIÁ',size=20))
 sell=kind in ['sell','finalsell','touchsell','retest','fib']; rising=not sell
 # Distinct trajectories for each lesson.
 paths={
 'fib':[130,160,205,255,310,285,220,160,175,215,260,320,355,390],
 'retest':[130,145,160,215,260,240,205,245,330,355,375,390,410,430],
 'holdbuy':[290,275,250,265,300,330,310,280,270,250,190,160,140,120],
 'counterbuy':[240,215,240,275,310,290,260,245,220,195,180,160,145,120],
 'flatbuy':[350,335,300,280,270,255,240,225,200,175,150,125,100,85],
 'touchsell':[170,200,250,285,260,300,335,340,350,370,395,420,430,440],
 }
 vals=paths.get(kind,[355,330,345,300,280,300,255,240,260,210,170,190,130,110] if rising else [110,135,120,170,190,170,215,230,210,260,300,280,340,360])
 # Trend levels remain deliberate and schematic.
 st1buy=kind not in ['sell','finalsell','fib','retest','flatbuy']; level=360 if st1buy else 150
 out.append(f'<path d="M55 {level} H420 L420 {level-20 if st1buy else level+20} H740 L740 {level-40 if st1buy else level+40} H1070" fill="none" stroke="{BLUE if st1buy else ORANGE}" stroke-width="5"/>')
 out.append(text(65,level-12,'ST1 Buy' if st1buy else 'ST1 Sell',BLUE if st1buy else ORANGE,24,700))
 st2sell=kind in ['sell','finalsell','counterbuy','touchsell','fib','retest'];lev2=220 if st2sell else 310
 out.append(f'<path d="M55 {lev2} H1070 V{lev2+90 if st2sell else lev2-90} H55 Z" fill="{SELL if st2sell else BUY}" opacity=".08"/>')
 out.append(f'<path d="M55 {lev2} H1070" stroke="{SELL if st2sell else BUY}" stroke-width="3"/>')
 out.append(text(865,lev2-12,'ST2 Sell' if st2sell else 'ST2 Buy',SELL if st2sell else BUY,24,700))
 for i in range(58):
  pos=i/57*(len(vals)-1);a=int(pos);f=pos-a;v=vals[a]*(1-f)+vals[min(a+1,len(vals)-1)]*f
  o=v+9*math.sin(i*1.7);c=v+11*math.sin(i*2.3+1);x=58+i*17.3;col=BUY if c<o else SELL
  out.append(f'<path d="M{x} {min(o,c)-12} V{max(o,c)+13}" stroke="{col}" stroke-width="2"/><rect x="{x-5}" y="{min(o,c)}" width="10" height="{max(abs(c-o),3)}" fill="{col}"/>')
 out.append(text(35,486,'QQE',size=20));out.append(text(35,590,'HVI / RSI',size=20))
 for i in range(62):
  x=165+i*14.5;h=9+abs(math.sin(i*.19))*45; col=SELL if st2sell else '#00a7ce'
  out.append(f'<rect x="{x}" y="{500 if st2sell else 550-h}" width="10" height="{h}" fill="{col}"/>')
  h2=12+abs(math.sin(i*1.73))*35; col2=ORANGE if i%8==0 else '#cdd4db'
  out.append(f'<rect x="{x}" y="{638-h2}" width="9" height="{h2}" fill="{col2}"/>')
 hvi_sell=kind in ['sell','counterbuy','touchsell','retest','holdbuy','finalbuy'];color=SELL if hvi_sell else BUY;label='Sell' if hvi_sell else 'Buy'
 out.append(f'<rect x="330" y="568" width="88" height="36" rx="6" fill="{color}"/>');out.append(text(345,594,'HVI '+label,'#ffffff',20,700))
 out.append(f'<path d="M375 560 V{285 if st2sell else 360}" stroke="{color}" stroke-width="3" stroke-dasharray="7 6"/>')
 out.append(f'<rect x="555" y="{lev2-58}" width="125" height="40" rx="6" fill="{SELL if st2sell else BUY}"/>');out.append(text(569,lev2-29,'ST2 '+('Sell' if st2sell else 'Buy'),'#ffffff',22,700))
 if kind=='fib':
  out.append('<rect x="495" y="132" width="290" height="66" fill="#b56700" opacity=".15"/>')
  for y,label2 in [(132,'0.786'),(198,'0.618')]: out.append(f'<path d="M445 {y} H900" stroke="{ORANGE}" stroke-dasharray="8 5"/>'+text(925,y+6,label2,ORANGE,24,700))
  out.append(text(510,110,'VÙNG HỒI BỊ TỪ CHỐI',ORANGE,22,700))
 if kind=='retest':
  out.append(f'<path d="M55 360 H1070" stroke="{BLUE}" stroke-width="3" stroke-dasharray="8 6"/>'+text(760,397,'BIÊN ST1 BUY TRƯỚC ĐÓ',BLUE,22,700))
 if kind in ['retest','entry']:
  out.append(f'<path d="M410 245 H1030" stroke="{INK}" stroke-width="3" stroke-dasharray="10 6"/>');out.append(text(750,279,'MỨC ENTRY THAM CHIẾU',size=21,weight=700))
 if kind in ['holdbuy','counterbuy','touchsell']:
  out.append('<rect x="425" y="315" width="330" height="75" fill="#2859c5" opacity=".09"/>');out.append(text(620,418,'ĐỐI CHIẾU VÙNG ST1',BLUE,22,700))
 out.append('</svg>');return ''.join(out)
css='''*{box-sizing:border-box}html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#f4f7fa;color:#142d42;font-family:"DejaVu Sans",sans-serif}.scene{position:absolute;inset:0;background:#f4f7fa}.content{width:100%;height:100%;padding:32px 60px 28px;display:flex;flex-direction:column;gap:12px}.top{display:flex;justify-content:space-between;font-size:23px;font-weight:bold;letter-spacing:2px;color:#2859c5}h1{font-size:58px;margin:0;font-weight:700;line-height:1.2;letter-spacing:-1.5px}.body{display:flex;gap:40px;align-items:center;height:590px}.diagram{width:1000px;flex-shrink:0;border:1px solid #d8e1e9;border-radius:22px;overflow:hidden;background:#ffffff}.diagram svg{width:100%;height:auto;display:block}.notes{width:740px;display:flex;flex-direction:column;gap:22px}.item{background:#ffffff;border-left:6px solid #2859c5;padding:22px 24px;font-size:31px;line-height:1.43;border-radius:0 14px 14px 0}.verdict{font-size:30px;line-height:1.4;font-weight:700;padding:18px 28px;border-radius:14px;background:#e6edf8;color:#142d42;min-height:80px;display:flex;align-items:center}.footer{display:flex;justify-content:space-between;font-size:21px;color:#475d70}.progress{height:5px;width:100%;background:#dce6ee;position:absolute;bottom:0;left:0}.fill{height:5px;width:100%;background:#2859c5;transform-origin:left}.tag{display:flex;gap:16px;font-size:22px}.pill{padding:8px 16px;border-radius:8px;background:#ffffff;border:1px solid #d8e1e9}'''
parts=['<!doctype html><html lang="vi"><head><meta charset="utf-8"><script src="assets/gsap.min.js"></script><style>'+css+'</style></head><body>',f'<div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1920" data-height="1080">']
for i,(s,t) in enumerate(zip(S,T)):
 title,ch,kind,v,points,nar=s
 parts.append(f'<section id="s{i}" class="scene" style="z-index:{i+1};opacity:{1 if i==0 else 0}"><div class="content"><div class="top"><span>{esc(ch)}</span><span>HVI × ST1 × ST2</span></div><h1>{esc(title)}</h1><div class="tag"><span class="pill" style="color:#087f55">BUY • MUA</span><span class="pill" style="color:#c9364c">SELL • BÁN</span><span class="pill">Hướng dẫn theo mô tả của tác giả</span></div><div class="body"><div class="diagram">{chart(kind)}</div><div class="notes">'+''.join(f'<div class="item">{esc(x)}</div>' for x in points)+f'</div></div><div class="verdict">{esc(v)}</div><div class="footer"><span>Sơ đồ minh họa • Thuyết minh Việt tổng hợp ngoại tuyến</span><span>{i+1:02d} / {len(S):02d}</span></div></div></section>')
 parts.append(f'<audio id="a{i}" src="assets/voice-{i:02}.wav" data-start="{t["start"]+0.8}" data-duration="{t["audio"]}" data-track-index="2" data-volume="1"></audio>')
parts.append('<div class="progress" style="z-index:100"><div class="fill"></div></div></div><script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});')
for i,t in enumerate(T):
 start=t['start'];sel=f'#s{i}'
 if i: parts.append(f'tl.to("#s{i-1}",{{opacity:0,duration:0.5,ease:"power2.inOut"}},{start});tl.to("{sel}",{{opacity:1,duration:0.5,ease:"power2.inOut"}},{start});')
 parts.append(f'tl.from("{sel} .top",{{y:12,opacity:0,duration:0.4,ease:"sine.out"}},{start+.15});tl.from("{sel} h1",{{x:28,opacity:0,duration:0.55,ease:"power3.out"}},{start+.2});tl.from("{sel} .tag",{{y:10,opacity:0,duration:0.4,ease:"power1.out"}},{start+.3});tl.from("{sel} .diagram",{{y:20,opacity:0,duration:0.6,ease:"power2.out"}},{start+.35});tl.from("{sel} .item",{{x:18,opacity:0,stagger:0.16,duration:0.5,ease:"power3.out"}},{start+.55});tl.from("{sel} .verdict",{{y:12,opacity:0,duration:0.55,ease:"sine.out"}},{start+.85});tl.from("{sel} .footer",{{opacity:0,duration:0.5,ease:"power1.out"}},{start+.4});')
parts.append(f'tl.from(".fill",{{scaleX:0,duration:{total},ease:"none"}},0);window.__timelines.main=tl;</script></body></html>')
(P/'index.html').write_text(''.join(parts))
def stamp(v):
 h=int(v//3600);m=int(v%3600//60);s=v%60;return f'{h:02}:{m:02}:{s:06.3f}'.replace('.',',')
# external full transcript, readable caption blocks segmented at sentence boundaries
caps=[];num=0
for s,t in zip(S,T):
 chunks=[x.strip()+'.' for x in s[5].split('. ') if x.strip()]; count=sum(len(x) for x in chunks); pos=t['start']+.8
 for c in chunks:
  dur=t['audio']*len(c)/count;num+=1;caps.append(f'{num}\n{stamp(pos)} --> {stamp(pos+dur)}\n{c}\n');pos+=dur
(P/'thuyet-minh.srt').write_text('\n'.join(caps))
(P/'chapters.txt').write_text('\n'.join(f'{int(t["start"]//60):02}:{int(t["start"]%60):02} {s[0]}' for s,t in zip(S,T)))
print('Composition duration:',total)
