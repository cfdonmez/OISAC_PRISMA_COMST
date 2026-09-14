from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

qa = Path(__file__).resolve().parent
pages = sorted(qa.glob('page-*.png'))
for start in range(0, len(pages), 6):
    group = pages[start:start+6]
    sheet = Image.new('RGB', (1275, 1140), '#dddddd')
    draw = ImageDraw.Draw(sheet)
    for k, path in enumerate(group):
        im = Image.open(path).convert('RGB')
        im.thumbnail((417, 540))
        x, y = (k % 3)*425 + 4, (k // 3)*570 + 24
        sheet.paste(im, (x, y))
        draw.text((x+8, y-18), path.stem, fill='black')
    sheet.save(qa / f'sheet-{start//6+1}.png')
print(f'{len(pages)} rendered pages; {(len(pages)+5)//6} contact sheets')
