import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

def vehicle_animation(t,y,psi,delta,xr,yr,psir,frame_amount,lf,lr,lane_width):
    def update_plot(num):

        return



car_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()

return