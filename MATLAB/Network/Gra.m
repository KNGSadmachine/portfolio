%N = ノード数
N = 10;

%A = NxNのゼロ行列
A = zeros(N,N);

%隣接行列の作成
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

%グラフの出力
G = graph(A);
P = plot(G,'NodeColor','r','MarkerSIze',15,'NodeFontSize',20);
        