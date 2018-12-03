import numpy as np

re = 2.8e-5 # classiacal electron radius 2.8e-5 A

def dsymaa(a):
    n, m = a.shape
    i, j = np.mgrid[:m,:m]
    idx = np.triu_indices(m, 0)
    
    return a[:,i[idx]] * a[:,j[idx]]


def dsymab(a, b):
    n, m = a.shape
    i, j = np.mgrid[:m,:m]
    idx = np.triu_indices(m, 0)
    i = i[idx]
    j = j[idx]
    
    return a[:,i] * b[:,j] + a[:,j] * b[:,i]

j1 = np.array([
    [4.49340945790906418, 2.46053557219039853],
    [7.72525183693770716, 6.02929238161457509],
    [10.9041216594288998, 9.26140192620464834],
    [14.0661939128314735, 12.4452597532120833],
    [17.2207552719307687, 15.6115852914514377],
    [20.3713029592875628, 18.7694688401628241],
    [23.5194524986890065, 21.9226193518347006],
    [26.6660542588126735, 25.0728441897943851],
    [29.8115987908929588, 28.2211321797148477],
    [32.9563890398224767, 31.368070766264539],
    [36.1006222443756107, 34.5140312445128805],
    [39.2444323611641928, 37.6592599403577472],
    [42.3879135681319199, 40.8039267708609718],
    [45.5311340139912798, 43.9481527704155214],
    [48.6741442319543871, 47.0920265062016135],
    [51.8169824872796695, 50.2356142895366224],
    [54.9596782878889359, 53.378966758577184],
    [58.1022547544955926, 56.5221232535956505],
    [61.2447302603744004, 59.6651148032279082],
    [64.3871195905574137, 62.8079662105857604],
        
])


def peaks(x):
    dx = x[1:] - x[:-1]
    i = np.where(dx[1:] * dx[:-1] < 0.)[0] + 1

    j = i[dx[i] < 0]
    i = i[dx[i] >= 0]
    
    nj = j.size
    ni = i.size
    
    if ni == 0 and nj == 0:
        f = x[0] > x[-1]
        i = np.array([f * dx.size])
        j = np.array([not f * dx.size])
    elif ni == 0:
        i = np.array([0, dx.size])
    elif nj == 0:
        j = np.array([0, dx.size])
    else:
        if i[0] > j[0]:
            i = np.concatenate([[0], i])
        else:
            j = np.concatenate([[0], j])
        if i[-1] < j[-1]:
            i = np.concatenate([i, [dx.size]])
        else:
            j = np.concatenate([j, [dx.size]])
    
    idx = np.argsort(x[i])
      
    return i, j, idx
