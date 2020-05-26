import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
# rgb
# red = [1, 0, 0]
# black = [0, 0, 0]
# white = [1, 1, 1]
# blue = [0, 0, 1]
# cyan = [0, 1, 1]
# green = [0, 0.5, 0] 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# imread and imshow
def img01():
    fig, axes = plt.subplots(nrows=2, ncols=2)
    fig.suptitle("US map in colors", fontsize=20)

    usMap = plt.imread('usa_map.png')
    # turn blue to red
    usMap1 = np.zeros(shape=usMap.shape)
    usMap1[:][:][:] = usMap[:][:][:] 
    
    for i in range(0, usMap.shape[0]):
        for j in range(0, usMap.shape[1]):
            if usMap1[i][j][0]==0:
                usMap1[i][j][0] = 1.0
                usMap1[i][j][1] = 0.0
                usMap1[i][j][2] = 0.0
    # white space in the middle
    usMap2 = np.zeros(shape=usMap.shape)
    usMap2[:][:][:] = usMap[:][:][:] 
    for i in range(0, usMap.shape[0]):
        for j in range(0, usMap.shape[1]):
                if (i>usMap.shape[0]/3) and (i<=2*usMap.shape[0]/3) and\
                   (j>usMap.shape[1]/3) and (j<=2*usMap.shape[1]/3):
                    usMap2[i][j][0] = 1.
                    usMap2[i][j][1] = 1
                    usMap2[i][j][2] = 1.
                    usMap2[i][j][3] = 1.
    # reduce size of usMap
    new_length = usMap.shape[0]/2-1
    new_width = usMap.shape[1]/2-1
    usMap3 = np.zeros([new_length, new_width, 4])
    for i in range(0, new_length):
        for j in range(0, new_width):
            for k in range(0,3):
                usMap3[i][j][k] =  0.25*(usMap[2*i][2*j][k] + usMap[2*i+1][2*j][k]\
                                         + usMap[2*i][2*j+1][k] + usMap[2*i+1][2*j+1][k])
            usMap3[i][j][3] = 1

    axes[0][0].imshow(usMap)
    axes[0][1].imshow(usMap1, alpha=0.8)
    axes[1][0].imshow(usMap2, alpha=0.8)
    axes[1][1].imshow(usMap3)
    axes[0][1].axis('off')
    axes[1][0].axis('off')
    fig.tight_layout()
    plt.show()
    fig.savefig("img01.png", dpi=200, orientation='landscape', facecolor='yellow', \
                bbox_inches = 'tight')
    return usMap
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# rgb example
def img02():
    fig = plt.figure(facecolor=[1,1,1], edgecolor=[0.5, 0.5, 0.5]) # white, grey
    ax = plt.gca()
    M = np.zeros([4, 4, 3])
    #M[0][0][:] = np.array([0, 0, 0]) # black
    M[0][0][:] = np.array([1, 0, 0]) # red
    M[0][1][:] = np.array([1, 1, 0]) # yellow
    M[0][2][:] = np.array([0, 0, 1]) # blue
    M[0][3][:] = np.array([0, 0.5, 0]) #green
    M[1][0][:] = np.array([1, 99./255, 71./255]) #tomato
    M[1][1][:] = np.array([1, 165.0/255, 0]) #orange
    M[1][2][:] = np.array([0, 1, 1]) #cyan
    M[1][3][:] = np.array([0, 1, 0]) #lime
    M[2][0][:] = np.array([1, 192./255, 203./255]) #pink
    M[2][1][:] = np.array([1, 215./255, 0]) #gold
    M[2][2][:] = np.array([135./255, 206./255, 235./255]) #sky blue
    M[2][3][:] = np.array([1, 250./255, 205./255]) #lemonchiffon
    M[3][0][:] = np.array([238./255, 130./255, 238./255]) #violet
    M[3][1][:] = np.array([165./255, 42./255, 42./255]) #brown
    M[3][2][:] = np.array([0.5, 0, 0.5]) #purple
    M[3][3][:] = np.array([192./255, 192./255, 192./255]) #silver
    #M[3][3][:] = np.array([1, 1, 1]) #white
    ax.imshow(M, interpolation='none')
    ax.axis('off')
    # fig.savefig("img02.png", dpi=200, orientation='landscape', bbox_inches = 'tight')
    plt.show()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# image turn to grayscale
def img03():
    fig = plt.figure()
    ax = plt.gca()
    #img = plt.imread('microwave_oven.png')
    img = plt.imread("General_Relativity_Astrophysics_and_Cosmology_mini.png")
    img01 = np.zeros(shape=(img.shape[0], img.shape[1]))
    img01[:][:] = img[:, :, 0]
    ax.imshow(img01, cmap=plt.cm.gray) #in grayscale
    ax.axis('off')
    fig.savefig("General_Relativity_Astrophysics_and_Cosmology_sold.png", \
                transparent=True, facecolor='none', format="png")
    plt.show()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def img04(name):
    fig = plt.figure()
    ax = plt.gca()
    fileName = name + ".png"
    img = plt.imread(fileName)
    length = img.shape[0]/4-1
    width = img.shape[1]/4-1
    img02 = np.zeros([length, width, 3])
    for j in range(0,length):
        for k in range(0, width):
            img02[j, k, 0] = img[4*j, 4*k, 0]
            img02[j, k, 1] = img[4*j, 4*k, 1]
            img02[j, k, 2] = img[4*j, 4*k, 2]
    ax.imshow(img02)
    ax.axis('off')
    newName = name + "_mini.png"
    fig.savefig(newName, transparent=True, facecolor='none', format="png")
    plt.show()

# # # # # # # # # # # # # # # # # # # # MAIN # # # # # # # # # # # # # # # # # # # #
# usMap = img01()
# img02()
img03()



# # # # #
