close all;

afd_practical = [
1.17731483	0.571145704	0.937197261	0.589384992	0.390780917	0.575711616	0.684315461	0.997901135	1.74838691	0.746437436;
1.729365442	0.617139199	0.665767943	0.481578645	1.06044103	0.501176561	0.730619397	0.482526675	1.078868529	1.117730807;
1.059149642	0.396488183	1.304594507	1.556995002	1.459878088	1.093330438	1.237019138	0.640585874	0.710171439	0.66882371;
1.414607192	1.509844829	0.849737716	1.12888948	1.133954106	0.545563409	0.682287572	0.853356025	0.817741799	0.921962199;
0.669201358	0.773266924	0.552375585	0.764226655	0.943136882	0.501833919	0.64999545	0.825664592	1.037437153	0.992116866;];

afd_theoretical = [
12.46197321	15.30152097	2.118099636	12.87053978	15.58801253	3.111072765	3.610544136	13.31785601	6.209885877	13.66500174;
13.26713957	13.00321412	13.17884256	13.4025513	13.3310972	13.24006275	13.40846249	13.27487012	13.73907585	13.84397688;
19.80349438	24.35593581	24.9746351	26.13007575	25.06393987	25.71163494	26.08590926	28.89086466	25.76688091	28.03028432;
5.536037045	5.880578303	17.53686638	2.210410487	10.11410332	2.230001727	8.365743	7.481833047	3.850363155	5.96903114;
7.796812622	5.588813048	25.81874734	13.77075891	21.16128273	5.216764967	11.13090493	4.187152556	12.74355638	2.47835304;];

figure;
x =  1 : 10;
for i =  1:5
    y_p = afd_practical(i,:);
    plot(x, y_p, 'r-*');hold on;
    y_t = afd_theoretical(i,:);
    plot(x, y_t, 'b-+');hold on;
end


iteration_practical = [
10	9	9	10	11	10	9	11	9	10;
9	10	13	10	11	11	11	9	11	9;
12	9	10	12	15	14	15	10	10	11;
11	10	14	11	10	13	15	9	13	14;
12	11	14	10	11	14	12	12	13	12;];

iteration_theoretical = [
15	20	17	17	21	27	19	13	28	13;
14	14	15	15	13	13	13	14	15	18;
13	14	22	24	16	22	25	16	22	21;
19	17	19	22	21	13	20	19	21	21;
17	15	16	18	15	20	17	23	19	17;   
];

figure;
for i =  1:5
    y_p = iteration_practical(i,:);
    plot(x, y_p, 'r-*');hold on;
    y_t = iteration_theoretical(i,:);
    plot(x, y_t, 'b-+');hold on;
end

lw = 1.5;

afd_practical_mean = mean(afd_practical,2);
afd_practical_var = std(afd_practical,0,2);
afd_theoretical_mean = mean(afd_theoretical,2);
afd_theoretical_var = std(afd_theoretical,0,2);
figure;
x =  1 : 5;
errorbar(x,afd_practical_mean,afd_practical_var,'r','LineWidth',lw); hold on;
errorbar(x,afd_theoretical_mean,afd_theoretical_var,'b','LineWidth',lw); hold on;
legend('effective','straightforward');
ylabel('AFD');

it_practical_mean = mean(iteration_practical,2);
it_practical_var = std(iteration_practical,0,2);
it_theoretical_mean = mean(iteration_theoretical,2);
it_theoretical_var = std(iteration_theoretical,0,2);
figure;
x = 1 : 5;
errorbar(x,it_practical_mean,it_practical_var,'r','LineWidth',lw); hold on;
errorbar(x,it_theoretical_mean,it_theoretical_var,'b','LineWidth',lw); hold on;
legend('effective','straightforward');
ylabel('Iteration Number');