from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsToPhiMuMuPi_CMSSW_10_2_X_2018_RECO_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/CrabSubmission/MC/TSG-RunIIAutumn18DR-step3_cfg.py'
config.Data.inputDataset = '/DsToPhiMuMuPi_CMSSW_10_2_X_2018/fsimone-DsToPhiMuMuPi_CMSSW_10_2_X_2018-2c9912c72108c252c02b22bd1c4743d6/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'DsToPhiMuMuPi_CMSSW_10_2_X_2018_RECO_v1'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist =True
config.Site.whitelist = ['T2_IT_Bari']
config.JobType.maxMemoryMB = 2500
