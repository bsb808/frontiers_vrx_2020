
function ferror = func_roughness(x,v10)
vstar = x(1);
z0 = x(2);

alpha =0.0144;
k = 0.41;
g = 9.81;

e1 = vstar - k*v10/(log(10/z0));
e2 = alpha - z0*g/vstar^2;

ferror = e1^2 + e2^2;

