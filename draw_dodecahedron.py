import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm #colormap
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import sympy
from numpy import linalg as la

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def dodecahedron():
    def spherical_coords(phi, theta):
        x0 = math.cos(theta)*math.sin(phi)
        y0 = math.sin(theta)*math.sin(phi)
        z0 = math.cos(phi)
        return [x0, y0, z0]
    # a = 0.5 # to be determined
    a = 0.713644
    b = a*math.sin(3*math.pi/10)/math.sin(2*math.pi/5)
    h = math.sqrt(1-b**2)
    p1 = np.array([b, 0, -h])
    p2 = np.array([b*math.cos(2*math.pi/5), b*math.sin(2*math.pi/5), -h])
    p3 = np.array([b*math.cos(4*math.pi/5), b*math.sin(4*math.pi/5), -h])
    p4 = np.array([b*math.cos(6*math.pi/5), b*math.sin(6*math.pi/5), -h])
    p5 = np.array([b*math.cos(8*math.pi/5), b*math.sin(8*math.pi/5), -h])
    # Plane 1: tangent to S2 at p1. <(x,y,z)-p1, p1> = 0
    # q2, q3 = projection of p2, p5 on Plane 1
    # q2 = p2 + lam2*p1 s.t. <p1,p2> + lam2 = 1
    # lam2 = 1-<p1,p2>
    lam2 = 1.0-np.dot(p1,p2)
    q2 = p2 + lam2*p1
    lam3 = 1.0-np.dot(p1,p5)
    q3 = p5 + lam3*p1
    # create p6 p7 p8 p9 p10
    q6 = p1 + (p1-1/2*q2-1/2*q3)/la.norm(p1-1/2*q2-1/2*q3)*la.norm(p1-q2)
    k6vec = [np.dot(p1,p1), 2*np.dot(q6,p1), np.dot(q6,q6)-1]
    k6 = (-k6vec[1] + math.sqrt(k6vec[1]**2-4*k6vec[0]*k6vec[2]))/(2*k6vec[0])
    p6 = q6 + k6*p1
    #
    p21 = p1 + (1-np.dot(p2,p1))*p2
    p23 = p3 + (1-np.dot(p2,p3))*p2
    q7 = p2 + (p2-1/2*p21-1/2*p23)/la.norm(p2-1/2*p21-1/2*p23)\
         *la.norm(p2-p21)
    k7vec = [np.dot(p2,p2), 2*np.dot(q7,p2), np.dot(q7,q7)-1]
    k7 = (-k7vec[1] + math.sqrt(k7vec[1]**2-4*k7vec[0]*k7vec[2]))/(2*k7vec[0])
    p7 = q7 + k7*p2
    #
    p32 = p2 + (1-np.dot(p3,p2))*p3
    p34 = p4 + (1-np.dot(p3,p4))*p3
    q8 = p3 + (p3-1/2*p32-1/2*p34)/la.norm(p3-1/2*p32-1/2*p34)\
         *la.norm(p3-p32)
    k8vec = [np.dot(p3,p3), 2*np.dot(q8,p3), np.dot(q8,q8)-1]
    k8 = (-k8vec[1] + math.sqrt(k8vec[1]**2-4*k8vec[0]*k8vec[2]))/(2*k8vec[0])
    p8 = q8 + k8*p3
    #
    p43 = p3 + (1-np.dot(p4,p3))*p4
    p45 = p5 + (1-np.dot(p4,p5))*p4
    q9 = p4 + (p4-1/2*p43-1/2*p45)/la.norm(p4-1/2*p43-1/2*p45)\
         *la.norm(p4-p43)
    k9vec = [np.dot(p4,p4), 2*np.dot(q9,p4), np.dot(q9,q9)-1]
    k9 = (-k9vec[1] + math.sqrt(k9vec[1]**2-4*k9vec[0]*k9vec[2]))/(2*k9vec[0])
    p9 = q9 + k9*p4
    #
    p54 = p4 + (1-np.dot(p5,p4))*p5
    p51 = p1 + (1-np.dot(p5,p1))*p5
    q10 = p5 + (p5-1/2*p54-1/2*p51)/la.norm(p5-1/2*p54-1/2*p51)\
         *la.norm(p5-p54)
    k10vec = [np.dot(p5,p5), 2*np.dot(q10,p5), np.dot(q10,q10)-1]
    k10 = (-k10vec[1] + math.sqrt(k10vec[1]**2-4*k10vec[0]*k10vec[2]))/(2*k10vec[0])
    p10 = q10 + k10*p5
    # create p11 p12 p13 p14 p15
    phi1 = math.acos(-h)
    c = a*math.sqrt(7.0/4 - 2*math.cos(3*math.pi/5))
    d = math.sqrt(1-a**2/4)
    phi2 = math.acos((1+d**2-c**2)/(2*d))

    p11 = np.array(spherical_coords(phi1-phi2, math.pi/5))
    p12 = np.array(spherical_coords(phi1-phi2, 3*math.pi/5))
    p13 = np.array(spherical_coords(phi1-phi2, 5*math.pi/5))
    p14 = np.array(spherical_coords(phi1-phi2, 7*math.pi/5))
    p15 = np.array(spherical_coords(phi1-phi2, 9*math.pi/5))

    # create p16 p17 p18 p19 p20
    p116 = p6 + (1-np.dot(p11,p6))*p11
    p117 = p7 + (1-np.dot(p11,p7))*p11
    q16 = p11 + (p11-1/2*p116-1/2*p117)/la.norm(p11-1/2*p116-1/2*p117)*la.norm(p11-p116)
    k16vec = [np.dot(p11,p11), 2*np.dot(q16,p11), np.dot(q16,q16)-1]
    k16 = (-k16vec[1] + math.sqrt(k16vec[1]**2-4*k16vec[0]*k16vec[2]))/(2*k16vec[0])
    p16 = q16 + k16*p11

    p127 = p7 + (1-np.dot(p12,p7))*p12
    p128 = p8 + (1-np.dot(p12,p8))*p12
    q17 = p12 + (p12-1/2*p127-1/2*p128)/la.norm(p12-1/2*p127-1/2*p128)*la.norm(p12-p127)
    k17vec = [np.dot(p12,p12), 2*np.dot(q17,p12), np.dot(q17,q17)-1]
    k17 = (-k17vec[1] + math.sqrt(k17vec[1]**2-4*k17vec[0]*k17vec[2]))/(2*k17vec[0])
    p17 = q17 + k17*p12

    p138 = p8 + (1-np.dot(p13,p8))*p13
    p139 = p9 + (1-np.dot(p13,p9))*p13
    q18 = p13 + (p13-1/2*p138-1/2*p139)/la.norm(p13-1/2*p138-1/2*p139)*la.norm(p13-p138)
    k18vec = [np.dot(p13,p13), 2*np.dot(q18,p13), np.dot(q18,q18)-1]
    k18 = (-k18vec[1] + math.sqrt(k18vec[1]**2-4*k18vec[0]*k18vec[2]))/(2*k18vec[0])
    p18 = q18 + k18*p13
    
    p149 = p9 + (1-np.dot(p14,p9))*p14
    p1410 = p10 + (1-np.dot(p14,p10))*p14
    q19 = p14 + (p14-1/2*p149-1/2*p1410)/la.norm(p14-1/2*p149-1/2*p1410)*la.norm(p14-p149)
    k19vec = [np.dot(p14,p14), 2*np.dot(q19,p14), np.dot(q19,q19)-1]
    k19 = (-k19vec[1] + math.sqrt(k19vec[1]**2-4*k19vec[0]*k19vec[2]))/(2*k19vec[0])
    p19 = q19 + k19*p14

    p1510 = p10 + (1-np.dot(p15,p10))*p15
    p156 = p6 + (1-np.dot(p15,p6))*p15
    q20 = p15 + (p15-1/2*p1510-1/2*p156)/la.norm(p15-1/2*p1510-1/2*p156)*la.norm(p15-p1510)
    k20vec = [np.dot(p15,p15), 2*np.dot(q20,p15), np.dot(q20,q20)-1]
    k20 = (-k20vec[1] + math.sqrt(k20vec[1]**2-4*k20vec[0]*k20vec[2]))/(2*k20vec[0])
    p20 = q20 + k20*p15
    
    # # # # # DRAW # # # # #
    fig = plt.figure()
    ax = plt.gca(projection='3d')
    x01 = [p1[0], p2[0], p3[0], p4[0], p5[0], p1[0]]
    y01 = [p1[1], p2[1], p3[1], p4[1], p5[1], p1[1]]
    z01 = [p1[2], p2[2], p3[2], p4[2], p5[2], p1[2]]

    x02 = [0, p1[0], 0, p2[0], 0, p3[0], 0, p4[0], 0, p5[0]]
    y02 = [0, p1[1], 0, p2[1], 0, p3[1], 0, p4[1], 0, p5[1]]
    z02 = [0, p1[2], 0, p2[2], 0, p3[2], 0, p4[2], 0, p5[2]]
    ax.plot(x01, y01, z01, linewidth=1.2, color='blue')
    ax.plot(x02, y02, z02, linewidth=0.7, color='red', linestyle='--')
    # # # # #
    phi0 = np.linspace(0, 2 * np.pi, 100)
    theta0 = np.linspace(0, np.pi, 100)
    xm = np.outer(np.cos(phi0), np.sin(theta0))
    ym = np.outer(np.sin(phi0), np.sin(theta0))
    zm = np.outer(np.ones(np.size(phi0)), np.cos(theta0))
    ax.plot_surface(xm, ym, zm, 
                    facecolor= None,
                    edgecolor='pink',
                    linewidth=0.1,
                    linestyle='--',
                    alpha=0.0)
    # # # # #
##    xv0 = np.arange(-1.0, 1.1, 0.2)
##    yv0 = np.arange(-1.0, 1.1, 0.2)
##    Xv0, Yv0 = np.meshgrid(xv0, yv0)
##    Zv0 = np.zeros(shape=Xv0.shape)
##    for i in range(Xv0.shape[0]):
##        for j in range(Xv0.shape[1]):
##            Zv0[i,j] = (b*Xv0[i,j]-1.0)/h
##    ax.plot_surface(Xv0, Yv0, Zv0,
##                    color= None,
##                    linewidth=0.5,
##                    linestyle='-',
##                    edgecolor= 'lime',
##                    alpha=0.0)
##    x03 = [p1[0], q2[0], q3[0], p1[0]]
##    y03 = [p1[1], q2[1], q3[1], p1[1]]
##    z03 = [p1[2], q2[2], q3[2], p1[2]]
##    ax.plot(x03, y03, z03, color='gold', linewidth=2.0)
    
##    ax.scatter3D(p1[0], p1[1], p1[2], s=100, color='gold')
    
    ax.plot([p1[0],p6[0]], [p1[1],p6[1]], [p1[2],p6[2]],
            linewidth=1.2, color='blue')
    ax.plot([p2[0],p7[0]], [p2[1],p7[1]], [p2[2],p7[2]],
            linewidth=1.2, color='blue')
    ax.plot([p3[0],p8[0]], [p3[1],p8[1]], [p3[2],p8[2]],
            linewidth=1.2, color='blue')
    ax.plot([p4[0],p9[0]], [p4[1],p9[1]], [p4[2],p9[2]],
            linewidth=1.2, color='blue')
    ax.plot([p5[0],p10[0]], [p5[1],p10[1]], [p5[2],p10[2]],
            linewidth=1.2, color='blue')

    x04 = [p6[0], p11[0], p7[0], p12[0], p8[0], p13[0], p9[0], p14[0], p10[0], p15[0], p6[0]]
    y04 = [p6[1], p11[1], p7[1], p12[1], p8[1], p13[1], p9[1], p14[1], p10[1], p15[1], p6[1]]
    z04 = [p6[2], p11[2], p7[2], p12[2], p8[2], p13[2], p9[2], p14[2], p10[2], p15[2], p6[2]]

    x05 = [p16[0], p17[0], p18[0], p19[0], p20[0], p16[0]]
    y05 = [p16[1], p17[1], p18[1], p19[1], p20[1], p16[1]]
    z05 = [p16[2], p17[2], p18[2], p19[2], p20[2], p16[2]]
    
    ax.plot(x04, y04, z04, linewidth=1.2, color='blue')
    ax.plot(x05, y05, z05, linewidth=1.2, color='green')
    ax.plot([p11[0], p16[0]], [p11[1], p16[1]], [p11[2], p16[2]],
            linewidth=1.2, color='green')
    ax.plot([p12[0], p17[0]], [p12[1], p17[1]], [p12[2], p17[2]],
            linewidth=1.2, color='green')
    ax.plot([p13[0], p18[0]], [p13[1], p18[1]], [p13[2], p18[2]],
            linewidth=1.2, color='green')
    ax.plot([p14[0], p19[0]], [p14[1], p19[1]], [p14[2], p19[2]],
            linewidth=1.2, color='green')
    ax.plot([p15[0], p20[0]], [p15[1], p20[1]], [p15[2], p20[2]],
            linewidth=1.2, color='green')

    ax.set_xlim([-1.35,1.35])
    ax.set_ylim([-1.35,1.35])
    ax.set_zlim([-1.0, 1.0])
    ax.set_xticks([-1.0, 0.0, 1.0])
    ax.set_yticks([-1.0, 0.0, 1.0])
    ax.set_zticks([-1.0, 0.0, 1.0])
    plt.show()
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def get_a_value():
    a0 = 1.2
    x = sympy.Symbol('x')
    b = x*math.sin(3*math.pi/10)/math.sin(2*math.pi/5)
    h = sympy.sqrt(1-b**2)
    P1 = np.array([b, 0, -h])
    #P2 = np.array([b*math.cos(2*math.pi/5), b*math.sin(2*math.pi/5), -h])
    #p5 = np.array([b*math.cos(8*math.pi/5), b*math.sin(8*math.pi/5), -h])
    lam2 = 1-(h**2+b**2*math.cos(2*math.pi/5))
    Q2 = [math.cos(2*math.pi/5)*b + lam2*b, \
          math.sin(2*math.pi/5)*b, \
          -h*(1+lam2)]
    lam3 = 1-(h**2+b**2*math.cos(8*math.pi/5))
    Q3 = [math.cos(8*math.pi/5)*b + lam3*b, \
          math.sin(8*math.pi/5)*b, \
          -h*(1+lam3)]
    ftop = np.dot(Q2-P1, Q3-P1)
    fbottom = sympy.sqrt(np.dot(Q2-P1,Q2-P1))*sympy.sqrt(np.dot(Q3-P1,Q3-P1))
    # ftop/fbottom = -1.0/2
    f = ftop + 1.0/2*fbottom 
    aSoln = sympy.nsolve(f, x, a0)
    return aSoln
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
