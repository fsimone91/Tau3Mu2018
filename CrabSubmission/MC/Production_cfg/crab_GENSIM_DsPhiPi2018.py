from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsToPhiMuMuPi_MC_generation_2018_10_2_X_v0'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/CrabSubmission/MC/DsPhiPi_step1_cfg.py'

config.Data.outputPrimaryDataset = 'DsToPhiMuMuPi_CMSSW_10_2_X_2018'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000000
config.Data.totalUnits = 10000000000
config.JobType.eventsPerLumi = 10000;
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'DsToPhiMuMuPi_MC_generation_2018_10_2_X_v0'
config.JobType.allowUndistributedCMSSW = True 
config.Site.storageSite = 'T2_IT_Bari'
