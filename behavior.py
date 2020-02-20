

# A Test in Dynamic Design
# (In Python because Java hurts my head)


class Task():
    """Performs a Computation every Cycle"""
    def __init__(self, newTargets, newTarget):
        """Calls Reset"""
        self.Reset(newTargets, newTarget)
    def Run(self):
        """The Computation"""
        print("4: task")
        if (len(self.targets) > 0):
            if (self.targets[0] == self.target):
                self.found += self.targets[0]
            self.targets.pop(0)
            self.status = "running"
        elif (len(self.found) > 0):
            self.status = "success"
        else:
            self.status = "failed"
        self.log += "Run " + str(self.clock) + ", " + self.__str__() + "\n"
        return self.status
    def Found(self):
        """The Results of the Compuation"""
        return str(self.found)
    def Targets(self):
        """Remaining Data to Compute"""
        return str(self.targets)
    def __str__(self):
        """Gather Debug Info together"""
        return "Task: Find " + self.target + " in " + self.Targets() + " has found " + self.Found() + " status: " + self.status
    def Log(self):
        """Debug the Progress of the Task"""
        return self.log
    def Reset(self, newTargets, newTarget):
        """Resets the Task"""
        self.found = []
        self.targets = newTargets
        self.target = newTarget
        self.status = "running"
        self.log = ""
        self.clock = 0


def Game(tasks, clock):
    """Runs the Tasks within the confines of an Environment"""
    print("3: game")
    for task in tasks:
        task.Run()
    if (clock < 10):
        Game(tasks, (clock + 1))
    else:
        for task in tasks:
            print(task.Log())


def Setup():
    """Sets the Game Up"""
    print("2: setup")
    tree = []
    myTask = Task(['a','b','a','a','b','b','b','b','a'], 'a')
    tree.append(myTask)
    myTask2 = Task(['b','b','b','b','b'], 'a')
    tree.append(myTask2)
    return tree


def main():
    """Entry Point to Program"""
    print("1: main")
    Game(Setup(), 0)


if (__name__ == "__main__"):
    print("0: program")
    main()

