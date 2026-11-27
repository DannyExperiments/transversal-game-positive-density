"""Render a rotating worked transversal with the two pairing links."""

import argparse
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BG = "#101c30"
PANEL = "#1b2e4b"
LIGHT = "#f5f8fd"
MUTED = "#cfdef2"
TEAL = "#78dcd1"
CORAL = "#ffac97"
COLUMNS = (1, 0, 3, 2)
REPLY_CELLS = ((0, 1), (1, 0))


def project(x, y, z, angle):
    x, z = x*cos(angle)+z*sin(angle), z*cos(angle)-x*sin(angle)
    tilt = .76 + .12 * cos(angle)
    y, z = y*cos(tilt)-z*sin(tilt), y*sin(tilt)+z*cos(tilt)
    size = 395/(5.55-z)
    return 223+size*x, 266-size*y, z


def tile_center(r, c):
    return .70*(c-1.5), .70*(r-1.5)


def frame(angle, title, label, value, body):
    image = Image.new("RGB", (880, 550), BG)
    draw = ImageDraw.Draw(image)
    draw.text((26,20),"Block a transversal by its pair",font=title,fill=LIGHT)
    draw.line((28,79,852,79),fill="#395375",width=2)
    draw.rounded_rectangle((27,105,413,424),radius=16,fill=PANEL)
    draw.rounded_rectangle((431,105,853,424),radius=16,fill=PANEL)
    draw.text((48,119),"Four-by-four board",font=label,fill=LIGHT)
    draw.text((454,119),"If X plays first",font=label,fill=LIGHT)
    tiles=[]
    for r in range(4):
        for c in range(4):
            x,z=tile_center(r,c)
            points=[project(x+dx,0,z+dz,angle)
                    for dx,dz in [(-.33,-.33),(-.33,.33),(.33,.33),(.33,-.33)]]
            fill="#34516d" if (r//2+c//2)%2==0 else "#253e5c"
            if COLUMNS[r]==c:
                fill="#42918b"
            if (r,c) in REPLY_CELLS:
                fill=CORAL if r==0 else TEAL
            tiles.append((sum(p[2] for p in points)/4,points,fill))
    for _, points, fill in sorted(tiles):
        draw.polygon([p[:2] for p in points],fill=fill,outline=BG,width=2)
    for r in (0,2):
        x,z=tile_center(r,COLUMNS[r])
        first=project(x,.16,z,angle)
        x,z=tile_center(r+1,COLUMNS[r+1])
        second=project(x,.16,z,angle)
        draw.line((first[:2],second[:2]),fill=LIGHT,width=3)
    for (r,c),symbol in zip(REPLY_CELLS,("X","O")):
        x,z=tile_center(r,c)
        xx,yy,_=project(x,.23,z,angle)
        draw.text((xx,yy),symbol,font=label,fill=BG,anchor="mm",stroke_width=2,stroke_fill=LIGHT)
    draw.text((455,191),"X takes (1, 2)",font=value,fill=CORAL)
    draw.text((455,258),"O takes (2, 1)",font=value,fill=TEAL)
    draw.text((455,348),"The pair is blocked",font=body,fill=LIGHT)
    draw.text((34,457),"The chosen transversal has two complete pairs.",font=body,fill=MUTED)
    draw.text((34,505),"Eight of the 24 transversals contain a pair.",font=body,fill=MUTED)
    return image


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font",default="DejaVuSans.ttf")
    parser.add_argument("--bold-font",default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output",type=Path,default=Path("visualization/paired-grid.gif"))
    args=parser.parse_args()
    fonts=tuple(ImageFont.truetype(font,size) for font,size in (
        (args.bold_font,42),(args.bold_font,32),(args.bold_font,42),(args.regular_font,30)
    ))
    frames=[frame(.55+i*tau/64,*fonts).quantize(colors=120,method=2) for i in range(64)]
    frames[0].save(args.output,save_all=True,append_images=frames[1:],duration=92,loop=0,disposal=2,optimize=True)


if __name__=="__main__":
    main()
