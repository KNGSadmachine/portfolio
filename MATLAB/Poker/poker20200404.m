clear ;

strRSF = "Ｒ・ストレート・フラッシュ　　";
strSF  = "ストレート・フラッシュ　　　　";
str4   = "４カード　　　　　　　　　　　";
str32  = "フルハウス　　　　　　　　　　";
strF   = "フラッシュ　　　　　　　　　　";
strS   = "ストレート　　　　　　　　　　";
str3   = "３カード　　　　　　　　　　　";
str2   = "２ペア　　　　　　　　　　　　";
str1   = "１ペア　　　　　　　　　　　　";
strNo  = "なし　　　　　　　　　　　　　";

nRSF = 0;
nSF = 0;
nF = 0;
nS = 0;
n4 = 0;
n32 = 0;
n3 = 0;
n2 = 0;
n1 = 0;

% カード画像を読み込み
for i=0:3
    for j=1:13
        str = strcat( num2str(i), num2str(j,'%02u'),'.png');
        CardImg{i*13+j} = imread( strcat( num2str(i), num2str(j,'%02u'),'.png') );
    end
end 
  
num = 100;
        
for j=1:num
    % 乱数で５２枚から５枚を選ぶ
    X = randsample(52,5)-1;
    Suit = floor(X./13);
    Number = rem(X,13)+1;

    % ５枚の数字をソート
    Number = sort(Number);

    Hand = strNo;

    % 役の判定（フラッシュ系とストレート）
    if Suit(1)==Suit(2) && Suit(2)==Suit(3) && Suit(3)==Suit(4) && Suit(4) ==Suit(5) % 全て同じ絵柄か？
        if Number==[1,10,11,12,13]
            Hand = strRSF;
            nRSF = nRSF + 1;
        elseif Number(1)==(Number(2)-1) && Number(2)==(Number(3)-1) && Number(3)==(Number(4)-1) && Number(4)==(Number(5)-1)
            Hand = strSF;
            nSF = nSF + 1;
        else
            Hand = strF;
            nF = nF + 1;
        end
    elseif Number(1)==(Number(2)-1) && Number(2)==(Number(3)-1) && Number(3)==(Number(4)-1) && Number(4)==(Number(5)-1) % ストレート
        Hand = strS;
        nS = nS + 1;
    end
    
    % 役の判定（４カード、フルハウス、３カード、２ペア、１ペア）
    if Number(1)==Number(2)==Number(3)==Number(4) || Number(2)==Number(3)==Number(4)==Number(5)
        Hand = str4;
        n4 =n4 + 1;
    elseif Number(1)==Number(2) && Number(2)==Number(3)
        if Number(4)==Number(5)
            Hand = str32;
            n32 = n32 + 1;
        else
            Hand = str3;
            n3 = n3 + 1;
        end
    elseif Number(2)==Number(3) && Number(3)==Number(4)
            Hand = str3;
        n3 = n3 + 1;
    elseif Number(3)==Number(4) && Number(4)==Number(5)
        if Number(1)==Number(2)
            Hand = str32;
            n32 = n32 + 1;
        else
            Hand = str3;
            n3 = n3 + 1;
        end
    elseif Number(1)==Number(2) && (Number(3)==Number(4) || Number(4)==Number(5))
        Hand = str2;
        n2 = n2 + 1;
    elseif Number(2)==Number(3) && Number(4)==Number(5)
        Hand = str2;
        n2 = n2 + 1;
    elseif Number(1)==Number(2) || Number(2)==Number(3) || Number(3)==Number(4) || Number(4)==Number(5)
        Hand = str1;
        n1 = n1 + 1;
    end
    
    % ウィンドウ表示
    tiledlayout(2,5);
    
    % 画面に５枚のカードを表示
    for i=1:5
        nexttile;
        imshow( CardImg{X(i)+1} );
    end
    
    Rate = [n1, n2, n3, nS, nF, n32, n4, nSF, nRSF] ./j*100;
    num = [nRSF, nSF, n4, n32, nF, nS, n3, n2, n1];

    nexttile;   % 出現回数を表示するヒートマップ
    xvalues = { '出現回数' };
    yvalues = { 'RSF', 'SF', '４カード', 'フルハウス', 'フラッシュ', 'ストレート', '３カード', '２ペア', '１ペア' };
    h = heatmap( xvalues, yvalues, num' );
    h.ColorbarVisible = 'off';
    h.CellLabelFormat = '%4d';
    title( {['試行回数：',num2str(j,'%03u')];''} );

    nexttile([1 4]);    % 出現割合を表示する横棒グラフ
    b = barh( Rate );
    xlim([0,100]);
    xticks( [ 0, 20, 40, 60, 80, 100] );
    yticks( [] );
    xtips = b.XEndPoints;
    ytips = b.YEndPoints;
    labels = strcat( num2str(Rate','%03.1f'), '%' );
    text(ytips+0.5,xtips,labels,'HorizontalAlignment','left','VerticalAlignment','middle' );

    title({Hand;''}, 'HorizontalAlignment', 'right', 'FontName', 'FixedWidth' );

    disp( j );
    drawnow;

    if Hand~=strNo && Hand~=str1
    %   waitforbuttonpress;
    end
end