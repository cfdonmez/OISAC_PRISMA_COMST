"""Editable, vector O-ISAC illustrations. Coordinates and font sizes are pt.

Run with the bundled Python runtime. This authors only the four flow figures.
SVG text remains editable; PDF text uses embedded Arial TrueType fonts.
"""
from pathlib import Path
from math import pi, sin, cos, atan2
from html import escape
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import toColor as HexColor

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'manuscript' / 'figures'
QA = Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))
NAVY='#16324F'; BLUE='#0072B2'; GREEN='#008665'; PURPLE='#7653A6'
AMBER='#C77C00'; GRAY='#687680'; LIGHT='#DCE3E7'; INK='#243B4A'
DIMENSIONS=[]

class Drawing:
    def __init__(self,name,h):
        self.name=name; self.w=516; self.h=h; self.items=[]; self.texts=[]
        self.c=canvas.Canvas(str(OUT/(name+'.pdf')),pagesize=(self.w,self.h),pageCompression=1)
        self.c.setTitle('O-ISAC: '+name); self.c.setAuthor('O-ISAC manuscript authors')
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="516pt" height="{h}pt" viewBox="0 0 516 {h}">', '<rect width="516" height="100%" fill="white"/>']
    def line(self,x1,y1,x2,y2,color=INK,width=.8,dash=False):
        c=self.c; c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.setDash([3,2] if dash else [])
        c.line(x1,self.h-y1,x2,self.h-y2)
        self.svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="3 2"' if dash else '')+'/>')
    def poly(self,pts,color=INK,width=.8,fill=None,close=False,dash=False):
        c=self.c;p=c.beginPath();p.moveTo(pts[0][0],self.h-pts[0][1])
        for x,y in pts[1:]:p.lineTo(x,self.h-y)
        if close:p.close()
        c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.setDash([3,2] if dash else [])
        if fill:c.setFillColor(HexColor(fill))
        c.drawPath(p,stroke=1,fill=bool(fill))
        tag='polygon' if close else 'polyline'
        self.svg.append(f'<{tag} points="'+ ' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{fill or "none"}" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="3 2"' if dash else '')+'/>')
    def rect(self,x,y,w,h,stroke=LIGHT,fill=None,width=.8,dash=False):
        self.poly([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],stroke,width,fill,True,dash)
    def ellipse(self,x,y,rx,ry=None,color=INK,width=.8,fill=None):
        ry=rx if ry is None else ry;c=self.c;c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.setDash([])
        if fill:c.setFillColor(HexColor(fill))
        c.ellipse(x-rx,self.h-y-ry,x+rx,self.h-y+ry,stroke=1,fill=bool(fill))
        self.svg.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill or "none"}" stroke="{color}" stroke-width="{width}"/>')
    def text(self,x,y,s,size=8.3,color=INK,bold=False,anchor='start'):
        font='Arial-Bold' if bold else 'Arial';w=pdfmetrics.stringWidth(s,font,size)
        left=x if anchor=='start' else x-w/2 if anchor=='middle' else x-w
        self.texts.append({'text':s,'x':left,'y':y-size,'width':w,'height':size,'font_pt':size})
        self.c.setFont(font,size);self.c.setFillColor(HexColor(color));self.c.drawString(left,self.h-y,s)
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}" fill="{color}">{escape(s)}</text>')
    def multi(self,x,y,lines,size=8.3,color=INK,bold=False,anchor='start',leading=10):
        for k,s in enumerate(lines):self.text(x,y+k*leading,s,size,color,bold,anchor)
    def arrow(self,x1,y1,x2,y2,color=INK,width=.9,dash=False,head=4):
        self.line(x1,y1,x2,y2,color,width,dash);a=atan2(y2-y1,x2-x1)
        p=[(x2,y2),(x2-head*cos(a)+head*.43*sin(a),y2-head*sin(a)-head*.43*cos(a)),(x2-head*cos(a)-head*.43*sin(a),y2-head*sin(a)+head*.43*cos(a))]
        self.poly(p,color,.35,color,True)
    def path(self,pts,color=INK,width=.9,dash=False):
        self.poly(pts,color,width,dash=dash);self.arrow(*pts[-2],*pts[-1],color,width,dash)
    def marker(self,x,y):self.ellipse(x,y,2.2,color=AMBER,fill=AMBER,width=.4)
    def finish(self):
        bad=[t for t in self.texts if t['x']<-.1 or t['x']+t['width']>self.w+.1 or t['y']<-.1 or t['y']+t['height']>self.h+.1]
        if bad:raise ValueError((self.name,'text outside canvas',bad))
        self.c.showPage();self.c.save();self.svg.append('</svg>');(OUT/(self.name+'.svg')).write_bytes('\n'.join(self.svg).encode('utf8'))
        DIMENSIONS.append({'name':self.name,'width_pt':self.w,'height_pt':self.h,'min_text_pt':min(t['font_pt'] for t in self.texts),'text_items':len(self.texts),'outside_text':bad})

def laser(d,x,y,s=1):
    d.rect(x-8*s,y-8*s,16*s,16*s,stroke=NAVY,fill='white')
    for k in range(8):
        a=k*pi/4;d.line(x-4*s*cos(a),y-4*s*sin(a),x+4*s*cos(a),y+4*s*sin(a),GREEN,.65)
    d.line(x+4*s,y,x+8*s,y,GREEN,.85)
def mod(d,x,y):
    d.poly([(x-12,y-6),(x-6,y-10),(x+6,y-10),(x+12,y-6),(x+12,y+6),(x+6,y+10),(x-6,y+10),(x-12,y+6)],NAVY,.85,'white',True)
    d.poly([(x-9,y),(x-4,y-4),(x+4,y-4),(x+9,y)],NAVY,.7)
    d.poly([(x-9,y),(x-4,y+4),(x+4,y+4),(x+9,y)],NAVY,.7)
def diode(d,x,y,s=1):
    d.ellipse(x,y,10*s,color=NAVY,fill='white')
    d.poly([(x-5*s,y-5*s),(x+3*s,y),(x-5*s,y+5*s)],NAVY,.85,close=True)
    d.line(x+3*s,y-5*s,x+3*s,y+5*s,NAVY,.85)
    d.line(x-9*s,y,x-5*s,y,NAVY,.8);d.line(x+3*s,y,x+9*s,y,NAVY,.8)
    d.arrow(x-5*s,y-15*s,x-1*s,y-10*s,BLUE,.55,head=2.5*s)
    d.arrow(x+1*s,y-16*s,x+5*s,y-11*s,BLUE,.55,head=2.5*s)
def chip(d,x,y,s=1):
    d.rect(x-8*s,y-8*s,16*s,16*s,stroke=NAVY,fill='white');d.rect(x-4*s,y-4*s,8*s,8*s,stroke=NAVY)
    for z in [-5,0,5]:
        d.line(x+z*s,y-11*s,x+z*s,y-8*s,NAVY,.6);d.line(x+z*s,y+8*s,x+z*s,y+11*s,NAVY,.6)
        d.line(x-11*s,y+z*s,x-8*s,y+z*s,NAVY,.6);d.line(x+8*s,y+z*s,x+11*s,y+z*s,NAVY,.6)
def data(d,x,y,s=1):
    d.poly([(x-7*s,y-10*s),(x+3*s,y-10*s),(x+8*s,y-5*s),(x+8*s,y+10*s),(x-7*s,y+10*s)],NAVY,.75,'white',True)
    d.poly([(x+3*s,y-10*s),(x+3*s,y-5*s),(x+8*s,y-5*s)],NAVY,.65)
    d.text(x-4.5*s,y, '01',7.5*s,BLUE);d.text(x-4.5*s,y+7*s,'10',7.5*s,BLUE)
def target(d,x,y,s=1):
    d.ellipse(x,y,7*s,color=GREEN,width=.9);d.ellipse(x,y,2*s,color=GREEN,width=.75)
    for a in [0,pi/2,pi,3*pi/2]:d.line(x+9*s*cos(a),y+9*s*sin(a),x+13*s*cos(a),y+13*s*sin(a),GREEN,.85)
def antenna(d,x,y,s=1):
    d.poly([(x-7*s,y+11*s),(x,y-6*s),(x+7*s,y+11*s)],NAVY,.9)
    d.line(x-4*s,y+4*s,x+4*s,y+4*s,NAVY,.6)
    d.ellipse(x,y-8*s,1.4*s,color=NAVY,fill=NAVY)
    for r in [6,10]:
        for side in [-1,1]:
            pts=[(x+side*r*s*cos(a),y-8*s+r*s*sin(a)) for a in [-.75,-.4,0,.4,.75]]
            d.poly(pts,BLUE,.75)
def wave(d,x,y,w=28,color=GREEN):
    d.poly([(x+i*w/24,y-4*sin(i*pi/6)) for i in range(25)],color,.8)

def paths():
    d=Drawing('paths',358)
    d.text(0,12,'(a) Optical propagation and observation',9.5,NAVY,True)
    d.text(18,36,'Optical transmitter',8.3,NAVY,True)
    d.text(157,36,'Alternative physical paths',8.3,NAVY,True)
    d.text(334,36,'Alternative receiver paths',8.3,NAVY,True)
    laser(d,25,88);mod(d,71,88);d.arrow(33,88,59,88,GREEN)
    d.text(25,113,'Laser',8,anchor='middle');d.text(71,113,'Modulator',8,anchor='middle')
    d.text(25,56,'Data',8,BLUE,anchor='middle');d.path([(39,53),(71,53),(71,77)],NAVY)
    d.arrow(83,88,131,88,GREEN);d.marker(106,88);d.multi(106,62,['Launch','power'],7.5,AMBER,anchor='middle',leading=9)
    # Fiber branch and a disturbance waveform identify distributed observation.
    d.path([(131,88),(131,70),(155,70)],GREEN)
    for x in [161,166,171,176,181,186]:d.ellipse(x,70,3.4,10,GREEN,.7)
    d.line(155,70,157,70,GREEN);d.path([(190,70),(231,70),(231,88)],GREEN)
    d.text(178,54,'Fiber',8,NAVY,anchor='middle');wave(d,195,56,24,AMBER)
    d.path([(131,88),(131,115),(155,115)],GREEN)
    d.ellipse(161,115,3,11,GREEN,.8);d.ellipse(194,115,3,11,GREEN,.8)
    d.line(164,115,191,115,GREEN,.8);d.path([(197,115),(231,115),(231,88)],GREEN)
    d.text(180,138,'Free-space / illuminated scene',7.5,NAVY,anchor='middle')
    d.arrow(231,88,294,88,GREEN);d.marker(250,88);d.marker(278,88)
    d.multi(250,64,['Received','power'],7.5,AMBER,anchor='middle',leading=9)
    d.text(278,106,'OSNR*',7.5,AMBER,anchor='middle')
    # Direct detector and coherent option are alternative valid receive branches.
    d.path([(294,88),(294,66),(326,66)],GREEN);diode(d,336,66)
    d.text(336,50,'Direct detection',7.5,NAVY,anchor='middle')
    d.path([(346,66),(380,66),(380,88)],NAVY)
    d.path([(294,88),(307,88),(307,119),(317,119)],GREEN)
    d.ellipse(324,119,7,color=GREEN,fill='white');d.line(320,115,328,123,GREEN,.7);d.line(320,123,328,115,GREEN,.7)
    laser(d,293,151,.8);d.path([(299.5,151),(324,151),(324,126)],GREEN)
    d.text(275,165,'Local oscillator',7.5,NAVY)
    d.arrow(331,119,346,119,GREEN);diode(d,356,119,.9);d.path([(365,119),(380,119),(380,88)],NAVY)
    d.multi(373,132,['Coherent option:', 'mixing +', 'photodetection'],7.5,NAVY,leading=9)
    d.arrow(380,88,389,88,NAVY);chip(d,400,88);d.text(400,109,'DSP',8,NAVY,anchor='middle')
    d.arrow(411,88,435,88,NAVY);d.marker(423,88);d.multi(424,55,['Electrical','SNR'],7.5,AMBER,anchor='middle',leading=9)
    d.path([(435,88),(447,88),(447,65),(471,65)],NAVY);d.marker(456,65);d.text(456,50,'BER',7.5,AMBER,anchor='middle');data(d,486,65)
    d.text(486,88,'Data',8,NAVY,anchor='middle')
    d.path([(447,88),(447,120),(472,120)],NAVY);target(d,486,120)
    d.multi(483,143,['Parameter','estimate'],8,NAVY,anchor='middle',leading=10)
    d.text(0,182,'Observations may use forward light, backscatter, reflections, or spatial intensity. *OSNR where applicable.',7.5,GRAY)
    d.line(0,193,516,193,LIGHT,.6)
    d.text(0,210,'(b) Photonic generation followed by RF propagation',9.5,NAVY,True)
    laser(d,25,261);mod(d,71,261);d.arrow(33,261,59,261,GREEN);d.arrow(83,261,119,261,GREEN)
    d.text(25,285,'Laser',8,NAVY,anchor='middle');d.text(71,285,'Modulator',8,NAVY,anchor='middle')
    d.text(25,235,'Data',8,BLUE,anchor='middle');d.path([(40,232),(71,232),(71,250)],NAVY)
    laser(d,89,307,.8);d.path([(95.5,307),(129,307),(129,272)],GREEN)
    d.text(49,326,'Optical reference tone',7.5,NAVY)
    diode(d,129,261);d.text(129,236,'Photomixing',7.5,NAVY,anchor='middle')
    d.arrow(139,261,168,261,BLUE);antenna(d,179,261)
    d.multi(179,286,['RF','transmitter'],7.5,NAVY,anchor='middle',leading=9)
    d.path([(190,261),(213,261),(213,235),(322,235)],BLUE)
    d.text(260,223,'Communication path',8,BLUE,anchor='middle');antenna(d,335,235)
    d.arrow(347,235,387,235,BLUE);chip(d,398,235);d.arrow(409,235,474,235,NAVY);data(d,486,235)
    d.text(398,257,'Receiver / DSP',7.5,NAVY,anchor='middle')
    d.path([(213,261),(213,304),(256,304)],BLUE,dash=True)
    # Vehicle target silhouette; return uses RF until receiver conversion.
    d.poly([(256,304),(260,298),(264,294),(275,294),(281,298),(286,299),(286,307),(256,307)],NAVY,.8,'white',True)
    d.ellipse(262,309,2,color=NAVY,fill='white');d.ellipse(281,309,2,color=NAVY,fill='white')
    d.arrow(286,304,322,304,BLUE,dash=True);antenna(d,335,304)
    d.arrow(347,304,387,304,BLUE);chip(d,398,304);d.arrow(409,304,473,304,NAVY);target(d,486,304)
    d.text(272,327,'Target interaction / echo',7.5,NAVY,anchor='middle')
    d.text(398,327,'Receiver / DSP',7.5,NAVY,anchor='middle');d.text(486,326,'Estimate',7.5,NAVY,anchor='middle')
    d.line(0,338,516,338,LIGHT,.6)
    for x,col,label in [(1,GREEN,'Optical'),(92,BLUE,'RF'),(155,NAVY,'Electrical / digital')]:
        d.arrow(x,349,x+21,349,col);d.text(x+26,352,label,8,INK)
    d.marker(333,349);d.text(341,352,'Measurement plane',8,INK)
    d.finish()

def sharing():
    d=Drawing('sharing',185)
    titles=['(a) Time allocation','(b) Frequency allocation','(c) Joint waveform']
    for k,title in enumerate(titles):
        off=k*174;d.text(off+1,12,title,9,NAVY,True)
        x=off+20;y=31;w=139;h=77
        d.rect(x,y,w,h,stroke=LIGHT,fill='white',width=.5)
        for j in range(1,4):d.line(x+j*w/4,y,x+j*w/4,y+h,LIGHT,.4);d.line(x,y+j*h/4,x+w,y+j*h/4,LIGHT,.4)
        d.arrow(x-3,y+h+4,x+w+3,y+h+4,NAVY,.7);d.arrow(x-3,y+h+4,x-3,y-4,NAVY,.7)
        d.text(x+w,125,'Time',7.5,NAVY,anchor='end');d.text(x-4,26,'Frequency',7.5,NAVY)
        if k==0:
            d.rect(x+2,y+2,65,h-4,stroke=BLUE,fill='#E9F3FA',width=.8)
            d.rect(x+72,y+2,65,h-4,stroke=GREEN,fill='#E8F4EE',width=.8)
            d.text(x+34,y+43,'C',12,BLUE,True,'middle');d.text(x+104,y+43,'S',12,GREEN,True,'middle')
            d.multi(off+88,141,['Time availability','is divided'],8.3,NAVY,anchor='middle',leading=10)
        elif k==1:
            d.rect(x+2,y+2,w-4,31,stroke=GREEN,fill='#E8F4EE',width=.8)
            d.rect(x+2,y+43,w-4,32,stroke=BLUE,fill='#E9F3FA',width=.8)
            d.text(x+w/2,y+23,'S',12,GREEN,True,'middle');d.text(x+w/2,y+66,'C',12,BLUE,True,'middle')
            d.text(x+w/2,y+40,'Guard band',7.5,GRAY,anchor='middle')
            d.multi(off+88,141,['Bandwidth','is divided'],8.3,NAVY,anchor='middle',leading=10)
        else:
            d.rect(x+2,y+2,w-4,h-4,stroke=PURPLE,fill='#F0ECF6',width=.8)
            d.text(x+w/2,y+36,'C + S',12,PURPLE,True,'middle');d.text(x+w/2,y+53,'One waveform',8,PURPLE,anchor='middle')
            d.multi(off+88,141,['Both tasks constrain','the waveform'],8.3,NAVY,anchor='middle',leading=10)
    d.line(0,158,516,158,LIGHT,.6)
    laser(d,11,173,.72);d.arrow(18,173,42,173,GREEN,.8);diode(d,51,173,.68)
    d.text(67,177,'Shared optical link',8,NAVY)
    d.text(174,177,'C: communication',8,BLUE);d.text(273,177,'S: sensing',8,GREEN)
    d.text(359,177,'Illustrative allocations',8,GRAY)
    d.finish()

def coupling():
    d=Drawing('coupling',240)
    d.text(0,12,'Two allocation costs and one feedback benefit',9.5,NAVY,True)
    for x,title in [(0,'Shared choice'),(175,'Physical or processing link'),(367,'Paired response')]:d.text(x,34,title,8.5,NAVY,True)
    rows=[
      (66,['More pilot','allocation'],['Fewer data subcarriers;','more known symbols'],['C: lower data fraction','S: pilot-error proxy changes']),
      (126,['Higher probe','power'],['Stronger sensed return;','inter-channel interference'],['C: higher BER','S: higher vibration SNR']),
      (186,['Sensing-guided','steering'],['Location estimate aligns','illumination to receiver'],['C: higher estimated rate','S: position feeds steering'])]
    for j,(y,left,mid,right) in enumerate(rows):
        if j:d.line(0,y-27,516,y-27,LIGHT,.5)
        if j==0:
            d.rect(1,y-10,29,20,stroke=NAVY,fill='white');d.rect(2,y-9,8,18,stroke=BLUE,fill='#E9F3FA');d.rect(12,y-9,6,18,stroke=GREEN,fill='#E8F4EE');d.rect(20,y-9,9,18,stroke=BLUE,fill='#E9F3FA')
        elif j==1:
            wave(d,1,y,28,GREEN);d.arrow(15,y+13,15,y-14,AMBER,.8)
        else:
            laser(d,8,y,.55);d.arrow(12.5,y,21,y,GREEN,.7)
            d.ellipse(24,y,2,9,GREEN,.8)
            d.arrow(26,y-2,36,y-8,GREEN,.7);d.arrow(26,y+2,36,y+8,GREEN,.7)
        d.multi(43,y-2,left,8.5,NAVY,True,leading=11)
        if j==0:d.text(43,y+23,'Fixed OFDM grid',7.5,GRAY)
        if j==1:d.multi(43,y+22,['Communication launch','power held fixed'],7.5,GRAY,leading=9)
        d.arrow(146,y,167,y,NAVY,.8)
        d.multi(178,y-3,mid,8.3,INK,leading=11)
        d.arrow(337,y,358,y,NAVY,.8)
        d.text(369,y-3,right[0],8.5,BLUE);d.text(369,y+10,right[1],8.5,GREEN)
    d.line(0,213,516,213,LIGHT,.6)
    d.multi(0,226,['Directions apply to the reported configurations, not pooled effects. The pilot-error proxy is not target error.',
                    'Position feeds steering; separate localization tests do not establish a joint accuracy gain.'],7.5,GRAY,leading=10)
    d.finish()

def validation():
    d=Drawing('validation',199)
    d.text(0,12,'(a) Highest reported validation setting',9,NAVY,True)
    d.text(0,28,'One setting per study; n = 206',8,GRAY)
    labels=['Simulation / numerical','Enhanced simulation / dataset','Laboratory / proof of concept','Controlled prototype','Field trial / deployment']
    vals=[32,18,78,66,12]
    x=155;scale=1.7
    for i,(lab,val) in enumerate(zip(labels,vals)):
        y=47+i*24;d.text(x-7,y+10,lab,8,INK,anchor='end')
        d.rect(x,y,val*scale,13,stroke=GREEN if i==4 else BLUE,fill=GREEN if i==4 else BLUE,width=.3)
        d.text(x+val*scale+5,y+10,str(val),8,INK,bold=True)
    d.line(x,166,x+80*scale,166,GRAY,.6)
    for v in [0,20,40,60,80]:
        d.line(x+v*scale,166,x+v*scale,169,GRAY,.6);d.text(x+v*scale,180,str(v),7.5,GRAY,anchor='middle')
    d.text(x+68,194,'Studies',8,INK,anchor='middle')
    d.line(313,4,313,182,LIGHT,.6)
    d.text(329,12,'(b) Field evidence, nested view',9,NAVY,True)
    d.rect(331,35,184,113,stroke=GREEN,fill='#F4F9F6',width=.9)
    d.text(342,54,'12 field / deployment studies',8.5,GREEN,True)
    d.rect(347,68,152,53,stroke=GREEN,fill='#E3F1E8',width=.8)
    d.text(423,88,'6 report outcomes',9,NAVY,True,'middle')
    d.text(423,102,'in both domains',9,NAVY,True,'middle')
    d.text(342,140,'Other field studies: 6',8,INK)
    d.multi(329,166,['Both-domain reporting does not', 'establish concurrent operation.'],8.2,GRAY,leading=11)
    d.finish()

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    paths();sharing();coupling();validation()
    (QA/'dimensions.json').write_text(json.dumps(DIMENSIONS,indent=2),encoding='utf8')
    print(json.dumps(DIMENSIONS,indent=2))
