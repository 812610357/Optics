hold on

Lambda = 0.5;
d = 30;
a = 15;
n = 10;
sintheta = linspace(-0.06, 0.06, 12000);

alpha = pi .* a .* sintheta ./ Lambda;
beta = pi .* d .* sintheta ./ Lambda;
id = (sin(alpha) ./ alpha).^2;
id = id ./ max(id);
ii = (sin(n * beta) ./ sin(beta)).^2;
ii = ii ./ max(ii);
I = id .* ii;

plot(sintheta, id)
plot(sintheta, I)

xlabel('{sin \theta}')
ylabel('{I/I_0}')
title('Light-strength distribution')
legend('{I_d}', '{I}')
