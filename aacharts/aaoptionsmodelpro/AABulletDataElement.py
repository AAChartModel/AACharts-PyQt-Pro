from ast import Num


class AABulletDataElement:
    y: Num
    target: Num

    def ySet(self, prop: Num):
        self.y = prop
        return self

    def targetSet(self, prop: Num):
        self.target = prop
        return self
        
         