%N = �m�[�h��
N = 10;

%A = NxN�̃[���s��
A = zeros(N,N);

%�אڍs��̍쐬
for i=1:length(A)
    for j=1:length(A)
        if i == j
            
        else
            R = randsample(2,1);
            A(i,j) = R - 1;
            A(j,i) = R -1;
        end
    end
end

%�O���t�̏o��
G = graph(A);
P = plot(G,'NodeColor','r','MarkerSIze',15,'NodeFontSize',20);
        