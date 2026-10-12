"""Report exact saved RGB differences outside the complete accepted mask support.

Example: python check_outside_pixels.py original.png composite.png accepted_mask.png
The mask must be the actual full-resolution mask used by the final compositor,
with white meaning replacement. This script does not resize or edit any file.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from PIL import Image


def digest(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()


def check(original,composite,mask):
    with Image.open(original) as im:a=np.asarray(im.convert('RGB'),dtype=np.int16)
    with Image.open(composite) as im:b=np.asarray(im.convert('RGB'),dtype=np.int16)
    with Image.open(mask) as im:
        # The MaskToImage output stores the selection in each RGB channel.
        m=np.asarray(im.convert('RGB'))[:,:,0]
    if a.shape!=b.shape or a.shape[:2]!=m.shape:
        raise ValueError(f'Image/mask dimensions differ: {a.shape}, {b.shape}, {m.shape}; do not silently resize the evidence.')
    outside=m==0
    if not outside.any():raise ValueError('No outside pixels: this mask cannot establish outside preservation.')
    diff=np.abs(a-b)
    maximum=int(diff[outside].max())
    return {'status':'pass' if maximum==0 else 'different','dimensions':[a.shape[1],a.shape[0]],
            'outside_pixels':int(outside.sum()),'changed_outside_pixels':int(np.any(diff>0,axis=2)[outside].sum()),
            'outside_max_channel_difference_8bit':maximum,
            'basis':'Saved 8-bit RGB pixels where the supplied mask red channel is exactly zero; all nonzero soft-mask pixels are excluded.',
            'inputs':{str(p):digest(p) for p in (original,composite,mask)}}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('original','composite','mask'):ap.add_argument(name,type=Path)
    ap.add_argument('--out',type=Path)
    args=ap.parse_args();result=check(args.original,args.composite,args.mask)
    text=json.dumps(result,indent=2)
    if args.out:args.out.write_text(text+'\n',encoding='utf8')
    print(text)
    raise SystemExit(0 if result['status']=='pass' else 1)
