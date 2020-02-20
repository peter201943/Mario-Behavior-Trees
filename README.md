

## CS 387: Game AI


---------


# README


## About
 - **Project**
     - HW3: Mario Behavior Trees
 - **Student**
     - Peter J. Mangelsdorf
     - pjm349@drexel.edu
     - 717-385-7068
 - **Professor**
     - Ehsan Khosroshahi
     - eb452@drexel.edu
 - **Contents**
     - [About](#about)
     - [Links](#links)
     - [Structural Additions](#structural-additions)
     - [Progress](#progress)


## Links
 - [README](README.md) -- Pertains to anything I _directly_ did
 - [Notes](Notes.md) -- Pertains to my understanding and development of the project


---------


## Structural Additions
```bash
.
└── src
    └── peter
        ├── AbstractTasks
        │   ├── Task.java               // Abstract -- Has Parent, Children, Effect, Status
        │   ├── Composite.java          // Abstract -- Has 
        │   ├── Sequence.java           // Abstract -- Do These Things in Order
        │   ├── Selector.java           // Abstract -- Pick One of These
        │   ├── RandomSelector.java     // Randomly Select
        │   ├── RandomSequence.java     // Randomly Order
        │   ├── Loop.java               // Calls itself and its children
        │   ├── Action.java             // Do a thing to the external environment
        │   └── Condition.java          // Get a thing from the external environment
        ├── MarioTasks
        │   ├── MoveFlat.java           // Move to a Point on Ground
        │   ├── MoveDown.java           // Move to a Point Below
        │   ├── MoveUp.java             // Move to a Point Above
        │   ├── EnemyInRange.java       // Can we step/jump on an enemy?
        │   ├── Survive.java            // Choose which sub behavior to pursue
        │   ├── Win.java                // Move right
        │   ├── Score.java              // Get Coins
        │   └── AttackJump.java         // Jump on Enemy
        ├── Trees
        │   ├── Tree.java               // Abstract - Has Root, Meta
        │   ├── Killing.java            // Emphasizes killing as many enemies as possible
        │   ├── Agility.java            // Emphasizes doing every jump correctly
        │   ├── Coins.java              // Emphasizes collecting as many coins as possible
        │   └── Combo.java              // Combines all of the Trees into a Mega Tree 
        ├── Agents
        │   ├── BTAgent.java            // Interface -- Has Tree, Update, Query
        │   └── MarioBTAgent.java       // Abstract -- Uses Regular Mario Agent and BT Functionality
        └── Tests
            ├── TestTask.java           // 
            ├── TestTree.java           // 
            └── TestAgent.java          // 
```


---------


## Progress


### Chapter 1: Getting this to Work
 - Got all these damn notes done
 - Did a crud-ton of reading
 - Now to get the damn thing to run
 - Nothing works
 - IntelliJ just deleted EVERYTHING I did
 - Using a different editor now
 - [Running and Debugging Java](https://code.visualstudio.com/docs/java/java-debugging)
 - Which JDK to Install?
     - `1.8` - compatibility
     - `11` - another class
     - `13` - latest edition
 - Installing all Java Related files into: `C:\Program Files\Java`
 - Something about the `.jar` files is wrong
 - Run this File: `src/ch/idsia/scenarios/Custom.java`
 - Oh great. I'm getting exactly _612_ errors. _WHY_.
     - Apparently `jdom` is needed: http://jdom.org/
     - And `testng` and a billion other things.
     - What is this `org` namespace?!?!?
     - Nevermind, I'm gonna regex and delete any references of it
     - No time for this nonsense
 - https://github.com/redhat-developer/vscode-java/issues/346
 - https://stackoverflow.com/questions/50232557/visual-studio-code-java-extension-howto-add-jar-to-classpath
 - https://github.com/leonardost/kifu-recorder-tests/commit/c09792b08e9a0e44ad1d4f0ccad8d55d8af0084a
 - And now I also need a _proper_ build system in order to load the `.jar`'s properly. _uuuggghhhhhh_
     - https://maven.apache.org/download.cgi
 - FINALLY!
 - Ughhh. Great, down from `618` bugs to _only_ `371`.
 - Seems related to `testng`. Was NOT included as a library.
 - Strat 1: Delete _ALL_ references to `testng`.
 - Offending Files:
     - `CmdLineOptionsTest.java`
     - `LevelGeneratorTest.java`
     - `LevelSceneTest.java`
     - `MarioAIBenchmarkTest.java`
     - `MarioEnvironmentTest.java`
 - Commenting failed. There are more conflicts than just `testng`
 - Add `gradle` to properly specify dependencies
 - Gradle installed, maven not working
 - https://stackoverflow.com/questions/18487406/how-do-i-tell-gradle-to-use-specific-jdk-version#21212790
 - Now to set the freaking compatibility for this thing
 - https://stackoverflow.com/questions/11364761/how-do-i-compile-a-java-with-support-for-older-versions-of-java
 - I have no idea how to do any of this
 - How about we just DELETE these classes:
     - AccessTest.java
     - Util.java
 - No, can't. Can't even tell how many files may or may not use these.
     - attempting to `grep` for usages of `AccessTest`, this will take a long time (584 files)
         - No results (too many files)
 - Plan B? D? Z? (How many of these stupid attempts at compatibility have borne no fruit?)
 - Download and attempt it in Eclipse
     - Wow.
     - It. Just. Works...
     - I hate everything, and most of all, Java.


### Chapter 2: Hiring an Agent
 - Potential Agents to Hire:
     - `C:\Users\Standard Access\Peter\School\College\3 - Junior\CS 387\Projects\HW 3\src\competition\gic2010\turing\sergeykarakovskiy\SergeyKarakovskiy_ForwardAgent.java`
     - `C:\Users\Standard Access\Peter\School\College\3 - Junior\CS 387\Projects\HW 3\src\competition\gic2010\gameplay\sergeykarakovskiy\SergeyKarakovskiy_ForwardAgent.java`
     - `C:\Users\Standard Access\Peter\School\College\3 - Junior\CS 387\Projects\HW 3\src\ch\idsia\agents\controllers\ForwardAgent.java`
 - Plan:
     - Study `ForwardAgent.java`
     - Redesign `ForwardAgent` in terms of Behavior Trees
     - Implement only the required Behavior Trees
     - Test this new framework/agent


### Chapter 3: Adding our First Task
 - I'm gonna cry, I haven't even touched this yet.
 - The game just WONT COMPILE


---------


