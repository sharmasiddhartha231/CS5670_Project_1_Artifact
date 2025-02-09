import sys
import cv2
import numpy as np

def cross_correlation_2d(img, kernel):
    '''Given a kernel of arbitrary m x n dimensions, with both m and n being
    odd, compute the cross correlation of the given image with the given
    kernel, such that the output is of the same dimensions as the image and that
    you assume the pixels out of the bounds of the image to be zero. Note that
    you need to apply the kernel to each channel separately, if the given image
    is an RGB image.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    k1,k2 = kernel.shape
    output_image = np.zeros(img.shape)
    p1 = int((k1 - 1)/2)
    p2 = int((k2 - 1)/2)

    ##For grayscale image
    if len(img.shape) == 2:
        height, width = img.shape
        ## Create new image array for padded image. Initial zero matrix is created with the dimensions of image plus kernel minus one. 
        ## Then the original image is placed in the center of the new image array. This allows there to be a layer of zeros surrounding the image.
        ## for example, for a 5 by 5 image and a 3 by 3 kernel, create a zero matrix of size 7 * 7. Then place the image in the center. This allows there to be a layer of zeros on each side of the image.
        ## The number of layers of zeros is defined by p1,p2 (half of kernel dimensions minus 1). 
        ## For 3 layer rgb image, do the same for each layer of image.
        input_image = np.zeros((height+k1-1,width+k2-1))
        input_image[p1:p1+height,p2:p2+width] = img
        ## Multiply the kernel by a matrix of same size while moving the kernel along the image array. Sum the matrix for the new cross correlation values.
        for i in range(0,height):
            for j in range(0,width):
                output_image[i,j] = np.sum(kernel * input_image[i:i+k1,j:j+k2])

    ## For rgb image
    if len(img.shape) == 3:
        height, width, depth = img.shape
        input_image = np.zeros((height+k1-1,width+k2-1,depth))
        for i in range(0,depth):
            input_image[p1:p1+height,p2:p2+width,i] = img[:,:,i]
        for j in range(0,height):
            for k in range(0,width):
                for i in range(0,depth):
                    output_image[j,k,i] = np.sum(kernel * input_image[j:j+k1,k:k+k2,i]) 

    return output_image
    #raise Exception("TODO in hybrid.py not implemented")
    # TODO-BLOCK-END

def convolve_2d(img, kernel):
    '''Use cross_correlation_2d() to carry out a 2D convolution.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    #kernel_flipped = np.flip(kernel)
    k = 0
    kernel_flipped = np.zeros(kernel.shape)
    k1,k2 = kernel.shape
    for i in range(k1):
        for j in range(k2):
            k = kernel[k1-1-i,k2-1-j]
            kernel_flipped[i,j] = k
            k = 0
    output_image = cross_correlation_2d(img,kernel_flipped)
    return output_image
    #raise Exception("TODO in hybrid.py not implemented")
    # TODO-BLOCK-END

def gaussian_blur_kernel_2d(sigma, height, width):
    '''Return a Gaussian blur kernel of the given dimensions and with the given
    sigma. Note that width and height are different.

    Input:
        sigma:  The parameter that controls the radius of the Gaussian blur.
                Note that, in our case, it is a circular Gaussian (symmetric
                across height and width).
        width:  The width of the kernel.
        height: The height of the kernel.

    Output:
        Return a kernel of dimensions height x width such that convolving it
        with an image results in a Gaussian-blurred image.
    '''
    # TODO-BLOCK-BEGIN
    kernel = np.zeros((height,width))
    #h_neg = -(height - 1)
    #w_neg = -(width - 1)
    #h_pos = (height + 1)
    #w_pos = (width + 1)
    #h_range = pow(np.arange(h_neg,h_pos,2),2)
    #w_range = pow(np.arange(w_neg,w_pos,2),2)

    ## Since the gaussian kernel is circularly symmetric, we split our x and y ranges (height and width) in a way that these arrays become symmetric about their midpoint.
    ## For example, for a 5*5 kernel, we define the ranges as [-2,-1,0,1,2] for both x and y. 
    ## By squaring these ranges, we ensure complete symmetry across the center or midpoint.
    ## Divide by sum of kernel to normalize kernel and sum the kernel to one. This is to ensure image brightness does not change.
    ## blur_kernel values end up being same when using constant value defined as 1/2pi(sigma^2) or root of that value. Is that due to the normalization step?
    h_neg = -(height - 1)/2
    w_neg = -(width - 1)/2
    h_pos = (height + 1)/2
    w_pos = (width + 1)/2
    h_range = np.arange(h_neg,h_pos,1)
    w_range = np.arange(w_neg,w_pos,1)
    #h_range = np.arange(-height,height+1,height/2)
    #w_range = np.arange(-width,width+1,width/2)
    const = 1/(2 * np.pi * pow(sigma,2))
    #const = 1/pow((2 * np.pi * pow(sigma,2)),0.5)
    for i in range(0,height):
        for j in range(0,width):
            x = h_range[i]
            y = w_range[j]
            exp_value = np.exp(-(pow(x,2) + pow(y,2))/(2 * pow(sigma,2)))
            g_value = const * exp_value
            kernel[i,j] = g_value
    norm_factor = np.sum(kernel)    
    blur_kernel = kernel / norm_factor
    return blur_kernel
    #raise Exception("TODO in hybrid.py not implemented")
    # TODO-BLOCK-END

def low_pass(img, sigma, size):
    '''Filter the image as if its filtered with a low pass filter of the given
    sigma and a square kernel of the given size. A low pass filter supresses
    the higher frequency components (finer details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    gaussian_kernel = gaussian_blur_kernel_2d(sigma, size, size)
    lowpass_image = convolve_2d(img, gaussian_kernel)
    return lowpass_image
    #raise Exception("TODO in hybrid.py not implemented")
    # TODO-BLOCK-END

def high_pass(img, sigma, size):
    '''Filter the image as if its filtered with a high pass filter of the given
    sigma and a square kernel of the given size. A high pass filter suppresses
    the lower frequency components (coarse details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    lowpass_image = low_pass(img,sigma,size)
    highpass_image = img - lowpass_image
    return highpass_image
    #raise Exception("TODO in hybrid.py not implemented")
    # TODO-BLOCK-END

def create_hybrid_image(img1, img2, sigma1, size1, high_low1, sigma2, size2,
        high_low2, mixin_ratio, scale_factor):
    '''This function adds two images to create a hybrid image, based on
    parameters specified by the user.'''
    high_low1 = high_low1.lower()
    high_low2 = high_low2.lower()

    if img1.dtype == np.uint8:
        img1 = img1.astype(np.float32) / 255.0
        img2 = img2.astype(np.float32) / 255.0

    if high_low1 == 'low':
        img1 = low_pass(img1, sigma1, size1)
    else:
        img1 = high_pass(img1, sigma1, size1)

    if high_low2 == 'low':
        img2 = low_pass(img2, sigma2, size2)
    else:
        img2 = high_pass(img2, sigma2, size2)

    img1 *=  (1 - mixin_ratio)
    img2 *= mixin_ratio
    hybrid_img = (img1 + img2) * scale_factor
    return (hybrid_img * 255).clip(0, 255).astype(np.uint8)

