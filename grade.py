from student import Student


class Grade(Student):
    def __init__(self, mmw, arts, history, math) -> None:
        self.science = mmw
        self.math = math
        self.english = history
        self.filipino = arts

    def getAverage(self):
        return (int(self.mmw) + int(self.math) + int(self.arts) + int(self.history))/4