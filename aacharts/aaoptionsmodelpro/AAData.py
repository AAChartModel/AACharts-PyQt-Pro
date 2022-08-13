from ast import Str, parse
import csv

from aacharts.aatool.AAStringPurer import AAStringPurer


class AAData:
    csv: str
    parsed: str

    def csvSet(self, prop: str):
        self.csv = prop
        return self

    def parsedSet(self, prop: str):
        self.parsed = AAStringPurer.pureJSString(prop)
        return self 
        