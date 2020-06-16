import FWCore.ParameterSet.Config as cms

process = cms.Process('Tau3MuSkim')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load("SkimTools.SkimTau3Mu.Tau3MuSkimAOD_MC_cff")
process.load("SkimTools.SkimTau3Mu.Tau3MuSkimAOD_BParking_cff")
process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v20' #MC2018 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cmsxrootd.fnal.gov//store/user/wangjian/DsToTau_TauTo3Mu/CRAB3_RunIIAutumn18DR_AODSIM/191120_085131/0000/TSG-RunIIAutumn18DR-00006_804.root',
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH1/AOD/05May2019-v1/280013/BC7F8403-4E85-5C4C-8A46-40E88B2DC7C2.root',
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH1/AOD/05May2019-v1/280013/AEC067D7-F97E-A34A-993C-B20E048E0250.root',
        #'root://xrootd-cms.infn.it//store/data/Run2018A/DoubleMuonLowMass/AOD/17Sep2018-v1/120000/3C6EECC5-5787-AC43-ACF0-3BE40CE1291C.root',
        #root://xrootd-cms.infn.it//store/data/Run2017F/DoubleMuonLowMass/AOD/09May2018-v1/80000/AECC4C56-BAB0-E811-B92A-008CFA1979AC.root'


    )
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("TreeData.root"))


process.TreeMakerBkg = cms.EDAnalyzer("MiniAna2017Tree",
                              isMcLabel = cms.untracked.bool(True),
                              isAnaLabel = cms.untracked.bool(True),
                              isBParkingLabel = cms.untracked.bool(True),        
                              muonLabel=cms.InputTag("looseMuons"),
                              VertexLabel=cms.InputTag("offlinePrimaryVertices"),
                              genParticleLabel=cms.InputTag("genParticles"),
                              pileupSummary = cms.InputTag("addPileupInfo"),
                              Cand3MuLabel=cms.InputTag("ThreeMuonsVtxKalmanFit"),
                              triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
                              triggerSummary = cms.InputTag("hltTriggerSummaryAOD", "", "HLT"),
                              AlgInputTag = cms.InputTag( "gtStage2Digis" )
)




process.Tau3MuSkim = cms.Path(process.ThreeMuonSelSeq*
                              process.TreeMakerBkg
                     )






