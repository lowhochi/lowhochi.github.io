from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from numpy import linalg as la

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def arc(r, theta1, theta2, N=100):
    h = (theta2-theta1)/N
    thetaArr = np.arange(theta1, theta2+h, h)
    xArr = np.zeros(len(thetaArr))
    yArr = np.zeros(len(thetaArr))
    for i in range(len(thetaArr)):
        xArr[i] = r*cos(thetaArr[i])
        yArr[i] = r*sin(thetaArr[i])
    return xArr, yArr

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def inscribedCircle(P0, P1, P2):
    # inscribed cricle in the triangle P0P1P2
    # P1,alpha1 and P2,alpha2 intersect at the inscribed center
    # radius = s
    vP1P2 = P2 - P1
    vP1P0 = P0 - P1
    vP2P0 = P0 - P2
    nP1P2 = np.array([-vP1P2[1], vP1P2[0]])
    lengthP0P1 = la.norm(vP1P0)
    lengthP0P2 = la.norm(vP2P0)
    lengthP1P2 = la.norm(vP1P2)
    # slopeP1P2 = (P2[1]-P1[1])/(P2[0]-P1[0])
    alpha1 = acos((lengthP0P1**2+lengthP1P2**2-lengthP0P2**2)/(2*lengthP0P1*lengthP1P2))
    alpha2 = acos((lengthP0P2**2+lengthP1P2**2-lengthP0P1**2)/(2*lengthP0P2*lengthP1P2))
    s = lengthP1P2*tan(alpha1/2)*tan(alpha2/2)/(tan(alpha1/2)+tan(alpha2/2))
    k1 = s/tan(alpha1/2)
    k2 = s/tan(alpha2/2)
    # # # # #
    iCenter = P1 + (k1/lengthP1P2)*vP1P2 + (s/la.norm(nP1P2))*nP1P2
    Q12 = P1 + (k1/lengthP1P2)*vP1P2
    Q01 = P1 + (k1/lengthP0P1)*vP1P0
    Q02 = P2 + (k2/lengthP0P2)*vP2P0

    if (Q02[0]==iCenter[0]):
        theta0 = pi/2
    else:
        theta0 = atan((Q02[1]-iCenter[1])/(Q02[0]-iCenter[0]))
    check0 = iCenter[0] + s*cos(theta0) - Q02[0]
    check1 = iCenter[1] + s*sin(theta0) - Q02[1]
    
    if (check0!=0) or (check1!=0):
        theta0 = pi + theta0
    
    iCircle = {"center": iCenter, \
               "radius" : s,
               "alpha1" : alpha1,
               "alpha2" : alpha2,
               "Q12": Q12, \
               "Q01": Q01, \
               "Q02": Q02, \
               "theta0": theta0, \
               "theta1": (theta0 + alpha1 + alpha2) }
    return iCircle

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def roundAngle01():
    fig = plt.figure()
    ax = fig.add_subplot(121)
    xs= [0, 1.0, 1.5, 1.0, 0.0, 0.0]
    ys = [0, 0.0, 1.0, 1.5, 1.0, 0.0]
    ax.plot(xs, ys, color='b', linewidth=1.5)
    # # # # #
    P0 = np.array([0.0, 1.0])
    P1 = np.array([0.0, 0.9])
    P2 = np.array([0.1, 1.05])
    xTri = [P0[0], P1[0], P2[0], P0[0]]
    yTri = [P0[1], P1[1], P2[1], P0[1]]
    #ax.plot(xTri, yTri, color='r', linestyle='--', linewidth=0.5)
    
    iCircle = inscribedCircle(P0, P1, P2)
    iCenter = iCircle["center"]
    s = iCircle["radius"]
    xArr, yArr = arc(s, 0, 2*pi)
    #ax.plot(iCenter[0]+xArr, iCenter[1]+yArr, color='r', linewidth=0.5)

    verts = list(zip(xs, ys))
    polys = Polygon(np.array(verts)) 
    polys.set_facecolor('yellow')
    polys.set_alpha(0.5)
    ax.add_patch(polys)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("sharp angle", fontsize=20)
    ax.axis('off')
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    Q01 = iCircle["Q01"]
    Q02 = iCircle["Q02"]
    Q12 = iCircle["Q12"]
    alpha1 = iCircle["alpha1"]
    alpha2 = iCircle["alpha2"]
    theta0 = iCircle["theta0"]
    theta1 = iCircle["theta1"]
    xArr2, yArr2 = arc(s, theta0, theta1)
    xlist2 = list(iCenter[0]+xArr2)[::-1]
    ylist2 = list(iCenter[1]+yArr2)[::-1]
    # # # # # # # # # #
    R0 = np.array([1, 1.5])
    R1 = np.array([0.9, 1.45])
    R2 = np.array([1.1, 1.4])
    Rcircle = inscribedCircle(R0, R1, R2)
    Rcenter = Rcircle["center"]
    rs = Rcircle["radius"]
    r01 = Rcircle["Q01"]
    r02 = Rcircle["Q02"]
    r12 = Rcircle["Q12"]
    rAlpha1 = Rcircle["alpha1"]
    rAlpha2 = Rcircle["alpha2"]
    rTheta0 = Rcircle["theta0"]
    rTheta1 = Rcircle["theta1"]

    xArr3, yArr3 = arc(rs, rTheta0, rTheta1)
    xlist3 = list(Rcenter[0]+xArr3)[::-1]
    ylist3 = list(Rcenter[1]+yArr3)[::-1]
    # # # # # # # # # #
    S0 = np.array([1.5, 1.0])
    S1 = np.array([1.4, 1.1])
    S2 = np.array([1.4, 0.8])
    Scircle = inscribedCircle(S0, S1, S2)
    Scenter = Scircle["center"]
    ss = Scircle["radius"]
    s01 = Scircle["Q01"]
    s02 = Scircle["Q02"]
    s12 = Scircle["Q12"]
    sAlpha1 = Scircle["alpha1"]
    sAlpha2 = Scircle["alpha2"]
    sTheta0 = Scircle["theta0"]
    sTheta1 = Scircle["theta1"]
    xArr4, yArr4 = arc(ss, sTheta0, sTheta1)
    xlist4 = list(Scenter[0]+xArr4)[::-1]
    ylist4 = list(Scenter[1]+yArr4)[::-1]
    
    # # # # # # # # # #
    T0 = np.array([1.0, 0.0])
    T1 = np.array([1.1, 0.2])
    T2 = np.array([0.9, 0.0])
    Tcircle = inscribedCircle(T0, T1, T2)
    Tcenter = Tcircle["center"]
    ts = Tcircle["radius"]
    t01 = Tcircle["Q01"]
    t02 = Tcircle["Q02"]
    t12 = Tcircle["Q12"]
    tAlpha1 = Tcircle["alpha1"]
    tAlpha2 = Tcircle["alpha2"]
    tTheta0 = Tcircle["theta0"]
    tTheta1 = Tcircle["theta1"]
    xArr5, yArr5 = arc(ts, tTheta0, tTheta1)
    xlist5 = list(Tcenter[0]+xArr5)[::-1]
    ylist5 = list(Tcenter[1]+yArr5)[::-1]

    # # # # # # # # # #
    U0 = np.array([0, 0])
    U1 = np.array([0.1, 0])
    U2 = np.array([0.0, 0.1])
    Ucircle = inscribedCircle(U0, U1, U2)
    Ucenter = Ucircle["center"]
    us = Ucircle["radius"]
    u01 = Ucircle["Q01"]
    u02 = Ucircle["Q02"]
    u12 = Ucircle["Q12"]
    uAlpha1 = Ucircle["alpha1"]
    uAlpha2 = Ucircle["alpha2"]
    uTheta0 = Ucircle["theta0"]
    uTheta1 = Ucircle["theta1"]
    xArr6, yArr6 = arc(us, uTheta0,uTheta1)
    xlist6 = list(Ucenter[0]+xArr6)[::-1]
    ylist6 = list(Ucenter[1]+yArr6)[::-1]              


    x1s = [u02[0], Q01[0], *xlist2, Q02[0], r01[0], *xlist3, r02[0], \
           s01[0], *xlist4, s02[0], t01[0], *xlist5, t02[0], \
           u01[0], *xlist6, u02[0]]

    y1s = [u02[1], Q01[1], *ylist2, Q02[1], r01[1], *ylist3, r02[1], \
           s01[1], *ylist4, s02[1], t01[1], *ylist5, t02[1], \
           u01[1], *ylist6, u02[1]]

    vert1s = list(zip(x1s, y1s))
    poly1s = Polygon(np.array(vert1s)) 
    poly1s.set_facecolor('lime')
    poly1s.set_alpha(0.5)

    axtwo = fig.add_subplot(122)
    axtwo.plot(x1s,  y1s, color='b', linewidth=1.5)
    axtwo.add_patch(poly1s)
    axtwo.set_aspect('equal', adjustable='box')
    axtwo.set_title("round angle", fontsize=20)
    axtwo.axis('off')
    plt.show()

roundAngle01()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
