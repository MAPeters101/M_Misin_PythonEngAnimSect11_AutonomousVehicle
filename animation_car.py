import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

def vehicle_animation(t,y,psi,delta,xr,yr,psir,frame_amount,lf,lr,lane_width):
    def update_plot(num):

        return

    # Set up your figure properties
    fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
    gs=gridspec.GridSpec(3,3)

    # Create a subplot for the motorcycle
    ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
    plt.xlim(xr[0],xr[frame_amount])
    plt.ylabel('Y-distance [m]',fontsize=15)

    # car_ani=animation.FuncAnimation(fig,update_plot,
    #     frames=frame_amount,interval=20,repeat=True,blit=True)
    plt.show()

    return