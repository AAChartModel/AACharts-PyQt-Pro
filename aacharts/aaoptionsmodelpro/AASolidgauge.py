from aacharts.aaoptionsmodel.AADataLabels import AADataLabels


class AASolidgauge:

    dataLabels: AADataLabels
    linecap: str
    stickyTracking: bool
    rounded: bool

    def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self

    def linecapSet(self, prop: str):
        self.linecap = prop
        return self

    def stickyTrackingSet(self, prop: bool):
        self.stickyTracking = prop
        return self

    def roundedSet(self, prop: bool):
        self.rounded = prop
        return self

    
