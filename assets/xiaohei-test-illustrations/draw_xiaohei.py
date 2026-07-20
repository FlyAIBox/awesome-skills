# -*- coding: utf-8 -*-
# Ian xiaohei style illustration: premature "done" declaration
# 16:9, pure white bg, black wobbly hand-drawn lines, sparse red annotations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import numpy as np

zh = fm.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')

BLACK = '#141414'
RED = '#d0342c'

plt.xkcd(scale=1.2, length=120, randomness=2)

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 1600)
ax.set_ylim(0, 900)
ax.invert_yaxis()
ax.axis('off')

lw_main = 2.6
lw_thin = 1.8

def line(xs, ys, lw=lw_main, color=BLACK, alpha=1.0):
    ax.plot(xs, ys, lw=lw, color=color, alpha=alpha, solid_capstyle='round')

# ground
line([440, 1380], [703, 701], lw=1.6, alpha=0.5)

# mailbox (已完成)
t = np.linspace(np.pi, 0, 40)
arch_x = 592 + 88*np.cos(t)
arch_y = 448 - 62*np.sin(t)
line(arch_x, arch_y)
line([504, 505], [448, 642])
line([680, 681], [448, 640])
line([505, 681], [643, 641])
line([506, 679], [470, 468], lw=lw_thin)
line([534, 533], [644, 700])
line([650, 650], [643, 700])
line([521, 547], [701, 701], lw=lw_thin)
line([637, 663], [701, 701], lw=lw_thin)
slot = mpatches.FancyBboxPatch((648, 500), 44, 16,
        boxstyle="round,pad=1.5,rounding_size=6", fc=BLACK, ec=BLACK)
ax.add_patch(slot)
ax.text(592, 566, '已完成', fontproperties=zh, fontsize=30, color=BLACK,
        ha='center', va='center')

# papers going into slot (ink wet)
def sheet(cx, cy, w, h, ang):
    a = np.deg2rad(ang)
    dx, dy = np.cos(a), np.sin(a)
    px, py = -np.sin(a), np.cos(a)
    corners = []
    for sx, sy in [(-w/2,-h/2),(w/2,-h/2),(w/2,h/2),(-w/2,h/2),(-w/2,-h/2)]:
        corners.append((cx + sx*dx + sy*px, cy + sx*dy + sy*py))
    xs, ys = zip(*corners)
    line(xs, ys, lw=lw_thin)
    for k in (-0.22, 0.02, 0.26):
        x1 = cx + (-w*0.32)*dx + (h*k)*px
        y1 = cy + (-w*0.32)*dy + (h*k)*py
        x2 = cx + (w*0.30)*dx + (h*k)*px
        y2 = cy + (w*0.30)*dy + (h*k)*py
        line([x1, x2], [y1, y2], lw=1.3, alpha=0.75)

sheet(750, 520, 105, 46, -16)
sheet(776, 546, 100, 42, -9)

for (dx0, dy0, s) in [(742, 576, 1.0), (782, 586, 1.2), (814, 572, 0.8)]:
    drop = mpatches.Ellipse((dx0, dy0+10*s), 9*s, 16*s, fc=BLACK, ec=BLACK)
    ax.add_patch(drop)
    line([dx0, dx0], [dy0-6, dy0+2], lw=1.4)

# 小黑
theta = np.linspace(0, 2*np.pi, 60)
rx = 50 + 6*np.sin(3*theta) + 3*np.cos(5*theta)
ry = 60 + 5*np.cos(2*theta) + 3*np.sin(4*theta)
bx = 872 + rx*np.cos(theta)
by = 616 + ry*np.sin(theta)
ax.fill(bx, by, color=BLACK, zorder=5)
ax.add_patch(mpatches.Circle((856, 596), 6.5, fc='white', ec='white', zorder=6))
ax.add_patch(mpatches.Circle((888, 593), 6.5, fc='white', ec='white', zorder=6))
line([834, 800, 772], [588, 566, 544])
line([830, 792, 760], [618, 598, 572])
line([852, 850], [674, 701])
line([890, 892], [673, 701])
line([840, 862], [702, 702], lw=lw_thin)
line([880, 902], [702, 702], lw=lw_thin)

ax.text(920, 500, '搞定了？', fontproperties=zh, fontsize=28, color=RED)
line([916, 902], [522, 552], lw=1.6, color=RED)

# sealed untouched box (测试)
line([1128, 1318], [568, 562])
line([1128, 1132], [568, 693])
line([1318, 1320], [562, 688])
line([1132, 1320], [693, 688])
line([1130, 1317], [594, 588], lw=lw_thin)
line([1196, 1198], [564, 590], lw=lw_thin)
line([1252, 1251], [563, 589], lw=lw_thin)
line([1196, 1252], [577, 575], lw=lw_thin)
ax.text(1224, 650, '测试', fontproperties=zh, fontsize=30, color=BLACK,
        ha='center', va='center')
for (mx, my) in [(1110, 546), (1338, 550), (1124, 534)]:
    line([mx, mx+4, mx+8], [my, my-4, my], lw=1.2, alpha=0.55)

line([1228, 1229], [468, 502], lw=4.0, color=RED)
ax.add_patch(mpatches.Circle((1229, 518), 5, fc=RED, ec=RED))
ax.text(1252, 486, '测试没跑', fontproperties=zh, fontsize=24, color=RED)
ax.text(1150, 740, '边界没查', fontproperties=zh, fontsize=23, color=RED)
line([1290, 1308], [722, 700], lw=1.6, color=RED)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
out = '/sessions/affectionate-exciting-cori/mnt/awesome-skills/assets/xiaohei-test-illustrations/01-premature-done.png'
fig.savefig(out, dpi=100, facecolor='white')
print('saved', out)
