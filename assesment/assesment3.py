###################################################
# The following 3 lines are required for drawing
# Do not edit or remove these
import sys
import matplotlib
matplotlib.use('Agg')
###################################################

# import your modules in the space below:
import matplotlib.pyplot as plt


# write your code in the space below:

#function to draw and combined all 4 triangles
def combined():
 #red triangle
 ax_a = [3, 5, 7, 3]
 ax_b = [3, 5, 3, 3]
 #blue triangle
 ax_c = [3, 5, 7, 3]
 ax_d = [5, 3, 5, 5]
 #green triangle
 ax_e = [3, 3, 7, 3]
 ax_f = [3, 5, 4, 3]
 #yellow triangle
 ax_g = [7, 7, 3, 7]
 ax_h = [3, 5, 4, 3]
 
 plt.plot(ax_a, ax_b, 'ro--', ax_c, ax_d, 'bs:', ax_e, ax_f, 'gd-.', ax_g, ax_h, 'yp-')
 plt.show

#function to draw and seperate each traingle onto a subplot
def seperated():
 #red triangle
 ax_a = [3, 5, 7, 3]
 ax_b = [3, 5, 3, 3]
 #blue triangle
 ax_c = [3, 5, 7, 3]
 ax_d = [5, 3, 5, 5]
 #green triangle
 ax_e = [3, 3, 7, 3]
 ax_f = [3, 5, 4, 3]
 #yellow triangle
 ax_g = [7, 7, 3, 7]
 ax_h = [3, 5, 4, 3]
 
 fig, axs = plt.subplots(2, 2)
 axs[0, 0].plot(ax_a, ax_b, 'ro--')
 axs[0, 1].plot(ax_c, ax_d, 'bs:')
 axs[1, 0].plot(ax_e, ax_f, 'gd-.')
 axs[1, 1].plot(ax_g, ax_h, 'yp-')
 #plt.show
 
seperated()



###################################################
# The following 2 lines are need to display plots.
# Do not edit or remove these
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
################################################### 