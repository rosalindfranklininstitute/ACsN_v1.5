# function [ score ] = metric( image_noisy,image_denoised )
# %     DENOISEIMGQUALITY A metric function that computes the image quality of
# %     a denoised image.
# %     ---------------------------------------------------------------------------------
# %     Input: noisy intensity image "image_noisy" and denoised image "image_denoised"
# %     Output: image quality score "score".
# %     ---------------------------------------------------------------------------------
# %     Code provided by Xiangfei Kong and Qingxiong Yang 
# %     Permission is granted for anyone to copy, use, modify, or distribute this program 
# %     and accompanying programs and documents for any purpose, provided this copyright 
# %     notice is retained and prominently displayed, along with a note saying that the 
# %     original programs are available from our web page. The programs and documents 
# %     are distributed without any warranty, express or implied. As the programs were 
# %     written for research purposes only, they have not been tested to the degree that 
# %     would be advisable in any important application. All use of these programs is 
# %     entirely at the user's own risk.


#     img_m = image_noisy - image_denoised;    %Compute the "Method Noise Image" (MNI)

#     [N] = SSIM(image_noisy,img_m);  %Compute the map of noise reduction measurement N (see Eq. 3 in the paper)

#     [P] = SSIM(image_noisy,image_denoised);  %Compute the map of Structure preservation measurement P (see Eq. 4 in the paper)

#     score = -corr(real(N(:)),real(P(:)),'type','Pearson'); %Compute linear correlation of N and P and normalize it as the quality score. final score ranges [-1,1]
# end

import numpy as np
# import minpy.numpy as np
from .SSIM import SSIM
from scipy.stats import pearsonr
from scipy.signal import convolve2d
from skimage.metrics import structural_similarity as ssim #could use this python function too
from numba import jit, njit
import time

def metric(image_noisy, image_denoised):
    
    img_m = image_noisy - image_denoised #Compute the "Method Noise Image"

    N = SSIM(image_noisy, img_m)

    P = SSIM(image_noisy, image_denoised)

    # To get rid of any inf or nan values that pop up
    N = np.nan_to_num(N)
    P = np.nan_to_num(P)

    #### Score calculation
    score = -pearsonr(N.flatten().real, P.flatten().real)[0]

    return score
