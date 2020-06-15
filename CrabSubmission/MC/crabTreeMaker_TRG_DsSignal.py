from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Skim_TRG_Tau3Mu_DsToTauTo3Mu_2018_CMSSW_10_2_1_v0'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/SkimTools/SkimTrigger/test/run_TriggerTreeMaker_MC_cfg.py'
config.Data.inputDataset = '/DsToTau_TauTo3Mu_March2020/wangjian-RunIIAutumn18DRPremix-102X-2f1667a4ab974bdf4cb2916f291c3603/USER'
config.Data.inputDBS = 'phys03'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'Skim_TRG_Tau3Mu_DsToTauTo3Mu_2018_CMSSW_10_2_1_v0'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
config.Site.ignoreGlobalBlacklist  = True
