clear;

fid = fopen('TimeTableSub.csv');
A = textscan(fid,'%d,%d,%d,%d,%d,%s');
fclose(fid);

SubjectNo = size(A{1},1);  
Subject = string(SubjectNo);     
Grade = string(SubjectNo);
Jikan = string(SubjectNo);
Place = string(SubjectNo);
Course = string(SubjectNo);

for i=1:SubjectNo
    Subject(i)=A{6}(i);
    Grade(i)=A{2}(i);
    Jikan(i)=A{3}(i);
    Place(i)=A{4}(i);
    Course(i)=A{5}(i);
end


slotfile = fopen('TimeTableSlot.csv');
B = textscan(slotfile,'%d,%s');
fclose(slotfile);

SlotNo = size(B{1},1);
Slot = string(SlotNo);

for t=1:SlotNo
    Slot(t)=B{2}(t);
end

teacherfile=fopen('TimeTableTeacher.csv');
C = textscan(teacherfile,'%d,%d,%s');
fclose(teacherfile);

for i=1:SubjectNo
    TeacherNo(i)=C{2}(i);
    TeacherName(i)=C{3}(i);
end

INDEX = [1:SubjectNo; Grade; Jikan; Place; Course; Subject; TeacherNo; TeacherName];

SE31 = 0;
SE32 = 0;
SK31 = 0;           
SKJ31 = 0;
SK32 = 0;
SKJ32 = 0;
SK33 = 0;
SKJ33 = 0;
SK34 = 0;
SKJ34 = 0;
SP31 = 0;
SPJ31 = 0;
SP32 = 0;
SPJ32 = 0;
SP33 = 0;
SPJ33 = 0;
SP34 = 0;
SPJ34 = 0;
SM31 = 0;
SMJ31 = 0;
SM32 = 0;
SMJ32 = 0;
SM33 = 0;
SMJ33 = 0;
SM34 = 0;
SMJ34 = 0;


SE41 = 0;
SE42 = 0;
SK41 = 0;           
SKJ41 = 0;
SK42 = 0;
SKJ42 = 0;
SK43 = 0;
SKJ43 = 0;
SK44 = 0;
SKJ44 = 0;
SP41 = 0;
SPJ41 = 0;
SP42 = 0;
SPJ42 = 0;
SP43 = 0;
SPJ43 = 0;
SP44 = 0;
SPJ44 = 0;
SM41 = 0;
SMJ41 = 0;
SM42 = 0;
SMJ42 = 0;
SM43 = 0;
SMJ43 = 0;
SM44 = 0;
SMJ44 = 0;
S3 = 0;
S4 = 0;

for i=1:SubjectNo
    if INDEX(4,i)=='3' %人社の教室を使用する科目
        S3(i)=i;
        if INDEX(5,i)=='0' %一般教
                if INDEX(2,i)=='1'
                    SE31(i)=i;
                else
                    SE32(i)=i;
                end

        elseif INDEX(5,i)=='1' %学科共通科目集合
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SK31(i)=i;
                else
                    SKJ31(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SK32(i)=i;
                else
                    SKJ32(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SK33(i)=i;
                else
                    SKJ33(i)=i;
                end
            end

        elseif INDEX(5,i)=='2' %数物コース科目
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SP31(i)=i;
                else
                    SPJ31(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SP32(i)=i;
                else
                    SPJ32(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SP33(i)=i;
                else
                    SPJ33(i)=i;
                end
            end
        else %マテリアル科目集合
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SM31(i)=i;
                else
                    SMJ31(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SM32(i)=i;
                else
                    SMJ32(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SM33(i)=i;
                else
                    SMJ33(i)=i;
                end
            end
        end
    else %理工側の教室を使用する科目
        S4(i) = i;
        if INDEX(5,i)=='0' %一般教
                if INDEX(2,i)=='1'
                    SE41(i)=i;
                else
                    SE42(i)=i;
                end

        elseif INDEX(5,i)=='1' %学科共通科目集合
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SK41(i)=i;
                else
                    SKJ41(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SK42(i)=i;
                else
                    SKJ42(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SK43(i)=i;
                else
                    SKJ43(i)=i;
                end
            end

        elseif INDEX(5,i)=='2' %数物コース科目
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SP41(i)=i;
                else
                    SPJ41(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SP42(i)=i;
                else
                    SPJ42(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SP43(i)=i;
                else
                    SPJ43(i)=i;
                end
            end
        else %マテリアル科目集合
            if INDEX(2,i)=='1'
                if INDEX(3,i)=='1'
                    SM41(i)=i;
                else
                    SMJ41(i)=i;
                end

            elseif INDEX(2,i)=='2'
                if INDEX(3,i)=='1'
                    SM42(i)=i;
                else
                    SMJ42(i)=i;
                end

            elseif INDEX(2,i)=='3'
                if INDEX(3,i)=='1'
                    SM43(i)=i;
                else
                    SMJ43(i)=i;
                end
            end
        end
    end
end
SE31 = find(SE31);
SE32 = find(SE32);
SK31 = find(SK31);           
SKJ31 = find(SKJ31);
SK32 = find(SK32);
SKJ32 = find(SKJ32);
SK33 = find(SK33);
SKJ33 = find(SKJ33);
SK34 = find(SK34);
SKJ34 = find(SKJ34);
SP31 = find(SP31);
SPJ31 = find(SPJ31);
SP32 = find(SP32);
SPJ32 = find(SPJ32);
SP33 = find(SP33);
SPJ33 = find(SPJ33);
SP34 = find(SP34);
SPJ34 = find(SPJ34);
SM31 = find(SM31);
SMJ31 = find(SMJ31);
SM32 = find(SM32);
SMJ32 = find(SMJ32);
SM33 = find(SM33);
SMJ33 = find(SMJ33);
SM34 = find(SM34);
SMJ34 = find(SMJ34);

SE41 = find(SE41);
SE42 = find(SE42);
SK41 = find(SK41);           
SKJ41 = find(SKJ41);
SK42 = find(SK42);
SKJ42 = find(SKJ42);
SK43 = find(SK43);
SKJ43 = find(SKJ43);
SK44 = find(SK44);
SKJ44 = find(SKJ44);
SP41 = find(SP41);
SPJ41 = find(SPJ41);
SP42 = find(SP42);
SPJ42 = find(SPJ42);
SP43 = find(SP43);
SPJ43 = find(SPJ43);
SP44 = find(SP44);
SPJ44 = find(SPJ44);
SM41 = find(SM41);
SMJ41 = find(SMJ41);
SM42 = find(SM42);
SMJ42 = find(SMJ42);
SM43 = find(SM43);
SMJ43 = find(SMJ43);
SM44 = find(SM44);
SMJ44 = find(SMJ44);


SE1 = sort([SE31,SE41]);
SE2 = sort([SE32,SE42]);
SK1 = sort([SK31,SKJ31,...
    SK41,SKJ41]);
SK2 = sort([SK32,SKJ32,...
    SK42,SKJ42]);
SK3 = sort([SK33,SKJ33,...
    SK43,SKJ43]);
SK4 = sort([SK34,SKJ34,...
    SK44,SKJ44]);
SP1 = sort([SP31,SPJ31,...
    SP41,SPJ41]);
SP2 = sort([SP32,SPJ32,...
    SP42,SPJ42]);
SP3 = sort([SP33,SPJ33,...
    SP43,SPJ43]);
SP4 = sort([SP34,SPJ34,...
    SP44,SPJ44]);
SM1 = sort([SM31,SMJ31,...
    SM41,SMJ41]);
SM2 = sort([SM32,SMJ32,...
    SM42,SMJ42]);
SM3 = sort([SM33,SMJ33,...
    SM43,SMJ43]);
SM4 = sort([SM34,SMJ34,...
    SM44,SMJ44]);
S3 = [S3,0,0,0,0,0,0];
for i=1:length(S3)
    if S3(1,i) == 0
        SubNo_H(i) = 0;
    else
        SubNo_H(i) = 1;
    end
end
for i=1:length(S4)
    if S4(1,i) == 0
        SubNo_P(i) = 0;
    else
        SubNo_P(i) = 1;
    end
end

TeacherAndSubject = zeros(max(TeacherNo),SubjectNo);
for i=1:SubjectNo %科目数
    k(i)=str2num(INDEX(7,i));
    TeacherAndSubject(k(i),i)=1;
end

TD1 = [1,2,3,4,6,7,8,9,11,12,13,14,15,17,18,19,20,22,23,24,25];
for i=1:length(TD1)
    for j=1:4
        TD(i+length(TD1)*(j-1)) = TD1(i) + 26*(j-1); 
    end
end

occupy = optimvar('occupy',length(Slot),length(Subject),...
    'Type','integer','LowerBound',0,'Upperbound',1);
occupy2 = optimvar('occupy2',length(TD)*2,9,...
    'Type','integer','LowerBound',0,'Upperbound',1);

F = 0; %目的関数
for i=1:length(TD)*2
        F = F + occupy2(i,:)*[0;0;0;0;0;1;0;1;0] ;
end

prob=optimproblem('ObjectiveSense','minimize','Objective',F);

prob.Constraints.c1 = sum(occupy,1)==1;
prob.Constraints.c2 = sum(occupy,2)<=1;


prob.Constraints.x1 = sum(occupy2,2)==1;

CS_Distance1 = optimconstr(1,length(TD));
CS_Distance2 = optimconstr(1,length(TD));
CS_Distance3 = optimconstr(1,length(TD));
CS_Distance4 = optimconstr(1,length(TD));
CS_Distance5 = optimconstr(1,length(TD));
CS_Distance6 = optimconstr(1,length(TD));
CS_Distance7 = optimconstr(1,length(TD));
CS_Distance8 = optimconstr(1,length(TD));
CS_Distance9 = optimconstr(1,length(TD));
CS_Distance10 = optimconstr(1,length(TD));
CS_Distance11 = optimconstr(1,length(TD));
CS_Distance12 = optimconstr(1,length(TD));
CS_Distance13 = optimconstr(1,length(TD));
CS_Distance14 = optimconstr(1,length(TD));
CS_Distance15 = optimconstr(1,length(TD));
CS_Distance16 = optimconstr(1,length(TD));
CS_Distance17 = optimconstr(1,length(TD));
CS_Distance18 = optimconstr(1,length(TD));

for i=1:length(TD)
    a = sum(occupy(TD(i),:).*SubNo_H) + sum(occupy(TD(i)+104,:).*SubNo_H);
    b = sum(occupy(TD(i)+1,:).*SubNo_H) + sum(occupy(TD(i)+105,:).*SubNo_H);
    c = sum(occupy(TD(i),:).*SubNo_P) + sum(occupy(TD(i)+104,:).*SubNo_P);
    d = sum(occupy(TD(i)+1,:).*SubNo_P) + sum(occupy(TD(i)+105,:).*SubNo_P);
    e = sum(occupy(TD(i),:).*SubNo_H) + sum(occupy(TD(i)+208,:).*SubNo_H);
    f = sum(occupy(TD(i)+1,:).*SubNo_H) + sum(occupy(TD(i)+209,:).*SubNo_H);
    g = sum(occupy(TD(i),:).*SubNo_P) + sum(occupy(TD(i)+208,:).*SubNo_P);
    h = sum(occupy(TD(i)+1,:).*SubNo_P) + sum(occupy(TD(i)+209,:).*SubNo_P);

    s1 = 4*occupy2(i,1)+a+b+c+d;
    s2 = 4*occupy2(i,2)+a+(1-b)+c+d;
    s3 = 4*occupy2(i,3)+a+b+c+(1-d);
    s4 = 4*occupy2(i,4)+(1-a)+b+c+d;
    s5 = 4*occupy2(i,5)+(1-a)+(1-b)+c+d;
    s6 = 4*occupy2(i,6)+(1-a)+b+c+(1-d);
    s7 = 4*occupy2(i,7)+a+b+(1-c)+d;
    s8 = 4*occupy2(i,8)+a+(1-b)+(1-c)+d;
    s9 = 4*occupy2(i,9)+a+b+(1-c)+(1-d);
    
    s10 = 4*occupy2(length(TD)+i,1)+e+f+g+h;
    s11 = 4*occupy2(length(TD)+i,2)+e+(1-f)+g+h;
    s12 = 4*occupy2(length(TD)+i,3)+e+f+g+(1-h);
    s13 = 4*occupy2(length(TD)+i,4)+(1-e)+f+g+h;
    s14 = 4*occupy2(length(TD)+i,5)+(1-e)+(1-f)+g+h;
    s15 = 4*occupy2(length(TD)+i,6)+(1-e)+f+g+(1-h);
    s16 = 4*occupy2(length(TD)+i,7)+e+f+(1-g)+h;
    s17 = 4*occupy2(length(TD)+i,8)+e+(1-f)+(1-g)+h;
    s18 = 4*occupy2(length(TD)+i,9)+e+f+(1-g)+(1-h);
    
    CS_Distance1(i) = s1<=4;
    CS_Distance2(i) = s2<=4;
    CS_Distance3(i) = s3<=4;
    CS_Distance4(i) = s4<=4;
    CS_Distance5(i) = s5<=4;
    CS_Distance6(i) = s6<=4;
    CS_Distance7(i) = s7<=4;
    CS_Distance8(i) = s8<=4;
    CS_Distance9(i) = s9<=4;
    
    CS_Distance10(i) = s10<=4;
    CS_Distance11(i) = s11<=4;
    CS_Distance12(i) = s12<=4;
    CS_Distance13(i) = s13<=4;
    CS_Distance14(i) = s14<=4;
    CS_Distance15(i) = s15<=4;
    CS_Distance16(i) = s16<=4;
    CS_Distance17(i) = s17<=4;
    CS_Distance18(i) = s18<=4;
end

prob.Constraints.x3 = CS_Distance1;
prob.Constraints.x4 = CS_Distance2;
prob.Constraints.x5 = CS_Distance3;
prob.Constraints.x6 = CS_Distance4;
prob.Constraints.x7 = CS_Distance5;
prob.Constraints.x8 = CS_Distance6;
prob.Constraints.x9 = CS_Distance7;
prob.Constraints.x10 = CS_Distance8;
prob.Constraints.x11 = CS_Distance9;
prob.Constraints.x12 = CS_Distance10;
prob.Constraints.x13 = CS_Distance11;
prob.Constraints.x14 = CS_Distance12;
prob.Constraints.x15 = CS_Distance13;
prob.Constraints.x16 = CS_Distance14;
prob.Constraints.x17 = CS_Distance15;
prob.Constraints.x18 = CS_Distance16;
prob.Constraints.x19 = CS_Distance17;
prob.Constraints.x20 = CS_Distance18;


%教員が同じ時間に複数の科目が割当たらないようにする制約
CS_KyouinSubject = optimconstr(26,max(TeacherNo));
for i=1:26
    Kyouin = occupy(i,:) + occupy(i+26,:) + occupy(i+52,:) + occupy(i+78,:)...
        +occupy(i+104,:) + occupy(i+130,:) + occupy(i+156,:) + occupy(i+182,:)...
        +occupy(i+208,:)+occupy(i+234,:)+occupy(i+260,:) + occupy(i+286,:);
    for j=1:max(TeacherNo)
        KyouinSub = Kyouin .* (TeacherAndSubject(j,:));
        CS_KyouinSubject(i,j) = sum(KyouinSub)<=1;
    end 
end
prob.Constraints.c3 = CS_KyouinSubject;

%学年ごとに入る科目を決める制約
CS_Gakunen = optimconstr(1,9);
s=0;
for i=1:length(SP2)
    for j=131:156
    s = s + occupy(j,SP2(i)) ;
    end
end
CS_Gakunen(1) = s == length(SP2);

s=0;
for i=1:length(SP3)
    for j=157:182
    s = s + occupy(j,SP3(i)) ;
    end
end
CS_Gakunen(2) = s == length(SP3);

s=0;
for i=1:length(SM2)
    for j=235:260
    s = s + occupy(j,SM2(i)) ;
    end
end
CS_Gakunen(3) = s == length(SM2);

s=0;
for i=1:length(SM3)
    for j=261:286
    s = s + occupy(j,SM3(i)) ;
    end
end
CS_Gakunen(4) = s == length(SM3);

s=0;
for i=1:length(SK1)
    for j=1:26
    s = s + occupy(j,SK1(i)) ;
    end
end
CS_Gakunen(5) = s == length(SK1);

s=0;
for i=1:length(SK2)
    for j=27:52
    s = s + occupy(j,SK2(i)) ;
    end
end
CS_Gakunen(6) = s == length(SK2);

s=0;
for i=1:length(SK3)
    for j=53:78
    s = s + occupy(j,SK3(i)) ;
    end
end
CS_Gakunen(7) = s == length(SK3);

s=0;
for i=1:length(SE1)
    for j=1:26
    s = s + occupy(j,SE1(i)) ;
    end
end
CS_Gakunen(8) = s == length(SE1);

s=0;
for i=1:length(SE2)
    for j=27:52
    s = s + occupy(j,SE2(i)) ;
    end
end
CS_Gakunen(9) = s == length(SE2);

prob.Constraints.c4 = CS_Gakunen;

%2コマ分使用する科目は決められた時間にしか入らないようにする制約
%2コマ分使用する科目のすぐ後ろの時間は'空き'にする制約
TJ1=[1,3,4,6,8,9,11,13,14,15,17,19,20,22,24,25];
Kyoutsu_KOMA12 = optimconstr(1,length(SKJ31)+length(SKJ41));
Kyoutsu_KOMA22 = optimconstr(1,length(SKJ32)+length(SKJ42));
Kyoutsu_KOMA32 = optimconstr(1,length(SKJ33)+length(SKJ43));
CS_Kyoutsu_KOMA12KOMAHAIRETSU = optimconstr(length(SKJ31)+length(SKJ41),length(TJ1));
CS_Kyoutsu_KOMA22KOMAHAIRETSU = optimconstr(length(SKJ32)+length(SKJ42),length(TJ1));
CS_Kyoutsu_KOMA32KOMAHAIRETSU = optimconstr(length(SKJ33)+length(SKJ43),length(TJ1));
Kyoutsu_koma12=0;
Kyoutsu_koma22=0;
Kyoutsu_koma32=0;
SKJ1 = sort([SKJ31,SKJ41]);
SKJ2 = sort([SKJ32,SKJ42]);
SKJ3 = sort([SKJ33,SKJ43]);
for i=1:length(TJ1)
    for j=1:length(SKJ1)
        Kyoutsu_koma12 = Kyoutsu_koma12 + occupy(TJ1(i),SKJ1(j));
        CS_Kyoutsu_KOMA12KOMAHAIRETSU(j,i) = occupy(TJ1(i),SKJ1(j))+sum(occupy(TJ1(i)+1,:))<=1;
    end
    for k=1:length(SKJ2)
        Kyoutsu_koma22 = Kyoutsu_koma22 + occupy(TJ1(i)+26,SKJ2(k));
        CS_Kyoutsu_KOMA22KOMAHAIRETSU(k,i) = occupy(TJ1(i)+26,SKJ2(k))+sum(occupy(TJ1(i)+27,:))<=1;
    end
    for l=1:length(SKJ3)
        Kyoutsu_koma32 = Kyoutsu_koma32 + occupy(TJ1(i)+52,SKJ3(l)); 
        CS_Kyoutsu_KOMA32KOMAHAIRETSU(l,i) = occupy(TJ1(i)+52,SKJ3(l))+sum(occupy(TJ1(i)+53,:))<=1;
    end
end
prob.Constraints.c5 = Kyoutsu_koma12==length(SKJ1);
prob.Constraints.c6 = CS_Kyoutsu_KOMA12KOMAHAIRETSU;
prob.Constraints.c7 = Kyoutsu_koma22==length(SKJ2);
prob.Constraints.c8 = CS_Kyoutsu_KOMA22KOMAHAIRETSU;
prob.Constraints.c9 = Kyoutsu_koma32==length(SKJ3);
prob.Constraints.c10 = CS_Kyoutsu_KOMA32KOMAHAIRETSU;

for i=1:length(TJ1)
    Kyouin = occupy(TJ1(i)+1,:) + occupy(TJ1(i)+27,:)+ occupy(TJ1(i)+53,:)  + occupy(TJ1(i)+79,:)...
        +occupy(TJ1(i)+105,:) + occupy(TJ1(i)+131,:) + occupy(TJ1(i)+157,:) + occupy(TJ1(i)+183,:)...
        +occupy(TJ1(i)+209,:) + occupy(TJ1(i)+235,:) + occupy(TJ1(i)+261,:) + occupy(TJ1(i)+287,:);
    for j=1:max(TeacherNo)
        KyouinSub = Kyouin .* (TeacherAndSubject(j,:));
        for k1=1:length(SKJ1)
            cs_1(i,j,k1) = TeacherAndSubject(j,SKJ1(k1)) + sum(KyouinSub)<=1;
        end
        for k2=1:length(SKJ2)
            cs_2(i,j,k2) = TeacherAndSubject(j,SKJ2(k2)) + sum(KyouinSub)<=1;
        end
        for k3=1:length(SKJ3)
            cs_3(i,j,k3) = TeacherAndSubject(j,SKJ3(k3)) + sum(KyouinSub)<=1;
        end
    end 
end

prob.Constraints.xx1 = cs_1;
prob.Constraints.xx2 = cs_2;
prob.Constraints.xx3 = cs_3;

%共通科目（実験）の入った時間には専門科目が入らないようにする制約
CS_Kyoutsu_Jikken_Grade1_Subutsu = optimconstr(length(SKJ1),length(TJ1));
CS_Kyoutsu_Jikken_Grade2_Subutsu = optimconstr(length(SKJ2),length(TJ1));
CS_Kyoutsu_Jikken_Grade3_Subutsu = optimconstr(length(SKJ3),length(TJ1));
CS_Kyoutsu_Jikken_Grade1_Mate = optimconstr(length(SKJ1),length(TJ1));
CS_Kyoutsu_Jikken_Grade2_Mate = optimconstr(length(SKJ2),length(TJ1));
CS_Kyoutsu_Jikken_Grade3_Mate = optimconstr(length(SKJ3),length(TJ1));
for i=1:length(TJ1)
    for j=1:length(SKJ1)
        CS_Kyoutsu_Jikken_Grade1_Subutsu(j,i) = occupy(TJ1(i),SKJ1(j))...
            +sum(occupy(TJ1(i)+105,:))<=1;
        CS_Kyoutsu_Jikken_Grade1_Mate(j,i) = occupy(TJ1(i),SKJ1(j))...
            +sum(occupy(TJ1(i)+209,:))<=1;
    end
    for k=1:length(SKJ2)
        CS_Kyoutsu_Jikken_Grade2_Subutsu(k,i) = occupy(TJ1(i)+26,SKJ2(k))...
            +sum(occupy(TJ1(i)+131,:))<=1;
        CS_Kyoutsu_Jikken_Grade2_Mate(k,i) = occupy(TJ1(i)+26,SKJ2(k))...
            +sum(occupy(TJ1(i)+235,:))<=1;
    end
    for l=1:length(SKJ3)
        CS_Kyoutsu_Jikken_Grade3_Subutsu(l,i) = occupy(TJ1(i)+52,SKJ3(l))...
            +sum(occupy(TJ1(i)+157,:))<=1;
        CS_Kyoutsu_Jikken_Grade3_Mate(l,i) = occupy(TJ1(i)+52,SKJ3(l))...
            +sum(occupy(TJ1(i)+261,:))<=1;
    end
end
prob.Constraints.c121 = CS_Kyoutsu_Jikken_Grade1_Subutsu;
prob.Constraints.c131 = CS_Kyoutsu_Jikken_Grade2_Subutsu;
prob.Constraints.c141 = CS_Kyoutsu_Jikken_Grade3_Subutsu;
prob.Constraints.c122 = CS_Kyoutsu_Jikken_Grade1_Mate;
prob.Constraints.c132 = CS_Kyoutsu_Jikken_Grade2_Mate;
prob.Constraints.c142 = CS_Kyoutsu_Jikken_Grade3_Mate;



%共通科目（実験以外）の入った時間には専門科目が入らないようにする制約
s=0;
CS_Subutsu_Jikken = optimconstr(1,104);
for i=1:26
    for j=0:3
            s = sum(occupy(i+j*26,:)) + sum(occupy(104+i+j*26,:));
             CS_Subutsu_Jikken(1,i+j*26) = s<=1;
    end
end
prob.Constraints.c15 = CS_Subutsu_Jikken;

s=0;
CS_Mate_Jikken = optimconstr(1,104);
for i=1:26
    for j=0:3
            s = sum(occupy(i+j*26,:)) + sum(occupy(208+i+j*26,:));
             CS_Mate_Jikken(1,i+j*26) = s<=1;
    end
end
prob.Constraints.c16 = CS_Mate_Jikken;

Pankyo(1) = occupy(2,31)==1;
Pankyo(2) = occupy(4,32)==1;
Pankyo(3) = occupy(5,33)==1;
Pankyo(4) = occupy(6,34)==1;
Pankyo(5) = occupy(11,35)==1;
Pankyo(6) = occupy(12,36)==1;
Pankyo(7) = occupy(13,37)==1;
Pankyo(8) = occupy(15,38)==1;
Pankyo(9) = occupy(16,39)==1;
Pankyo(10) = occupy(18,40)==1;
Pankyo(11) = occupy(22,41)==1;
Pankyo(12) = occupy(28,42)==1;
Pankyo(13) = occupy(32,43)==1;
Pankyo(14) = occupy(33,44)==1;
Pankyo(15) = occupy(42,45)==1;
Pankyo(16) = occupy(44,46)==1;
prob.Constraints.c13 = Pankyo;

options = optimoptions('intlinprog');
options.MaxTime=3e4;
options.AbsoluteGapTolerance=2;
options
[soln,fval,exitflag,output] = solve(prob,'Options',options);

%load handel.mat; sound(y,Fs);



%以下，結果表示
%各スロットに何の科目が入ったかを読み込む．
for i=1:SlotNo
    if isempty(find(soln.occupy(i,:)))
        table(i) = 0;
    else
        table(i) = find(soln.occupy(i,:));
    end
end

jikan = strings(12,26);

%時間割の形に整形
for i=0:11
    for j =1:26
        if table(26*i+j)==0
            jikan(i+1,j)='空き';
        else
            jikan(i+1,j)=Subject(table(26*i+j));
        end
    end
end

disp(jikan)%結果の表示


for i=1:104
    if isempty(find(soln.occupy(i,:)))
        if isempty(find(soln.occupy(i+104,:)))
            table(i) = 0;
        else
            table(i)=find(soln.occupy(i+104,:));
        end
    else
        table(i) = find(soln.occupy(i,:));
    end
end

Subutsu_jikanwari=strings(4,26);
for i=0:3
    for j =1:26
        if table(26*i+j)==0
            Subutsu_jikanwari(i+1,j)='空き';
        else
            Subutsu_jikanwari(i+1,j)=Subject(table(26*i+j));
        end
    end
end
disp(Subutsu_jikanwari);

Mate_jikanwari = strings(4,26);
for i=1:104
    if isempty(find(soln.occupy(i,:)))
        if isempty(find(soln.occupy(i+208,:)))
            table(i) = 0;
        else
            table(i)=find(soln.occupy(i+208,:));
        end
    else
        table(i) = find(soln.occupy(i,:));
    end
end

Mate_jikanwari=strings(4,26);
for i=0:3
    for j =1:26
        if table(26*i+j)==0
            Mate_jikanwari(i+1,j)='空き';
        else
            Mate_jikanwari(i+1,j)=Subject(table(26*i+j));
        end
    end
end
disp(Mate_jikanwari);

Slotid = fopen('Slot.csv');
D = textscan(Slotid,'%s');
fclose(Slotid);

for i=1:26
    Slots(i)=D{1}(i);
end
writematrix([Slots; jikan; Slots; Subutsu_jikanwari; Slots; Mate_jikanwari],'jikanwari20200227Distance.csv')%結果をcsv形式で書き出し

%disp(soln.occupy2);

%writematrix(soln.occupy2,'occupy2_20200211Distance.csv')%結果をcsv形式で書き出し
