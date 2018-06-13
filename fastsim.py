# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: MinBias_13TeV_pythia8_TuneCUETP8M1_cfi --conditions auto:run2_mc --fast -n 1000 --era Run2_25ns --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,RECO --datatier GEN-SIM-DIGI-RECO --beamspot Realistic25ns13TeVEarly2017Collision --no_exec --filetype=LHE --filein=file:unweighted_events.lhe
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:LM1_13.lhe'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*', 
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('MinBias_13TeV_pythia8_TuneCUETP8M1_cfi nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('fastsimtest.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring('BeamRemnants:unresolvedHadron = 3'), 
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters'
                                    )
        )
)

# process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    # PythiaParameters = cms.PSet(
        # JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
            # 'JetMatching:scheme = 1', 
            # 'JetMatching:merge = on', 


            # 'JetMatching:jetAlgorithm = 2', 
            # 'JetMatching:etaJetMax = 5.', 
            # 'JetMatching:coneRadius = 1.', 
            # 'JetMatching:slowJetPower = 1', 
            # 'JetMatching:qCut = 20.', 
            # 'JetMatching:nQmatch = 5', 
            # 'JetMatching:nJetMax = 4', 
            # 'JetMatching:doShowerKt = off'),
        # parameterSets = cms.vstring('pythia8CommonSettings', 
            # 'pythia8CUEP8M1Settings', 
            # 'processParameters', 
            # 'JetMatchingParameters'),
        # processParameters = cms.vstring('15:onMode = off', 
            # '15:onIfMatch = 16 -211 111'),
        # pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            # 'Tune:ee 7', 
            # 'MultipartonInteractions:pT0Ref=2.4024', 
            # 'MultipartonInteractions:ecmPow=0.25208', 
            # 'MultipartonInteractions:expPow=1.6'),
        # pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            # 'Main:timesAllowErrors = 10000', 
            # 'Check:epTolErr = 0.01', 
            # 'Beams:setProductionScalesFromLHEF = off', 
            # 'SLHA:keepSM = on', 
            # 'SLHA:minMassSM = 1000.', 
            # 'ParticleDecays:limitTau0 = on', 
            # 'ParticleDecays:tau0Max = 10', 
            # 'ParticleDecays:allowPhotonRadiation = on')
    # ),
    # comEnergy = cms.double(13000.0),
    # filterEfficiency = cms.untracked.double(1.0),
    # maxEventsToPrint = cms.untracked.int32(1),
    # pythiaHepMCVerbosity = cms.untracked.bool(False),
    # pythiaPylistVerbosity = cms.untracked.int32(1)
# )

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
