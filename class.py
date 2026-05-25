from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("passed value: ", x )
    @abstractmethod
    def task(self):
        print("this text is in the abs class")
class classclass(Absclass):
    def task(self):
        print("this text is in the child's child class")
obj = classclass()
obj.task()
obj.print(100)