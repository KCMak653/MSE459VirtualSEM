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

def get_values():
    sampNames = ['Alpha A.R', 'Sulzer A.R', 'Alpha Dry', 'Sulzer Dry', 'Alpha Wet', 'Sulzer Wet']
    hints = ['Hint 1: Although we would expect the particle size to decrease after ball milling, the same may not be true for particle size',
            'Hint 2: Look at the EDS - For which milling condition do we expect there to be more contamination?',
                'Hint 3: What is the key difference between Sulzer and Alpha - how could this affect contamination levels?']
    answTxt ='Correct answers are shown in red above.  \nYour password to access the SEM images and EDS spectra is: SPEX'
    answKey = ['D', 'C', 'F', 'B', 'A', 'E']
    
    return(hints, sampNames, answTxt, answKey)