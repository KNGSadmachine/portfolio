clear;
time = 10; %���s��
N = 5; %�m�[�h��N^2
A = zeros(N^2,N^2);
U = [2:N-1];
B = [N^2-N+2:N^2-1];
L = [N+1:N:N^2-N];
R = [2*N:N:N^2-N];
C=zeros(1,N^2);
%����
A(1,2) = 1;
A(1,1+N) = 1;
C(1) = 1;
%�E��
A(N,N-1) = 1;
A(N,2*N) = 1;
C(N) = 1;
%����
A(N^2-N+1,N^2-2*N+1) = 1;
A(N^2-N+1,N^2-N+2) = 1;
C(N^2-N+1) = 1;
%�E��
A(N^2,N^2-N) = 1;
A(N^2,N^2-1) = 1;
C(N^2) = 1;

for i=2:N-1 %��      
        A(i,i+1) = 1;
        A(i,i+N) = 1;
        A(i,i-1) = 1;
        C(i) = 1;
end
for i=N^2-N+2:N^2-1 %��
        A(i,i+1) = 1;
        A(i,i-N) = 1;
        A(i,i-1) = 1;
        C(i) = 1;
end
for i=N+1:N:N^2-N %��
        A(i,i-N) = 1;
        A(i,i+1) = 1;
        A(i,i+N) = 1;
        C(i) = 1;
end
for i=2*N:N:N^2-N %�E
        A(i,i-N) = 1;
        A(i,i-1) = 1;
        A(i,i+N) = 1;
        C(i) = 1;
end

for i=1:N^2
    if C(i) == 1;
    
    else
        A(i,i-1) = 1;
        A(i,i+1) = 1;
        A(i,i+N) = 1;
        A(i,i-N) = 1;  
    end
end
S = [1:N^2];
G = graph(A);
P = plot(G,'NodeColor','r','MarkerSIze',5,'NodeFontSize',10);
Ad = full(adjacency(G));
I = randsample(N^2,1);
highlight(P,I,'NodeColor','g');

K = find(I);

for i = 1:length(I)
    K = find(A(I(i),:));
end

