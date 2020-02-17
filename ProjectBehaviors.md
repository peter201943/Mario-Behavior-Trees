


## CS 387: Game AI

[Introduction](Intro.md) | [Schedule](Schedule.md) | [Projects](Projects.md)



# Scripting in Super Mario

The goal of Project 3 is to learn how to use `Behavior Trees`, which are very commonly used in computer games for defining the behavior of characters and groups of characters.  

In this project you will work with the a Java version of Super Mario that you can download from [here](../Projects/HW%203/MarioAI.zip).  

This version is played on randomly generated maps, so you have a practically infinite number of different levels to play or test your AI. Follow the instructions from the link above to configure the code in your favorite Java IDE. If you run the `ch.idsia.scenarios.Main` class directly, you can play the game by hand by controlling Mario using the keyboard (`arrow key`s, `a`, `s`), if the screen is too small, press `z` to zoom in.  

For the purposes of this class, we are not interested in finding the optimal behavior, but with authoring an acceptable behavior for Mario. As you will see, the game comes with several controllers already defined (like the `ForwardJumpingAgent.java` one that simply moves to the right and jumps constantly (with which you can surprisingly complete some easy levels!). You can use them as an example of how to interface your controller with the game.  

Try to create, using `Behavior Trees`, a controller for Mario that tries to collect as many coins as possible, and kill as many enemies as possible. Do not code a fast forward controller that simply advances and jumps. In case enemies are too hard to kill (e.g. flying enemies, or enemies that are in a hard to reach place), it is ok if you controller skips them (same for coins).  

As you will discover, `Behavior Trees` are not the best idea for this kind of game. But precisely for that reason I've chosen it. The goal of this project is for you to explore the possibilities of BTs and their limits. Discover what is easy and what is hard to do with BTs.  

You are free to use any `Behavior Tree` library you can find online. But I strongly recommend implementing everything from scratch, since that will be much faster and easier for you. BTs are VERY easy to implement, and in the time you take to locate and learn a library, you can already have your own version implemented.  


## Specific Project Tasks:
 - Download the Super Mario source code from [here](../Projects/HW%203/MarioAI.zip).
 - Set the Super Mario in your favorite Java IDE (Netbeans, Eclipse, etc.)
 - To test that you have it properly setup, you can try to run the file `ch.idsia.scenarios.Main`. If you see Super Mario launching and you can control it with the arrow keys, you are good.
 - Read the documentation at the bottom of this page to familiarize yourself with the code. But maybe the easiest way is just to look at example controllers (that can be found in the package `controllers`). In this project you will just have to create a new class that extends the `BasicMarioAIAgent` class.
 - Implement a controller that uses `Behavior Trees` (as explained in class) for controlling Mario to collect as many coins, and to kill as many enemies as possible.
 - Create a short 3 minute video demoing your project, and send it to the instructor (do not send the video file! please just send a link (e.g., DropBox link, Youtube link, etc.). You will have to present this video in class.
 - Turn in the source-code of your project, plus a 1-2 page description of what you did before midnight the due date. Submissions will be done via Blackboard.


## Notes:
 - The goal of the project is to learn how to use `Behavior Trees`, not to create the best Mario AI. If you create a very good Mario AI that doesn't use `Behavior Trees`, I will be very impressed but it will NOT count towards your grade.
 - In the description of your project, please tell me where in the project I can find the code you added.


## [Documentation](https://code.google.com/archive/p/marioai/wikis/GettingStarted.wiki)

### Introduction

Checkout from [SVN](http://code.google.com/p/marioai/source/checkout) Source or download a [zip](http://www.marioai.com/marioai-benchmark/download/MarioAI.zip) package.  

`ch.idsia.scenarios.CustomRun` - the simplest run. Its main method consists of three lines. Update your Run Configuration and run in your IDE or run this (after the compilation) as java `ch.idsia.scenarios.CustomRun`. You'll see in the top left corner the main View of the benchmark with a waiting for your commands Mario.  
Available actions are:
 - Arrow Keys: `←` - left, `↓` - ?, `→` - right
 - Buttons: `s` - jump, `a` - speed, `fire` - shoot.

### Details

Look for the specific project files in trunk. Project files for IntelliJ IDEA, Eclipse Galileo and Netbeans are provided. Or you might also checkout from SVN using the above mentioned IDEs. Use SVN version 1.6 everywhere.  

For more information run and have a look at `ch.idsia.scenarios.Play` class. After that you're ready to come up with `MainRun`.  

### IntelliJ IDEA
 1. Version Control
 2. Checkout from Version Control.
 3. Subversion.
 4. http://marioai.googlecode.com/svn/trunk/ or http://marioai.googlecode.com/svn/ if you would like to checkout the entire project with branches, documentation and target folder, etc.
 5. Create a project from source in _Your\_Just\_Created\_Folder_? Yes
 6. **Next>**(if you satisfied with suggested project name and path; otherwise, change it!)
 7. Mark All if you want IDEA to recognize all java files in source directories.
 8. **Next>**1. Mark `jdom.jar` and press**Next>**1. Select _Trunk_ or _Src_ in**Modules**column. In the right column**Module Dependencies**you should see `jdom.jar`
 9. **Next >**1. Exclude if any facets in Python src found
 10. **Finish**!
 11. Go to**Preferences**>**Compiler**1. Add here `;*.lvl;*.dat` (this makes IDEA to copy these files within the compiled binary class-files; so the IDE could find it while running)
 12. **OK

### Eclipse Galileo for Python parts of the project only
 1. File -> New -> Other
 2. SVN -> Checkout projects from SVN
 3. Create a new repository location http://marioai.googlecode.com/svn/trunk
 4. **Next >**1. src -> python -> competition
 5. **Next >**1. Select "Check out as a project configured using the New Project Wizard"
 6. **Next >**(You will see a project creation wizard)
 7. _Pydev_ -> _Pydev_ Project ([Pydev](http://pydev.org) plugin for Eclipse should be installed)
 8. Give name to a project, say "MarioAICompetition"
 9. uncheck "Create default 'src'..."
 10. **Finish

### Eclipse Galileo for Java part and entire source
 1. File -> New -> Other
 2. SVN -> Checkout projects from SVN
 3. Create a new repository location http://marioai.googlecode.com/svn/trunk or use the existing one
 4. **Next >**1. Select "Check out as a project configured using the New Project Wizard"
 5. **Next >**(You will see a project creation wizard)
 6. Select "_Java_ _Project_"
 7. Name the project, say "MarioAI" and select a location
 8. Make root folder as source folder
 9. Configure inclusion and exclusion filters
 10. Press**Add**and put down '**.lvl', '**.dat'
 11. **Finish

### Netbeans IDE

*Please, let  us know, if one need instructions for Netbeans (which are basically similar to the aboves)*  

Once your project had been set up, you can go to Overview, run the becnhmark, Play and start programming your Agent!  


---------


From: https://www.cs.drexel.edu/~eb452/teaching/CS387-w20/projectMario.html


