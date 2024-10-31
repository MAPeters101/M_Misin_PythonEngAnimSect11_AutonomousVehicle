import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

def vehicle_animation(t,y,psi,delta,xr,yr,psir,frame_amount,lf,lr,lane_width):
    def update_plot(num):
        bike_determined.set_data(xr[0:num],y[0:num])

        bike_1.set_data([xr[num]-lr*np.cos(psi[num]),xr[num]+lf*np.cos(psi[num])],
            [y[num]-lr*np.sin(psi[num]),y[num]+lf*np.sin(psi[num])])

        bike_1_body.set_data([0-lr*np.cos(psi[num]),0+lf*np.cos(psi[num])],
            [0-lr*np.sin(psi[num]),0+lf*np.sin(psi[num])])

        bike_1_body_extension.set_data([0,(lf+40)*np.cos(psi[num])],
            [0,(lf+40)*np.sin(psi[num])])

        bike_1_back_wheel.set_data([-(lr+0.5)*np.cos(psi[num]),-(lr-0.5)*np.cos(psi[num])],
            [-(lr+0.5)*np.sin(psi[num]),-(lr-0.5)*np.sin(psi[num])])

        bike_1_front_wheel.set_data([lf*np.cos(psi[num])-0.5*np.cos(psi[num]+delta[num]),lf*np.cos(psi[num])+0.5*np.cos(psi[num]+delta[num])],
            [lf*np.sin(psi[num])-0.5*np.sin(psi[num]+delta[num]),lf*np.sin(psi[num])+0.5*np.sin(psi[num]+delta[num])])

        bike_1_front_wheel_extension.set_data([lf*np.cos(psi[num]),lf*np.cos(psi[num])+40*lf*np.cos(psi[num]+delta[num])],
            [lf*np.sin(psi[num]),lf*np.sin(psi[num])+40*lf*np.sin(psi[num]+delta[num])])

        yaw_angle_text.set_text(str(round(psi[num],2))+' rad')
        steer_angle_text.set_text(str(round(delta[num],2))+' rad')

        return bike_determined,bike_1,bike_1_body,bike_1_body_extension, \
            bike_1_back_wheel,bike_1_front_wheel,bike_1_front_wheel_extension, \
            yaw_angle_text,steer_angle_text

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

    # Create an object for the motorcycle (zoomed)
    ax1=fig.add_subplot(gs[1,:],facecolor=(0.9,0.9,0.9))
    plt.xlim(-5,30)
    plt.ylim(-4,4)
    plt.ylabel('Y-distance [m]',fontsize=15)
    neutral_line=ax1.plot([-50,50],[0,0],'k',linewidth=1)
    bike_1_body,=ax1.plot([],[],'k',linewidth=3)
    bike_1_body_extension,=ax1.plot([],[],'--k',linewidth=1)
    bike_1_back_wheel,=ax1.plot([],[],'r',linewidth=4)
    bike_1_front_wheel,=ax1.plot([],[],'r',linewidth=4)
    bike_1_front_wheel_extension,=ax1.plot([],[],'--r',linewidth=1)

    bbox_props_angle=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='k',lw=1)
    yaw_angle_text=ax1.text(25,2,'',size='20',color='k',bbox=bbox_props_angle)

    bbox_props_steer_angle=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='r',lw=1)
    steer_angle_text=ax1.text(25,-2.5,'',size='20',color='r',bbox=bbox_props_steer_angle)

    car_ani=animation.FuncAnimation(fig,update_plot,
        frames=frame_amount,interval=20,repeat=True,blit=True)
    plt.show()

    return