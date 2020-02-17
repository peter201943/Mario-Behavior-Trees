

## CS 387: Game AI


---------


# HW3: Mario Behavior Trees


## About
 - **Student**
     - Peter J. Mangelsdorf
     - pjm349@drexel.edu
     - 717-385-7068
 - **Professor**
     - Ehsan Khosroshahi
     - eb452@drexel.edu
 - **Contents8*
     - [About](#about)
     - [Project Structure](#project-structure)
     - [Structure Analysis](#structure-analysis)
     - [Structural Additions](#structural-additions)
     - [Structural Additions Annotated](#structural-additions-annotated)


---------


## Project Structure
```bash
Standard Access@SHODAN /cygdrive/c/Users/Standard Access/Peter/School/College/3 - Junior/CS 387/Projects/HW 3
$ tree .
.
├── bin
│   ├── AmiCoBuild
│   │   └── PyJava
│   │       ├── AmiCoPyJava.dll
│   │       ├── AmiCoPyJava.exp
│   │       ├── AmiCoPyJava.lib
│   │       ├── ch
│   │       │   └── idsia
│   │       │       ├── agents
│   │       │       │   ├── Agent.class
│   │       │       │   ├── AgentsPool.class
│   │       │       │   ├── AmiCoAgent.class
│   │       │       │   ├── BasicLearningAgent.class
│   │       │       │   ├── controllers
│   │       │       │   │   ├── BasicMarioAIAgent.class
│   │       │       │   │   ├── ForwardAgent.class
│   │       │       │   │   ├── ForwardJumpingAgent.class
│   │       │       │   │   ├── human
│   │       │       │   │   │   ├── CheaterKeyboardAgent.class
│   │       │       │   │   │   └── HumanKeyboardAgent.class
│   │       │       │   │   ├── RandomAgent.class
│   │       │       │   │   ├── ReplayAgent.class
│   │       │       │   │   ├── ScaredAgent.class
│   │       │       │   │   ├── ScaredShooty.class
│   │       │       │   │   └── TimingAgent.class
│   │       │       │   ├── learning
│   │       │       │   │   ├── LargeMLPAgent.class
│   │       │       │   │   ├── LargeSRNAgent.class
│   │       │       │   │   ├── MediumMLPAgent.class
│   │       │       │   │   ├── MediumSRNAgent.class
│   │       │       │   │   ├── SimpleMLPAgent.class
│   │       │       │   │   ├── SmallMLPAgent.class
│   │       │       │   │   ├── SmallSRNAgent.class
│   │       │       │   │   └── SRNAgent.class
│   │       │       │   ├── LearningAgent.class
│   │       │       │   ├── MLPESLearningAgent.class
│   │       │       │   ├── SimpleAgent.class
│   │       │       │   └── SRNESLearningAgent.class
│   │       │       ├── benchmark
│   │       │       │   ├── experiments
│   │       │       │   │   ├── EpisodicExperiment.class
│   │       │       │   │   └── Experiment.class
│   │       │       │   ├── mario
│   │       │       │   │   ├── engine
│   │       │       │   │   │   ├── Art.class
│   │       │       │   │   │   ├── BgRenderer.class
│   │       │       │   │   │   ├── GeneralizerEnemies.class
│   │       │       │   │   │   ├── GeneralizerLevelScene.class
│   │       │       │   │   │   ├── GlobalOptions.class
│   │       │       │   │   │   ├── level
│   │       │       │   │   │   │   ├── BgLevelGenerator.class
│   │       │       │   │   │   │   ├── ImprovedNoise.class
│   │       │       │   │   │   │   ├── Level$objCounters.class
│   │       │       │   │   │   │   ├── Level.class
│   │       │       │   │   │   │   ├── LevelGenerator.class
│   │       │       │   │   │   │   └── SpriteTemplate.class
│   │       │       │   │   │   ├── LevelRenderer.class
│   │       │       │   │   │   ├── LevelScene.class
│   │       │       │   │   │   ├── mapedit
│   │       │       │   │   │   │   ├── LevelEditor$1.class
│   │       │       │   │   │   │   ├── LevelEditor.class
│   │       │       │   │   │   │   ├── LevelEditView.class
│   │       │       │   │   │   │   └── TilePicker.class
│   │       │       │   │   │   ├── MarioVisualComponent.class
│   │       │       │   │   │   ├── Recorder.class
│   │       │       │   │   │   ├── Replayer.class
│   │       │       │   │   │   ├── resources
│   │       │       │   │   │   │   ├── bgsheet.png
│   │       │       │   │   │   │   ├── endscene.gif
│   │       │       │   │   │   │   ├── enemysheet.png
│   │       │       │   │   │   │   ├── firemariosheet.png
│   │       │       │   │   │   │   ├── font.gif
│   │       │       │   │   │   │   ├── itemsheet.png
│   │       │       │   │   │   │   ├── logo.gif
│   │       │       │   │   │   │   ├── mapsheet.png
│   │       │       │   │   │   │   ├── mariosheet.png
│   │       │       │   │   │   │   ├── particlesheet.png
│   │       │       │   │   │   │   ├── princess.png
│   │       │       │   │   │   │   ├── racoonmariosheet.png
│   │       │       │   │   │   │   ├── smallmariosheet.png
│   │       │       │   │   │   │   ├── test.lvl
│   │       │       │   │   │   │   ├── tiles.dat
│   │       │       │   │   │   │   └── worldmap.png
│   │       │       │   │   │   └── sprites
│   │       │       │   │   │       ├── BulletBill.class
│   │       │       │   │   │       ├── CoinAnim.class
│   │       │       │   │   │       ├── Enemy.class
│   │       │       │   │   │       ├── Fireball.class
│   │       │       │   │   │       ├── FireFlower.class
│   │       │       │   │   │       ├── FlowerEnemy.class
│   │       │       │   │   │       ├── GreenMushroom.class
│   │       │       │   │   │       ├── Mario.class
│   │       │       │   │   │       ├── Mushroom.class
│   │       │       │   │   │       ├── Particle.class
│   │       │       │   │   │       ├── Princess.class
│   │       │       │   │   │       ├── Shell.class
│   │       │       │   │   │       ├── Sparkle.class
│   │       │       │   │   │       ├── Sprite.class
│   │       │       │   │   │       ├── SpriteContext.class
│   │       │       │   │   │       └── WaveGoomba.class
│   │       │       │   │   ├── environments
│   │       │       │   │   │   ├── Environment.class
│   │       │       │   │   │   └── MarioEnvironment.class
│   │       │       │   │   └── simulation
│   │       │       │   │       ├── AmiCoSimulator.class
│   │       │       │   │       └── SimulationOptions.class
│   │       │       │   └── tasks
│   │       │       │       ├── BasicTask.class
│   │       │       │       ├── GamePlayTask.class
│   │       │       │       ├── LearningTask.class
│   │       │       │       ├── MarioCustomSystemOfValues.class
│   │       │       │       ├── MarioSystemOfValues$timeLengthMapping.class
│   │       │       │       ├── MarioSystemOfValues.class
│   │       │       │       ├── MultiDifficultyProgressTask.class
│   │       │       │       ├── MultiSeedProgressTask.class
│   │       │       │       ├── MushroomTask.class
│   │       │       │       ├── ProgressTask.class
│   │       │       │       ├── ReplayTask.class
│   │       │       │       ├── SystemOfValues.class
│   │       │       │       └── Task.class
│   │       │       ├── evolution
│   │       │       │   ├── ea
│   │       │       │   │   └── ES.class
│   │       │       │   ├── EA.class
│   │       │       │   ├── Evolvable.class
│   │       │       │   ├── FA.class
│   │       │       │   ├── MLP.class
│   │       │       │   └── SRN.class
│   │       │       ├── scenarios
│   │       │       │   ├── champ
│   │       │       │   │   ├── GamePlayTrack.class
│   │       │       │   │   ├── LearningTrack.class
│   │       │       │   │   └── TuringTestTrack.class
│   │       │       │   ├── Custom.class
│   │       │       │   ├── Main.class
│   │       │       │   ├── oldscenarios
│   │       │       │   │   ├── CompetitionScore.class
│   │       │       │   │   ├── Evolve.class
│   │       │       │   │   ├── EvolveIncrementally.class
│   │       │       │   │   ├── EvolveMultiSeed.class
│   │       │       │   │   ├── GeneralScenario.class
│   │       │       │   │   ├── MainRun.class
│   │       │       │   │   └── Stats.class
│   │       │       │   ├── Play.class
│   │       │       │   ├── Replay.class
│   │       │       │   └── test
│   │       │       │       ├── EvaluateJLink.class
│   │       │       │       ├── EvolveSingle.class
│   │       │       │       ├── EvolveWithChangingSeeds.class
│   │       │       │       ├── PaperEvolve.class
│   │       │       │       ├── PaperEvolveBatch.class
│   │       │       │       ├── PlayJLink.class
│   │       │       │       ├── StatsJLink.class
│   │       │       │       └── StochasticityTest.class
│   │       │       ├── tools
│   │       │       │   ├── amico
│   │       │       │   │   └── AmiCoJavaPy.class
│   │       │       │   ├── EvaluationInfo.class
│   │       │       │   ├── EvaluationInfoStatisticalSummary.class
│   │       │       │   ├── Evaluator.class
│   │       │       │   ├── GameViewer$1.class
│   │       │       │   ├── GameViewer$GameViewerActions.class
│   │       │       │   ├── GameViewer$GameViewerView.class
│   │       │       │   ├── GameViewer.class
│   │       │       │   ├── MarioAIOptions.class
│   │       │       │   ├── RandomCreatureGenerator.class
│   │       │       │   ├── ReplayerOptions$Interval.class
│   │       │       │   ├── ReplayerOptions.class
│   │       │       │   ├── Scale2x.class
│   │       │       │   ├── StateEncoderDecoder.class
│   │       │       │   ├── ToolsConfigurator$INTERFACE_TYPE.class
│   │       │       │   ├── ToolsConfigurator$ToolsConfiguratorActions.class
│   │       │       │   └── ToolsConfigurator.class
│   │       │       ├── unittests
│   │       │       │   ├── CmdLineOptionsTest.class
│   │       │       │   ├── LevelGeneratorTest.class
│   │       │       │   ├── LevelSceneTest.class
│   │       │       │   ├── MarioAIBenchmarkTest.class
│   │       │       │   └── MarioEnvironmentTest.class
│   │       │       └── utils
│   │       │           ├── ErrorCodes.class
│   │       │           ├── MathX.class
│   │       │           ├── ParameterContainer.class
│   │       │           ├── statistics
│   │       │           │   ├── StatisticalSummary$Watch.class
│   │       │           │   ├── StatisticalSummary.class
│   │       │           │   ├── StatisticalTests.class
│   │       │           │   └── Stats.class
│   │       │           └── wox
│   │       │               └── serial
│   │       │                   ├── AccessTest$Sub.class
│   │       │                   ├── AccessTest$Super.class
│   │       │                   ├── AccessTest.class
│   │       │                   ├── ArrayListTest.class
│   │       │                   ├── Easy.class
│   │       │                   ├── EasyTest.class
│   │       │                   ├── EncodeBase64.class
│   │       │                   ├── ObjectReader.class
│   │       │                   ├── ObjectWriter.class
│   │       │                   ├── ReadTest.class
│   │       │                   ├── Serial.class
│   │       │                   ├── ShadowTest$X.class
│   │       │                   ├── ShadowTest$Y.class
│   │       │                   ├── ShadowTest.class
│   │       │                   ├── SimpleReader.class
│   │       │                   ├── SimpleWriter.class
│   │       │                   ├── TestObject$Inner.class
│   │       │                   ├── TestObject.class
│   │       │                   ├── Util.class
│   │       │                   └── WriterTest.class
│   │       ├── DemoForwardAgent.py
│   │       ├── DemoForwardJumpingAgent.py
│   │       ├── Dima_agent.py
│   │       ├── Dima_agent.pyc
│   │       ├── DimaAgent.py
│   │       ├── evaluationinfo.py
│   │       ├── evaluationinfo.pyc
│   │       ├── forwardagent.py
│   │       ├── forwardjumpingagent.py
│   │       ├── forwardjumpingagent.pyc
│   │       ├── marioagent.py
│   │       └── marioagent.pyc
│   └── MarioAI
│       ├── ch
│       │   └── idsia
│       │       ├── agents
│       │       │   ├── Agent.class
│       │       │   ├── AgentLoader.class
│       │       │   ├── AgentsPool.class
│       │       │   ├── AmiCoAgent.class
│       │       │   ├── BasicLearningAgent.class
│       │       │   ├── controllers
│       │       │   │   ├── BasicMarioAIAgent.class
│       │       │   │   ├── ForwardAgent.class
│       │       │   │   ├── ForwardJumpingAgent.class
│       │       │   │   ├── human
│       │       │   │   │   ├── CheaterKeyboardAgent.class
│       │       │   │   │   └── HumanKeyboardAgent.class
│       │       │   │   ├── RandomAgent.class
│       │       │   │   ├── ReplayAgent.class
│       │       │   │   ├── ScaredAgent.class
│       │       │   │   ├── ScaredShooty.class
│       │       │   │   └── TimingAgent.class
│       │       │   ├── learning
│       │       │   │   ├── LargeMLPAgent.class
│       │       │   │   ├── LargeSRNAgent.class
│       │       │   │   ├── MediumMLPAgent.class
│       │       │   │   ├── MediumSRNAgent.class
│       │       │   │   ├── SimpleMLPAgent.class
│       │       │   │   ├── SmallMLPAgent.class
│       │       │   │   ├── SmallSRNAgent.class
│       │       │   │   └── SRNAgent.class
│       │       │   ├── LearningAgent.class
│       │       │   ├── MLPESLearningAgent.class
│       │       │   ├── SimpleAgent.class
│       │       │   └── SRNESLearningAgent.class
│       │       ├── benchmark
│       │       │   ├── experiments
│       │       │   │   ├── EpisodicExperiment.class
│       │       │   │   └── Experiment.class
│       │       │   ├── mario
│       │       │   │   ├── engine
│       │       │   │   │   ├── Art.class
│       │       │   │   │   ├── BgRenderer.class
│       │       │   │   │   ├── GeneralizerEnemies.class
│       │       │   │   │   ├── GeneralizerLevelScene.class
│       │       │   │   │   ├── GlobalOptions.class
│       │       │   │   │   ├── level
│       │       │   │   │   │   ├── BgLevelGenerator.class
│       │       │   │   │   │   ├── ImprovedNoise.class
│       │       │   │   │   │   ├── Level$objCounters.class
│       │       │   │   │   │   ├── Level.class
│       │       │   │   │   │   ├── LevelGenerator.class
│       │       │   │   │   │   └── SpriteTemplate.class
│       │       │   │   │   ├── LevelRenderer.class
│       │       │   │   │   ├── LevelScene.class
│       │       │   │   │   ├── mapedit
│       │       │   │   │   │   ├── LevelEditor$1.class
│       │       │   │   │   │   ├── LevelEditor.class
│       │       │   │   │   │   ├── LevelEditView.class
│       │       │   │   │   │   └── TilePicker.class
│       │       │   │   │   ├── MarioVisualComponent.class
│       │       │   │   │   ├── Recorder.class
│       │       │   │   │   ├── Replayer.class
│       │       │   │   │   ├── resources
│       │       │   │   │   │   ├── bgsheet.png
│       │       │   │   │   │   ├── endscene.gif
│       │       │   │   │   │   ├── enemysheet.png
│       │       │   │   │   │   ├── firemariosheet.png
│       │       │   │   │   │   ├── font.gif
│       │       │   │   │   │   ├── itemsheet.png
│       │       │   │   │   │   ├── logo.gif
│       │       │   │   │   │   ├── mapsheet.png
│       │       │   │   │   │   ├── mariosheet.png
│       │       │   │   │   │   ├── particlesheet.png
│       │       │   │   │   │   ├── princess.png
│       │       │   │   │   │   ├── racoonmariosheet.png
│       │       │   │   │   │   ├── smallmariosheet.png
│       │       │   │   │   │   ├── test.lvl
│       │       │   │   │   │   ├── tiles.dat
│       │       │   │   │   │   └── worldmap.png
│       │       │   │   │   └── sprites
│       │       │   │   │       ├── BulletBill.class
│       │       │   │   │       ├── CoinAnim.class
│       │       │   │   │       ├── Enemy.class
│       │       │   │   │       ├── Fireball.class
│       │       │   │   │       ├── FireFlower.class
│       │       │   │   │       ├── FlowerEnemy.class
│       │       │   │   │       ├── GreenMushroom.class
│       │       │   │   │       ├── Mario.class
│       │       │   │   │       ├── Mushroom.class
│       │       │   │   │       ├── Particle.class
│       │       │   │   │       ├── Princess.class
│       │       │   │   │       ├── Shell.class
│       │       │   │   │       ├── Sparkle.class
│       │       │   │   │       ├── Sprite.class
│       │       │   │   │       ├── SpriteContext.class
│       │       │   │   │       └── WaveGoomba.class
│       │       │   │   ├── environments
│       │       │   │   │   ├── Environment.class
│       │       │   │   │   └── MarioEnvironment.class
│       │       │   │   └── simulation
│       │       │   │       ├── AmiCoSimulator.class
│       │       │   │       └── SimulationOptions.class
│       │       │   └── tasks
│       │       │       ├── BasicTask.class
│       │       │       ├── GamePlayTask.class
│       │       │       ├── LearningTask.class
│       │       │       ├── MarioCustomSystemOfValues.class
│       │       │       ├── MarioSystemOfValues$timeLengthMapping.class
│       │       │       ├── MarioSystemOfValues.class
│       │       │       ├── MultiDifficultyProgressTask.class
│       │       │       ├── MultiSeedProgressTask.class
│       │       │       ├── MushroomTask.class
│       │       │       ├── ProgressTask.class
│       │       │       ├── ReplayTask.class
│       │       │       ├── SystemOfValues.class
│       │       │       └── Task.class
│       │       ├── evolution
│       │       │   ├── ea
│       │       │   │   └── ES.class
│       │       │   ├── EA.class
│       │       │   ├── Evolvable.class
│       │       │   ├── FA.class
│       │       │   ├── MLP.class
│       │       │   └── SRN.class
│       │       ├── scenarios
│       │       │   ├── champ
│       │       │   │   ├── GamePlayTrack.class
│       │       │   │   ├── LearningTrack.class
│       │       │   │   └── TuringTestTrack.class
│       │       │   ├── Custom.class
│       │       │   ├── Main.class
│       │       │   ├── oldscenarios
│       │       │   │   ├── CompetitionScore.class
│       │       │   │   ├── Evolve.class
│       │       │   │   ├── EvolveIncrementally.class
│       │       │   │   ├── EvolveMultiSeed.class
│       │       │   │   ├── GeneralScenario.class
│       │       │   │   ├── MainRun.class
│       │       │   │   └── Stats.class
│       │       │   ├── Play.class
│       │       │   ├── Replay.class
│       │       │   └── test
│       │       │       ├── EvaluateJLink.class
│       │       │       ├── EvolveSingle.class
│       │       │       ├── EvolveWithChangingSeeds.class
│       │       │       ├── PaperEvolve.class
│       │       │       ├── PaperEvolveBatch.class
│       │       │       ├── PlayJLink.class
│       │       │       ├── StatsJLink.class
│       │       │       └── StochasticityTest.class
│       │       ├── tools
│       │       │   ├── amico
│       │       │   │   └── AmiCoJavaPy.class
│       │       │   ├── EvaluationInfo.class
│       │       │   ├── EvaluationInfoStatisticalSummary.class
│       │       │   ├── Evaluator.class
│       │       │   ├── GameViewer$1.class
│       │       │   ├── GameViewer$GameViewerActions.class
│       │       │   ├── GameViewer$GameViewerView.class
│       │       │   ├── GameViewer.class
│       │       │   ├── MarioAIOptions.class
│       │       │   ├── punj
│       │       │   │   └── PunctualJudge.class
│       │       │   ├── RandomCreatureGenerator.class
│       │       │   ├── ReplayerOptions$Interval.class
│       │       │   ├── ReplayerOptions.class
│       │       │   ├── Scale2x.class
│       │       │   ├── StateEncoderDecoder.class
│       │       │   ├── ToolsConfigurator$INTERFACE_TYPE.class
│       │       │   ├── ToolsConfigurator$ToolsConfiguratorActions.class
│       │       │   └── ToolsConfigurator.class
│       │       ├── unittests
│       │       │   ├── CmdLineOptionsTest.class
│       │       │   ├── LevelGeneratorTest.class
│       │       │   ├── LevelSceneTest.class
│       │       │   ├── MarioAIBenchmarkTest.class
│       │       │   └── MarioEnvironmentTest.class
│       │       └── utils
│       │           ├── ErrorCodes.class
│       │           ├── MathX.class
│       │           ├── ParameterContainer.class
│       │           ├── statistics
│       │           │   ├── StatisticalSummary$Watch.class
│       │           │   ├── StatisticalSummary.class
│       │           │   ├── StatisticalTests.class
│       │           │   └── Stats.class
│       │           └── wox
│       │               └── serial
│       │                   ├── AccessTest$Sub.class
│       │                   ├── AccessTest$Super.class
│       │                   ├── AccessTest.class
│       │                   ├── ArrayListTest.class
│       │                   ├── Easy.class
│       │                   ├── EasyTest.class
│       │                   ├── EncodeBase64.class
│       │                   ├── ObjectReader.class
│       │                   ├── ObjectWriter.class
│       │                   ├── ReadTest.class
│       │                   ├── Serial.class
│       │                   ├── ShadowTest$X.class
│       │                   ├── ShadowTest$Y.class
│       │                   ├── ShadowTest.class
│       │                   ├── SimpleReader.class
│       │                   ├── SimpleWriter.class
│       │                   ├── TestObject$Inner.class
│       │                   ├── TestObject.class
│       │                   ├── Util.class
│       │                   └── WriterTest.class
│       └── competition
│           ├── cig
│           │   └── sergeykarakovskiy
│           │       └── SergeyKarakovskiy_JumpingAgent.class
│           ├── evostar
│           │   └── sergeykarakovskiy
│           │       └── SergeyKarakovskiy_JumpingAgent.class
│           ├── gic2010
│           │   ├── gameplay
│           │   │   └── sergeykarakovskiy
│           │   │       └── SergeyKarakovskiy_ForwardAgent.class
│           │   ├── learning
│           │   │   └── sergeykarakovskiy
│           │   │       └── SergeyKarakovskiy_MLPAgent.class
│           │   └── turing
│           │       └── sergeykarakovskiy
│           │           └── SergeyKarakovskiy_ForwardAgent.class
│           └── wcci
│               └── NikolaySohryakov
│                   └── NikolaySohryakovAgent.class
├── lib
│   ├── asm-all-3.3.jar
│   ├── jdom.jar
│   └── junit-4.8.2.jar
├── LICENSE
├── MarioAI.zip
├── README.md
├── src
│   ├── amico
│   │   ├── cpp
│   │   ├── haskell
│   │   ├── mono
│   │   ├── ocaml
│   │   ├── pascal
│   │   ├── python
│   │   │   ├── agents
│   │   │   │   ├── DemoForwardAgent.py
│   │   │   │   ├── DemoForwardJumpingAgent.py
│   │   │   │   ├── evaluationinfo.py
│   │   │   │   ├── forwardagent.py
│   │   │   │   ├── forwardjumpingagent.py
│   │   │   │   └── marioagent.py
│   │   │   ├── JavaPy
│   │   │   │   ├── make.cmd
│   │   │   │   ├── Makefile
│   │   │   │   ├── Makefile.Darwin
│   │   │   │   ├── Makefile.Linux
│   │   │   │   ├── Makefile.Win
│   │   │   │   ├── run.cmd
│   │   │   │   ├── run.sh
│   │   │   │   └── src
│   │   │   │       ├── AmiCoJavaPy.def
│   │   │   │       ├── arrayutils.h
│   │   │   │       ├── ch_idsia_tools_amico_AmiCoJavaPy.cc
│   │   │   │       └── ch_idsia_tools_amico_AmiCoJavaPy.h
│   │   │   └── PyJava
│   │   │       ├── AmiCoRunner.sh
│   │   │       ├── make.cmd
│   │   │       ├── Makefile
│   │   │       ├── Makefile.Darwin
│   │   │       ├── Makefile.Linux
│   │   │       ├── Makefile.Win
│   │   │       ├── PythonCallsJava.obj
│   │   │       ├── run.cmd
│   │   │       ├── run.sh
│   │   │       └── src
│   │   │           ├── AmiCoPyJava.def
│   │   │           ├── arrayutils.h
│   │   │           ├── PythonCallsJava.cc
│   │   │           └── PythonCallsJava.h
│   │   └── scala
│   ├── ch
│   │   └── idsia
│   │       ├── agents
│   │       │   ├── Agent.java
│   │       │   ├── AgentLoader.java
│   │       │   ├── AgentsPool.java
│   │       │   ├── AmiCoAgent.java
│   │       │   ├── BasicLearningAgent.java
│   │       │   ├── controllers
│   │       │   │   ├── BasicMarioAIAgent.java
│   │       │   │   ├── ForwardAgent.java
│   │       │   │   ├── forwardagent.py
│   │       │   │   ├── ForwardJumpingAgent.java
│   │       │   │   ├── human
│   │       │   │   │   ├── CheaterKeyboardAgent.java
│   │       │   │   │   └── HumanKeyboardAgent.java
│   │       │   │   ├── marioagent.py
│   │       │   │   ├── RandomAgent.java
│   │       │   │   ├── ReplayAgent.java
│   │       │   │   ├── ScaredAgent.java
│   │       │   │   ├── ScaredShooty.java
│   │       │   │   └── TimingAgent.java
│   │       │   ├── learning
│   │       │   │   ├── LargeMLPAgent.java
│   │       │   │   ├── LargeSRNAgent.java
│   │       │   │   ├── MediumMLPAgent.java
│   │       │   │   ├── MediumSRNAgent.java
│   │       │   │   ├── SimpleMLPAgent.java
│   │       │   │   ├── SmallMLPAgent.java
│   │       │   │   ├── SmallSRNAgent.java
│   │       │   │   └── SRNAgent.java
│   │       │   ├── LearningAgent.java
│   │       │   ├── MLPESLearningAgent.java
│   │       │   ├── SimpleAgent.java
│   │       │   ├── simplepythonagent.py
│   │       │   └── SRNESLearningAgent.java
│   │       ├── benchmark
│   │       │   ├── experiments
│   │       │   │   ├── EpisodicExperiment.java
│   │       │   │   └── Experiment.java
│   │       │   ├── mario
│   │       │   │   ├── engine
│   │       │   │   │   ├── Art.java
│   │       │   │   │   ├── BgRenderer.java
│   │       │   │   │   ├── GeneralizerEnemies.java
│   │       │   │   │   ├── GeneralizerLevelScene.java
│   │       │   │   │   ├── GlobalOptions.java
│   │       │   │   │   ├── level
│   │       │   │   │   │   ├── BgLevelGenerator.java
│   │       │   │   │   │   ├── ImprovedNoise.java
│   │       │   │   │   │   ├── Level.java
│   │       │   │   │   │   ├── LevelGenerator.java
│   │       │   │   │   │   └── SpriteTemplate.java
│   │       │   │   │   ├── LevelRenderer.java
│   │       │   │   │   ├── LevelScene.java
│   │       │   │   │   ├── mapedit
│   │       │   │   │   │   ├── LevelEditor.java
│   │       │   │   │   │   ├── LevelEditView.java
│   │       │   │   │   │   └── TilePicker.java
│   │       │   │   │   ├── MarioVisualComponent.java
│   │       │   │   │   ├── Recorder.java
│   │       │   │   │   ├── Replayer.java
│   │       │   │   │   ├── resources
│   │       │   │   │   │   ├── bgsheet.png
│   │       │   │   │   │   ├── endscene.gif
│   │       │   │   │   │   ├── enemysheet.png
│   │       │   │   │   │   ├── firemariosheet.png
│   │       │   │   │   │   ├── font.gif
│   │       │   │   │   │   ├── itemsheet.png
│   │       │   │   │   │   ├── logo.gif
│   │       │   │   │   │   ├── mapsheet.png
│   │       │   │   │   │   ├── mariosheet.png
│   │       │   │   │   │   ├── particlesheet.png
│   │       │   │   │   │   ├── princess.png
│   │       │   │   │   │   ├── racoonmariosheet.png
│   │       │   │   │   │   ├── smallmariosheet.png
│   │       │   │   │   │   ├── test.lvl
│   │       │   │   │   │   ├── tiles.dat
│   │       │   │   │   │   └── worldmap.png
│   │       │   │   │   └── sprites
│   │       │   │   │       ├── BulletBill.java
│   │       │   │   │       ├── CoinAnim.java
│   │       │   │   │       ├── Enemy.java
│   │       │   │   │       ├── Fireball.java
│   │       │   │   │       ├── FireFlower.java
│   │       │   │   │       ├── FlowerEnemy.java
│   │       │   │   │       ├── GreenMushroom.java
│   │       │   │   │       ├── Mario.java
│   │       │   │   │       ├── Mushroom.java
│   │       │   │   │       ├── Particle.java
│   │       │   │   │       ├── Princess.java
│   │       │   │   │       ├── Shell.java
│   │       │   │   │       ├── Sparkle.java
│   │       │   │   │       ├── Sprite.java
│   │       │   │   │       ├── SpriteContext.java
│   │       │   │   │       └── WaveGoomba.java
│   │       │   │   ├── environments
│   │       │   │   │   ├── Environment.java
│   │       │   │   │   └── MarioEnvironment.java
│   │       │   │   └── simulation
│   │       │   │       ├── AmiCoSimulator.java
│   │       │   │       └── SimulationOptions.java
│   │       │   └── tasks
│   │       │       ├── BasicTask.java
│   │       │       ├── GamePlayTask.java
│   │       │       ├── LearningTask.java
│   │       │       ├── MarioCustomSystemOfValues.java
│   │       │       ├── MarioSystemOfValues.java
│   │       │       ├── MultiDifficultyProgressTask.java
│   │       │       ├── MultiSeedProgressTask.java
│   │       │       ├── MushroomTask.java
│   │       │       ├── ProgressTask.java
│   │       │       ├── ReplayTask.java
│   │       │       ├── SystemOfValues.java
│   │       │       └── Task.java
│   │       ├── evolution
│   │       │   ├── ea
│   │       │   │   └── ES.java
│   │       │   ├── EA.java
│   │       │   ├── Evolvable.java
│   │       │   ├── FA.java
│   │       │   ├── MLP.java
│   │       │   └── SRN.java
│   │       ├── scenarios
│   │       │   ├── champ
│   │       │   │   ├── GamePlayTrack.java
│   │       │   │   ├── LearningTrack.java
│   │       │   │   └── TuringTestTrack.java
│   │       │   ├── Custom.java
│   │       │   ├── Main.java
│   │       │   ├── oldscenarios
│   │       │   │   ├── CompetitionScore.java
│   │       │   │   ├── Evolve.java
│   │       │   │   ├── EvolveIncrementally.java
│   │       │   │   ├── EvolveMultiSeed.java
│   │       │   │   ├── GeneralScenario.java
│   │       │   │   ├── MainRun.java
│   │       │   │   └── Stats.java
│   │       │   ├── Play.java
│   │       │   ├── Replay.java
│   │       │   └── test
│   │       │       ├── EvaluateJLink.java
│   │       │       ├── EvolveSingle.java
│   │       │       ├── EvolveWithChangingSeeds.java
│   │       │       ├── PaperEvolve.java
│   │       │       ├── PaperEvolveBatch.java
│   │       │       ├── PlayJLink.java
│   │       │       ├── StatsJLink.java
│   │       │       └── StochasticityTest.java
│   │       ├── tools
│   │       │   ├── amico
│   │       │   │   └── AmiCoJavaPy.java
│   │       │   ├── EvaluationInfo.java
│   │       │   ├── EvaluationInfoStatisticalSummary.java
│   │       │   ├── Evaluator.java
│   │       │   ├── GameViewer.java
│   │       │   ├── MarioAIOptions.java
│   │       │   ├── punj
│   │       │   │   └── PunctualJudge.java
│   │       │   ├── RandomCreatureGenerator.java
│   │       │   ├── ReplayerOptions.java
│   │       │   ├── Scale2x.java
│   │       │   ├── StateEncoderDecoder.java
│   │       │   └── ToolsConfigurator.java
│   │       ├── unittests
│   │       │   ├── CmdLineOptionsTest.java
│   │       │   ├── LevelGeneratorTest.java
│   │       │   ├── LevelSceneTest.java
│   │       │   ├── MarioAIBenchmarkTest.java
│   │       │   └── MarioEnvironmentTest.java
│   │       └── utils
│   │           ├── ErrorCodes.java
│   │           ├── MathX.java
│   │           ├── ParameterContainer.java
│   │           ├── statistics
│   │           │   ├── StatisticalSummary.java
│   │           │   ├── StatisticalTests.java
│   │           │   └── Stats.java
│   │           └── wox
│   │               └── serial
│   │                   ├── AccessTest.java
│   │                   ├── ArrayListTest.java
│   │                   ├── Easy.java
│   │                   ├── EasyTest.java
│   │                   ├── EncodeBase64.java
│   │                   ├── ObjectReader.java
│   │                   ├── ObjectWriter.java
│   │                   ├── ReadTest.java
│   │                   ├── Serial.java
│   │                   ├── ShadowTest.java
│   │                   ├── SimpleReader.java
│   │                   ├── SimpleWriter.java
│   │                   ├── TestObject.java
│   │                   ├── Util.java
│   │                   └── WriterTest.java
│   └── competition
│       ├── cig
│       │   └── sergeykarakovskiy
│       │       └── SergeyKarakovskiy_JumpingAgent.java
│       ├── evostar
│       │   └── sergeykarakovskiy
│       │       └── SergeyKarakovskiy_JumpingAgent.java
│       ├── gic2010
│       │   ├── gameplay
│       │   │   └── sergeykarakovskiy
│       │   │       └── SergeyKarakovskiy_ForwardAgent.java
│       │   ├── learning
│       │   │   └── sergeykarakovskiy
│       │   │       └── SergeyKarakovskiy_MLPAgent.java
│       │   └── turing
│       │       └── sergeykarakovskiy
│       │           └── SergeyKarakovskiy_ForwardAgent.java
│       └── wcci
│           └── NikolaySohryakov
│               └── NikolaySohryakovAgent.java
└── target
    └── scripts
        ├── catResults.sh
        ├── game-play-track-evaluation.sh
        ├── learning-track-evaluation.sh
        ├── runClient.sh
        ├── runExperiments.sh
        ├── runServer.sh
        └── turing-test-track-evaluation.sh

141 directories, 584 files
```


## Structure Analysis
 - There are 3 `ch.idsia.scenarios.Main` files.
     1. `bin/AmiCo/Buil/PyJava/ch/idsia/scenarios/Main.class`
     2. `bin/MarioAI/ch/idsia/scenarios/Main.class`
     3. `src/ch/idsia/scenarios/Main.java`
 - There is no `CustomRun` file.
 - There are 2 `Play` files.


## Structural Additions
```bash
.
└── src
    └── peter
        ├── Nodes
        |   ├── Node.java
        |   ├── Composite.java
        |   ├── Sequence.java
        |   ├── Selector.java
        |   ├── RandomSelector.java
        |   ├── RandomSequence.java
        |   ├── Action.java
        |   └── Condition.java
        ├── Trees
        |   ├── Tree.java
        |   ├── Kill.java
        |   ├── Jump.java
        |   ├── Score.java
        |   └── Combo.java
        └── Agents
            ├── BTAgent.java
            └── MarioBTAgent.java
```


## Structural Additions Annotated
```bash
.
└── src
    └── peter
        ├── Tasks
        |   ├── Task.java               // Abstract -- Has Parent, Children, Effect, Status
        |   ├── Composite.java          // Abstract -- Has 
        |   ├── Sequence.java           // Do These Things in Order
        |   ├── Selector.java           // Pick One of These
        |   ├── RandomSelector.java     // Randomly Select
        |   ├── RandomSequence.java     // Randomly Order
        |   ├── Action.java             // Do a thing to the external environment
        |   └── Question.java           // Get a thing from the external environment
        ├── Trees
        |   ├── Tree.java               // Abstract - Has Root, Meta
        |   ├── Kill.java               // Emphasizes killing as many enemies as possible
        |   ├── Jump.java               // Emphasizes doing every jump correctly
        |   ├── Coins.java              // Emphasizes collecting as many coins as possible
        |   └── Combo.java              // Combines all of the Trees into a Mega Tree 
        ├── Agents
        |   ├── BTAgent.java            // Interface -- Has Tree, Update, Query
        |   └── MarioBTAgent.java       // Uses Regular Mario Agent and BT Functionality
        └── Tests
            ├── TestTask.java
            ├── TestTree.java           // Emphasizes getting the tree to work
```
















