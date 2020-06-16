from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SkimTau3Mu_BdToTauTo3Mu_2018_CMSSW_10_2_1_v10'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/SkimTools/SkimTau3Mu/test/run_TreeMaker_MC_cfg.py'
config.Data.inputDataset = '/BdTau3Mu/bjoshi-CRAB3_MC2018_BdTau3Mu_13TeV_DIGI-87600497c2c6a5767aee5d92666e59c3/USER'
config.Data.inputDBS = 'phys03'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SkimTau3Mu_BdToTauTo3Mu_2018_CMSSW_10_2_1_v10'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
#config.Site.ignoreGlobalBlacklist  = True
