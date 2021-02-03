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

plot(sintheta, id,'LineWidth',2)
plot(sintheta, I,'LineWidth',2)

xlabel('{sin \theta}','fontsize',24)
ylabel('{I/I_0}','fontsize',24)
title('Light-strength distribution','fontsize',36)
legend('{I_d}', '{I}','fontsize',24)
