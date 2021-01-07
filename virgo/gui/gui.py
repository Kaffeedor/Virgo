import virgo
import tkinter as tk

while 1:
    if __name__ == "__main__":
        break


def onPlay():
    durationvar = duration.get()
    frequencyvar = float(frequency.get())
    bandwidthvar = float(bandwidth.get())
    channelsvar = int(channels.get())
    t_samplevar = float(t_sample.get())
    rf_gainvar = float(rf_gain.get())
    if_gainvar = float(if_gain.get())
    bb_gainvar = float(bb_gain.get())
    dev_argsvar = dev_args.get()
    cal_filevar = cal_file.get()
    print(t_samplevar, bandwidthvar)

    if durationvar == "":
        durationvar=60
    else:
        symbol=durationvar[-1]
        try:
            float(symbol)
        except:
            if symbol=="s":
                durationvar=float(durationvar)
            elif symbol=="m":
                durationvar=float(durationvar)*60
            elif symbol=="h":
                durationvar=float(durationvar)*60*60
            elif symbol=="d":
                durationvar=float(durationvar)*60*60*24
    if frequencyvar == "":
        frequencyvar=1420e6
    if bandwidthvar == "":
        bandwidthvar=5e6
    if channelsvar == "":
        channelsvar=2048
    if t_samplevar == "":
        t_samplevar=1
    if rf_gainvar == "":
        rf_gainvar=10
    if if_gainvar == "":
        if_gainvar=20
    if bb_gainvar == "":
        bb_gainvar=20

        # Define observation parameters
    observation = {
        'dev_args': dev_argsvar,
        'rf_gain': rf_gainvar,
        'if_gain': if_gainvar,
        'bb_gain': bb_gainvar,
        'frequency': frequencyvar,
        'bandwidth': bandwidthvar,
        'channels': channelsvar,
        't_sample': t_samplevar,
        'duration': durationvar
    }

    # Data acquisition
    virgo.observe(obs_parameters=observation, obs_file='observation.dat', start_in=0)

    # Data analysis
    virgo.plot(obs_parameters=observation, n=10, m=25, f_rest=1420.4057517667e6,
            dB=False, obs_file='observation.dat', cal_file=cal_filevar, waterfall_fits='obs.fits',
            spectra_csv='spectra.csv', power_csv='pwr.csv', plot_file='plot.png')


def onExit():
    quit()


#main

main_window = tk.Tk()
main_window.title("VIRGO GUI vWIP")
main_window.geometry("600x600")
main_window.iconphoto(False, tk.PhotoImage(file="icon.png"))


duration_label = tk.Label(main_window, text="duration: ") #duration label
duration_label.pack()
duration=tk.Entry(main_window, bd=5, width=40)
duration.pack()

frequency_label = tk.Label(main_window, text="frequency: ") #frequency label
frequency_label.pack()
frequency=tk.Entry(main_window, bd=5, width=40)
frequency.pack()

bandwidth_label = tk.Label(main_window, text="bandwidth: ") #bandwidth label
bandwidth_label.pack()
bandwidth=tk.Entry(main_window, bd=5, width=40)
bandwidth.pack()

channels_label = tk.Label(main_window, text="channels: ") #channels label
channels_label.pack()
channels=tk.Entry(main_window, bd=5, width=40)
channels.pack()

t_sample_label = tk.Label(main_window, text="t_sample: ") #t_sample label
t_sample_label.pack()
t_sample=tk.Entry(main_window, bd=5, width=40)
t_sample.pack()

rf_gain_label = tk.Label(main_window, text="rf_gain: ") #rf_gain label
rf_gain_label.pack()
rf_gain=tk.Entry(main_window, bd=5, width=40)
rf_gain.pack()

if_gain_label = tk.Label(main_window, text="if_gain: ") #if_gain label
if_gain_label.pack()
if_gain=tk.Entry(main_window, bd=5, width=40)
if_gain.pack()

bb_gain_label = tk.Label(main_window, text="bb_gain: ") #bb_gain label
bb_gain_label.pack()
bb_gain=tk.Entry(main_window, bd=5, width=40)
bb_gain.pack()

dev_args_label = tk.Label(main_window, text="dev_args: ") #dev_args label
dev_args_label.pack()
dev_args=tk.Entry(main_window, bd=5, width=40)
dev_args.pack()

cal_file_label = tk.Label(main_window, text="cal_file: ") #cal_file label
cal_file_label.pack()
cal_file=tk.Entry(main_window, bd=5, width=40)
cal_file.pack()

photo = tk.PhotoImage(file="PlayButton.png") #play button
playbutton = tk.Button(main_window, image=photo, command=onPlay)
playbutton.pack()


main_window.mainloop()
