import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

def vehicle_animation(t,y,psi,delta,xr,yr,psir,frame_amount,lf,lr,lane_width):
    def update_plot(num):
        bike_determined.set_data(xr[0:num],y[0:num])


        return bike_determined,

    # Set up your figure properties
    fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
    gs=gridspec.GridSpec(3,3)

    # Create a subplot for the motorcycle
    ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
    plt.xlim(xr[0],xr[frame_amount])
    plt.ylabel('Y-distance [m]',fontsize=15)

    # Plot the lanes
    lane_1,=ax0.plot([xr[0],xr[frame_amount]],[lane_width/2,lane_width/2],'k',linewidth=0.2)
    lane_2,=ax0.plot([xr[0],xr[frame_amount]],[-lane_width/2,-lane_width/2],'k',linewidth=0.2)

    lane_3,=ax0.plot([xr[0],xr[frame_amount]],[lane_width/2+lane_width,lane_width/2+lane_width],'k',linewidth=0.2)
    lane_4,=ax0.plot([xr[0],xr[frame_amount]],[-lane_width/2-lane_width,-lane_width/2-lane_width],'k',linewidth=0.2)

    lane_5,=ax0.plot([xr[0],xr[frame_amount]],[lane_width/2+2*lane_width,lane_width/2+2*lane_width],'k',linewidth=3)
    lane_6,=ax0.plot([xr[0],xr[frame_amount]],[-lane_width/2-2*lane_width,-lane_width/2-2*lane_width],'k',linewidth=3)

    ref_trajectory=ax0.plot(xr,yr,'b',linewidth=1) # reference trajectory

    # Draw a motorcycle
    bike_1,=ax0.plot([],[],'k',linewidth=3)
    bike_determined,=ax0.plot([],[],'-r',linewidth=1)

    car_ani=animation.FuncAnimation(fig,update_plot,
        frames=frame_amount,interval=20,repeat=True,blit=True)
    plt.show()

    return