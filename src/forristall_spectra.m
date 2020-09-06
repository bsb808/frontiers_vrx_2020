function sigma_xx = forristall_spectra(f,z,vz,sigma)

% One-sided Forristall spectrum as a function of oscillation frequency 
% f - in Hz
% sigma - sqrt of variance
% z - height, typically 10
% vz - mean velocity at z

if ~exist('sigma','var')
    w = 1;
    sigma = 3*w*(0.00076 * vz^2 +0.0304*vz);
end

A = 42.0;
B = 63.0;
sigma_xx = (sigma^2 * A * z /vz) / (1 + B * f * z / vz)^(5/3);


