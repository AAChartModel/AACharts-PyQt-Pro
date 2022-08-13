from ast import Str, parse
import csv


class AAData:
    csv: str
    parsed: str

    def csvSet(self, prop: str):
        self.csv = prop
        return self

    def parsedSet(self, prop: str):
        self.parsed = prop
        return self 
        