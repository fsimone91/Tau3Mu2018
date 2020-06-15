from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsToPhiMuMuPi_MC_generation_2018_10_2_X'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '/lustrehome/venditti/Tau3Mu2018_final/CMSSW_10_2_1/src/CrabSubmission/'

config.Data.outputPrimaryDataset = 'DsToPhiMuMuPi_CMSSW_10_2_X_2018'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000000
NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = 10000000000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'DsToPhiMuMuPi_MC_generation_2018_10_2_X'

config.Site.storageSite = 'T2_IT_Bari'
