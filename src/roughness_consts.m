pubfig

V10 = linspace(4,21,20);
x = [0.1, 0.1];    
vstar = zeros(length(V10),1);
z0 = zeros(length(V10),1);
for ii = 1:length(V10)
    v10 = V10(ii);
    x0 = x;
    fun = @(x)func_roughness(x,v10);
    [x,fval,exitflag,output]  = fminsearch(fun,x0);
    vstar(ii) = x(1);
    z0(ii) = x(2);
end

% Set font size
labelFont = 18;
tickFont = 13;


figure(1);
clf();
% ax = gca();
% set(gca(),'FontSize',14);
% ax.YAxis.FontSize = 10;
yyaxis left

% See https://www.mathworks.com/matlabcentral/answers/298117-independent-xticklabel-and-yticklabel-font-sizes
p_vstar = plot(V10,vstar,'b','linewidth',2)
xl = xlabel('Mean wind speed, $v_{10}$ [m/s]','interpreter','latex');
yl = ylabel('Friction velocity, $v_*$ [m/s]','interpreter','latex');
ax = ancestor(p_vstar,'axes');
yrules = ax.YAxis;
xrule = ax.XAxis;
grid on

for ii = 1:length(yrules)
    yrules(ii).FontSize = tickFont;
end
xrule.FontSize = tickFont;
yl.FontSize = labelFont;
xl.FontSize = labelFont;

yyaxis right
p_z0 = plot(V10,z0,'r','linewidth',2)
ylr = ylabel('Sea surface roughness, $z_0$ [m]','interpreter','latex')
ax = ancestor(p_z0,'axes');
yrules = ax.YAxis;
for ii = 1:length(yrules)
    yrules(ii).FontSize = tickFont;
end
ylr.FontSize = labelFont;
yl.FontSize = labelFont;  %labelFont;



figure(2)
clf()
w = 1.0;
plot(V10,3.0*w*vstar,'b','linewidth',2)
grid on
xlabel('Mean wind speed, $\bar{v}_{10}$ [m/s]','interpreter','latex')
ylabel('Standard deviation of wind speed, $\sigma$ [m/s]','interpreter','latex')

% Polyfit
p = polyfit(V10',3.0*w*vstar,2)
hold on
vv = linspace(0,25,10);
%plot(vv,polyval(p,vv),'k--')

% Nonlinear regression
% Quadratic with zero intercept
polyfcn = @(b,x) b(1).*x + b(2).*x.^2;
% Intial guess from poly fit
beta0 = [p(2), p(1)];
beta = nlinfit(V10',3.0*w*vstar,polyfcn,beta0)
pp = [beta(2) beta(1) 0];
plot(vv,polyval(pp,vv),'k--')
pstr = sprintf('$\\sigma = %.4f \\, \\bar{v}_{10}^2 + %.3f \\, \\bar{v}_{10}$',beta(2), beta(1));
legend('Numerical Soln for $v_*$',pstr,'interpreter','latex','location','northwest')


% Now fit the sea surface roughness
beta0 = beta/3;
beta = nlinfit(V10',vstar,polyfcn,beta0)
figure(1)
hold on
yyaxis left
pp = [beta(2) beta(1) 0];
p_fit = plot(vv,polyval(pp,vv),'k--')
pstr = sprintf('Fit: \n $v_* = %.5f \\, \\bar{v}_{10}^2 + %.4f \\, \\bar{v}_{10}$',beta(2), beta(1));
l = legend([p_vstar, p_fit, p_z0], ...
    {'Numerical Soln for $v_*$',  ...
        pstr, ...
        '$z_0$'}, ...
        'interpreter','latex','location','northwest');
    
set(l,'FontSize',14);