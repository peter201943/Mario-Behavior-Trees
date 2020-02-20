

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


### ???
 - Got all these damn notes done
 - Did a crud-ton of reading
 - Now to get the damn thing to run



---------



































