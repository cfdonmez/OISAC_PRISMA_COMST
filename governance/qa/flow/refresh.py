"""Record the verified EOF-only rebuild and refresh exact-PDF previews."""
from pathlib import Path
import hashlib, json
from PIL import Image,ImageDraw,ImageChops
root=Path(__file__).resolve().parents[3]
paper=root/'governance/qa/flow/paper'
newsha=hashlib.sha256((root/'manuscript/main.pdf').read_bytes()).hexdigest()
changed=[]
for i,p in enumerate(sorted((root/'tmp/final').glob('p-*.png')),1):
    old=paper/f'page-{i:02d}.png'
    if ImageChops.difference(Image.open(p).convert('RGB'),Image.open(old).convert('RGB')).getbbox():
        changed.append(i)
    old.write_bytes(p.read_bytes())
assert changed==[2], changed
for group in range(4):
    board=Image.new('RGB',(1290,1150),'#dddddd')
    d=ImageDraw.Draw(board)
    for j in range(6):
        n=group*6+j+1
        if n>20: break
        x=(j%3)*430; y=(j//3)*575
        page=Image.open(paper/f'page-{n:02d}.png').convert('RGB')
        page.thumbnail((420,544))
        board.paste(page,(x+5,y+25))
        d.text((x+6,y+7),f'Page {n}',fill='black')
    board.save(paper/f'sheet-{group+1}.png')
p=paper/'visual_checks.json'; v=json.loads(p.read_text())
oldsha=v['pdf_sha256']; v['pdf_sha256']=newsha
v['detailed_visual_pages']=sorted(set(v['detailed_visual_pages']+[2]))
v['last_rebuild']={'previous_sha256':oldsha,'reason':'Remove one trailing blank line in Introduction',
                   'pixel_identical_pages':19,'changed_pages':[2],
                   'changed_page_visually_rechecked':True,'clipping_or_collision':False}
p.write_bytes(json.dumps(v,indent=2).encode())
p=paper/'page_map.json'; v=json.loads(p.read_text());v['pdf_sha256']=newsha
p.write_bytes(json.dumps(v,indent=2).encode())
p=paper/'visual.md'; s=p.read_text(encoding='utf-8').replace(oldsha,newsha)
s+='\nFinal EOF-only rebuild: 19 pages pixel-identical at 110 dpi; page 2 re-inspected with no clipping, collision or poor heading placement. Contact sheets and page renders match the final PDF.\n'
p.write_bytes(s.encode('utf-8'))
print(json.dumps({'final_pdf_sha256':newsha,'pixel_identical_pages':19,'rechecked_pages':[2]}))
