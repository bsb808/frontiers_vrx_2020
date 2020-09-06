# Plotting Pierson-Moskowitz

def pm_U(omega,U):
    ''' U_{10} from Realistic Simulation Of Ocean Surface Using Wave Spectra '''
    g = 9.81
    return pm(omega, 0.855*g/U)

def pm(omega,omega_p):
    ''' 
    Return spectrum value as a function of freq and peak freq
    '''
    alpha = 0.0081
    beta = 0.74
    g = 9.81
    return alpha*g**2/(omega**5)*exp(-(5.0/4.0)*(omega_p/omega)**4)

#rc('font',family='serif')

N = 5
for i in range(1,N+1):
    figure(i)
    clf()

Tps = [ 4, 7, 10]
lc = ['r','g','b','c']
K = [1.0, 0.5]

for Tp, c in zip(Tps,lc):
    wp = 2.0*pi/Tp
    U = 20
    Ts = linspace(0.1,20)
    ws =  2.0*pi/Ts
    S = []
    for w in ws:
        S.append(pm(w,wp))
        #S.append(pm_U(w,U))

    H = 0.162*9.81/(wp**2)
    lstr = (r'$T_p = %.1f \, \mathrm{s} $'%Tp +'\n'+ r'$H_{s} = %0.2f \, \mathrm{m}$ '%H)
    figure(1)
    plot(Ts,sqrt(array(S)),c,label=lstr)
    grid(True)
    xlabel('Period [s]')
    ylabel(r'$\sqrt{S(\omega)} \,\,\,\,\, \mathrm{\left[m/\sqrt{rad/s}\right]}$')

    figure(2)
    plot(ws,S,label=lstr)
    grid(True)
    xlabel('Frequency [rad/s]')
    ylabel('S [m^2 / (rad/s)]')

    fs = ws/(2.0*pi)
    figure(3)
    plot(fs,S,label=lstr)
    xlabel('Frequency [Hz]')
    ylabel('S [m^2 / (Hz)]')

    K = [1.0, 0.5]
    ltype = ['-','--']
    for k,lt in zip(K,ltype):
        figure(4)
        lstr = (r'$T_p = %.1f \, \mathrm{s} $'%Tp +'\n'+ r'$K_H = %0.1f$ '%k)
        plot(Ts,k*sqrt(array(S)),c+lt,label=lstr)
        grid(True)
        xlabel('Period [s]')
        ylabel(r'$\sqrt{S(\omega)} \,\,\,\,\, \mathrm{\left[m/\sqrt{rad/s}\right]}$')

for i in range(1,N+1):
    figure(i)
    legend()
    grid(True)

figure(4)
legend(bbox_to_anchor=(0.95, 1.1),ncol=3)
ylim([0, 2])

show()


