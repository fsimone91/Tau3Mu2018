from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SkimPhiPi_DoubleMuonLowMass_Run2017F_19Aug_newSplit'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/venditti/Tau3MU_29072019/CMSSW_9_4_4/src/DsPhiPiTreeMaker/DsPhiPiTreeMaker/test/run_Data_DsPhiPiSkimAndTree_cfg.py'

config.Data.inputDataset = '/DoubleMuonLowMass/Run2017F-17Nov2017-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
#config.Data.runRange = '193093-193999' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'SkimPhiPi_DoubleMuonLowMass_Run2017F_19Aug_newSplit'
config.JobType.allowUndistributedCMSSW = True
config.Site.storageSite = 'T2_IT_Bari'


