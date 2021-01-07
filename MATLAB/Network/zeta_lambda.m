clear;

format long

L = 2;
D = 1000000000;
%x = 0;
%f = x;
%g = exp(L*(x-1));

I = [];

for x = 0:1/D:1
    E = abs(x-exp(L*(x-1)));
    if E < 1/D
        I(end+1) = x;
    end
end


Point = [I(2),I(2)];
disp(Point);
Alive = 1 - I(2);
disp(Alive);