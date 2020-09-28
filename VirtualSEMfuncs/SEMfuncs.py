def adjust_focus(img, sig):
    import numpy as np
    from scipy import ndimage
    arr = np.asarray(img)
    arrlab = arr[890:,:,:3]
    arr = arr[:890,:,:3]
    newIm = ndimage.gaussian_filter(arr,sig)
    newIm = np.append(newIm, arrlab, axis=0)
    return(newIm)

def adjust_contrast(img,vmin, vmax):
    import numpy as np
    arr = np.asarray(img)
    arrlab = arr[890:,:,:3]
    arr = arr[:890,:,:3]
    pixMx = arr.max()
    pixMn = arr.min()
    LUT = np.zeros(256, dtype=np.uint8)
    LUT[pixMn:pixMx+1] = np.linspace(vmin,vmax,(pixMx-pixMn)+1, 
                                 endpoint=True, dtype=np.uint8)
    newIm = LUT[arr]
    newIm = np.append(newIm, arrlab, axis=0)
    return(newIm)