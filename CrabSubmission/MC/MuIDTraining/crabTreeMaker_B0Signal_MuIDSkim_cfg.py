from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SkimMuID_B0Tau3Mu_2018_CMSSW_10_2_1_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.Data.inputDataset = '/B0ToTau_TauTo3Mu/wangjian-CRAB3_RunIIAutumn18DR_AODSIM-87600497c2c6a5767aee5d92666e59c3/USER'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/SkimTools/SkimTau3Mu/test/run_MC_2018_PatAndTree_MuonID_cfg.py'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 7
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SkimMuID_B0Tau3Mu_2018_CMSSW_10_2_1_v1'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True
