clear all;
clc;

file1 = './ourAlgorithm/scene1_2/stepnum.txt';
file2 = './theoreticalAlgorithm/scene1_2/stepnum.txt';

iteration1 = load(file1);
mean1 = mean(iteration1);
variance1 = var(iteration1);

iteration2full = load(file2);
iteration2 = iteration2full(:,3);
mean2_1 = mean(iteration2full(:,1));
mean2_2 = mean(iteration2full(:,2));
mean2 = mean(iteration2);
variance2 = var(iteration2);

x =  1 : 10;

figure;
plot(x,iteration1','r-*','LineWidth',2);
hold on;
plot(x,iteration2','b-x','LineWidth',2);
xlabel('Number');
ylabel('#Iteration');
legend('Our Algorithm','Theoretical Strategy');
