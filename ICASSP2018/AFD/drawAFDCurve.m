clear all;
clc;

file1 = './ourAlgorithm/scene1_2/allAFD.mat';
file2 = './theoreticalAlgorithm/scene1_2/allAFD.mat';

load(file1);
AFD1 = allAFD(:,2);
mean1 = mean(AFD1);
variance1 = var(AFD1);

load(file2);
AFD2 = allAFD(:,2);
mean2 = mean(AFD2);
variance2 = var(AFD2);
x =  1 : 10;

h = figure;
plot(x,AFD1,'r-*','LineWidth',2);
hold on;
plot(x,AFD2,'b-x','LineWidth',2);
xlabel('Number');
ylabel('AFD');
legend('Our Algorithm','theoretical');
print(h,'-depsc','afd_scene1_2.eps');
save('afd_scene1_2.mat','mean1','mean2','variance1','variance2','AFD1','AFD2');
