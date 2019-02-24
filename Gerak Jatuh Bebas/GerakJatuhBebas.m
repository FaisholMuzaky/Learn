clear all;
close all;
clc;

N=21;
T=5;
V=1;
G=9,8;
deltaT=T/(N-1);
t=[0:deltaT:T];
y(1)=100;
y(2)=y(1)+V*deltaT;
for i=3:N
    y(i)=((-G)*(deltaT^2))-y(i-2)+(2*y(i-1));
end

for j = 1:N
    x(j)=(-0.5*G*(t(j)^2))+(t(j))+100;
end
plot(t,x,'DisplayName','x');
hold on;
plot(t,y,'DisplayName','y');
hold off;
