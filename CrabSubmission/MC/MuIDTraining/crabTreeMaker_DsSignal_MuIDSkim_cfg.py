from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SkimMuID_B0Tau3Mu_2018_CMSSW_10_2_1_v3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.Data.inputDataset = 

config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/SkimTools/SkimTau3Mu/test/run_MC_2018_PatAndTree_MuonID_cfg.py'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 7
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SkimMuID_B0Tau3Mu_2018_CMSSW_10_2_1_v3'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True
