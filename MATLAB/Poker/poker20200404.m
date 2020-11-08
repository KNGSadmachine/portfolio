clear ;

strRSF = "�q�E�X�g���[�g�E�t���b�V���@�@";
strSF  = "�X�g���[�g�E�t���b�V���@�@�@�@";
str4   = "�S�J�[�h�@�@�@�@�@�@�@�@�@�@�@";
str32  = "�t���n�E�X�@�@�@�@�@�@�@�@�@�@";
strF   = "�t���b�V���@�@�@�@�@�@�@�@�@�@";
strS   = "�X�g���[�g�@�@�@�@�@�@�@�@�@�@";
str3   = "�R�J�[�h�@�@�@�@�@�@�@�@�@�@�@";
str2   = "�Q�y�A�@�@�@�@�@�@�@�@�@�@�@�@";
str1   = "�P�y�A�@�@�@�@�@�@�@�@�@�@�@�@";
strNo  = "�Ȃ��@�@�@�@�@�@�@�@�@�@�@�@�@";

nRSF = 0;
nSF = 0;
nF = 0;
nS = 0;
n4 = 0;
n32 = 0;
n3 = 0;
n2 = 0;
n1 = 0;

% �J�[�h�摜��ǂݍ���
for i=0:3
    for j=1:13
        str = strcat( num2str(i), num2str(j,'%02u'),'.png');
        CardImg{i*13+j} = imread( strcat( num2str(i), num2str(j,'%02u'),'.png') );
    end
end 
  
num = 100;
        
for j=1:num
    % �����łT�Q������T����I��
    X = randsample(52,5)-1;
    Suit = floor(X./13);
    Number = rem(X,13)+1;

    % �T���̐������\�[�g
    Number = sort(Number);

    Hand = strNo;

    % ���̔���i�t���b�V���n�ƃX�g���[�g�j
    if Suit(1)==Suit(2) && Suit(2)==Suit(3) && Suit(3)==Suit(4) && Suit(4) ==Suit(5) % �S�ē����G�����H
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
    elseif Number(1)==(Number(2)-1) && Number(2)==(Number(3)-1) && Number(3)==(Number(4)-1) && Number(4)==(Number(5)-1) % �X�g���[�g
        Hand = strS;
        nS = nS + 1;
    end
    
    % ���̔���i�S�J�[�h�A�t���n�E�X�A�R�J�[�h�A�Q�y�A�A�P�y�A�j
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
    
    % �E�B���h�E�\��
    tiledlayout(2,5);
    
    % ��ʂɂT���̃J�[�h��\��
    for i=1:5
        nexttile;
        imshow( CardImg{X(i)+1} );
    end
    
    Rate = [n1, n2, n3, nS, nF, n32, n4, nSF, nRSF] ./j*100;
    num = [nRSF, nSF, n4, n32, nF, nS, n3, n2, n1];

    nexttile;   % �o���񐔂�\������q�[�g�}�b�v
    xvalues = { '�o����' };
    yvalues = { 'RSF', 'SF', '�S�J�[�h', '�t���n�E�X', '�t���b�V��', '�X�g���[�g', '�R�J�[�h', '�Q�y�A', '�P�y�A' };
    h = heatmap( xvalues, yvalues, num' );
    h.ColorbarVisible = 'off';
    h.CellLabelFormat = '%4d';
    title( {['���s�񐔁F',num2str(j,'%03u')];''} );

    nexttile([1 4]);    % �o��������\�����鉡�_�O���t
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