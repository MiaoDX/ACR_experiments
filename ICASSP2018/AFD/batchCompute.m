%run('D:\Code\lib&Utility\vlfeat-0.9.20\toolbox\vl_setup');
run('H:\projects\graduation_project_codebase\ACR_experiments\ICASSP2018\AFD\vlfeat-0.9.20\toolbox\vl_setup')

rootdir = 'F:\research&project\Our_Paper\PAMI2017_Camera6dRelocation\results\repairEvaluation\data\';
subdirs = dir(rootdir);
num =  numel(subdirs);
for i =  1 : num
    subdir = subdirs(i); 
    if(strcmp(subdir.name,'.') || strcmp(subdir.name,'..') || ~subdir.isdir)
        continue;
    end
    
    fullsubdir = fullfile(rootdir, subdir.name); 
    CalculateOne(fullsubdir);
end