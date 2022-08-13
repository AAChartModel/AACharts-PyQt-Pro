from ast import Num


class AAParallelAxes:
    lineWidth: Num

    def lineWidthSet(self, prop: Num):
        self.lineWidth = prop
        return self
        