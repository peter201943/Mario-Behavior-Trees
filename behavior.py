

# A Test in Dynamic Design
# (In Python because Java hurts my head)


class Task():
    """Performs a Computation every Cycle"""
    def __init__(self):
        """Calls Reset"""
        self.Reset()
    def Run(self):
        """The Computation"""
        print("4: Task")
        self.status = "running"
        self.clock += 1
        self.log += "Run " + str(self.clock) + ", " + self.__str__() + "\n"
        return self.status
    def __str__(self):
        """Gather Debug Info together"""
        return self.name + ": "  + "None " + " status: " + self.status
    def Log(self):
        """Debug the Progress of the Task"""
        return self.log
    def Reset(self):
        """Resets the Task"""
        self.status = "running"
        self.clock = 0
        self.name = "Task"
        self.log = self.name + "\n"
    def Name(self):
        return self.name


class Find(Task):
    """Finds Things every Cycle"""
    def __init__(self, newTargets, newTarget):
        """Calls Reset"""
        self.Reset(newTargets, newTarget)
    def Run(self):
        """The Computation"""
        print("4: FindTask")
        self.clock += 1
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
        return self.name + ": " + self.target + " in " + self.Targets() + " has found " + self.Found() + " status: " + self.status
    def Log(self):
        """Debug the Progress of the Task"""
        return self.log
    def Reset(self, newTargets, newTarget):
        """Resets the Task"""
        self.found = []
        self.targets = newTargets
        self.target = newTarget
        self.status = "running"
        self.clock = 0
        self.name = "Find"
        self.log = self.name + "\n"
    def Name(self):
        return self.name


class Container(Task):
    """Finds Children every Cycle"""
    def __init__(self):
        """Calls Reset"""
        self.Reset()
    def Run(self):
        """The Computation"""
        print("4: ContainerTask")
        self.clock += 1
        self.log += "Run " + str(self.clock) + ", " + self.__str__() + "\n"
        return self.status
    def __str__(self):
        """Gather Debug Info together"""
        return self.name + ": " +  " children: " + str(self.childnames) +  " status: " + self.status
    def Log(self):
        """Debug the Progress of the Task"""
        return self.log
    def Reset(self):
        """Resets the Task"""
        self.status = "running"
        self.clock = 0
        self.children = []
        self.name = "Container"
        self.childnames = []
        self.log = self.name + "\n"
    def Children(self):
        """Access the Child Tasks"""
        return self.children
    def Add(self, task):
        self.children.append(task)
        self.childnames.append(task.Name())
    def Remove(self, task):
        if task in self.children:
            self.children.remove(task)
            self.childnames.remove(task.Name())
    def Name(self):
        return self.name


def Game(tasks, clock):
    """Runs the Tasks within the confines of an Environment"""
    print("\n3: game (" + str(clock) + ")")
    for task in tasks:
        task.Run()
    if (clock < 10):
        Game(tasks, (clock + 1))
    else:
        print()
        for task in tasks:
            print(task.Log())


def Setup():
    """Sets the Game Up"""
    print("2: setup")
    tree = []
    myTask = Task()
    tree.append(myTask)
    myFind = Find(['a','b','a','a','b','b','b','b','a'], 'a')
    tree.append(myFind)
    myFind2 = Find(['b','b','b','b','b'], 'a')
    tree.append(myFind2)
    myContainer = Container()
    myContainer.Add(myFind)
    myContainer.Add(myFind2)
    tree.append(myContainer)
    return tree


def main():
    """Entry Point to Program"""
    print("1: main")
    Game(Setup(), 0)


if (__name__ == "__main__"):
    print("0: program")
    main()

