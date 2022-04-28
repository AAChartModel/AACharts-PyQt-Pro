
from aacharts.aaenum.AAEnum import AAChartAlignType, AAChartVerticalAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle
from aacharts.aatool.AAStringPurer import AAStringPurer

class AAFilter:
    property: str
    operator: str
    value: float
    
    def propertySet(self, prop: str):
        self.property = prop
        return self
    
    def operatorSet(self, prop: str):
        self.operator = prop
        return self
    
    def valueSet(self, prop: float):
        self.value = prop
        return self


class AATextPath: 
    enabled: bool
    attributes: map
    value: float
    
    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self
    
    def attributesSet(self, prop: map):
        self.attributes = prop
        return self



class AADataLabels:
    enabled: bool = True
    align: str
    style: AAStyle
    format: str
    formatter: str
    rotation: float
    allowOverlap: bool
    useHTML: bool
    distance: str
    verticalAlign: str
    x: float
    y: float
    color: str
    backgroundColor: str
    borderColor: str
    borderRadius: float
    borderWidth: float
    shape: str
    crop: bool
    inside: bool
    overflow: str
    softConnector: bool
    connectorColor: str
    connectorPadding: float
    connectorShape: str
    connectorWidth: float
    crookDistance: str
    alignTo: str

    filter: AAFilter
    textPath: AATextPath
    linkTextPath: AATextPath
    padding: float #When either the borderWidth or the backgroundColor is set, this is the padding within the box. Defaults to 5.
    nodeFormat: str #The format string specifying what to show for nodes in the sankey diagram. By default the nodeFormatter returns {point.name}. Defaults to undefined.


    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self
   
    
    def alignSet(self, prop: AAChartAlignType):
        self.align = prop.value
        return self
   
    
    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self
   
    
    def formatSet(self, prop: str):
        self.format = prop
        return self
   
    
    def formatterSet(self, prop: str):
        if (prop != None):
             self.formatter = AAStringPurer.pureJSString(prop)
        return self
   
    
    def rotationSet(self, prop: float):
        self.rotation = prop
        return self
   
    
    def allowOverlapSet(self, prop: bool):
        self.allowOverlap = prop
        return self
   
    
    def useHTMLSet(self, prop: bool):
        self.useHTML = prop
        return self
   
    
    def distanceSet(self, prop: str):
        self.distance = prop
        return self
   
    
    def verticalAlignSet(self, prop: AAChartVerticalAlignType):
        self.verticalAlign = prop.value
        return self
   
    
    def xSet(self, prop: float):
        self.x = prop
        return self
   
    
    def ySet(self, prop: float):
        self.y = prop
        return self
   
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
   
    
    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self
   
    
    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self
   
    
    def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self
   
    
    def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
   
    
    def shapeSet(self, prop: str):
        self.shape = prop
        return self
   
    
    def cropSet(self, prop: bool):
        self.crop = prop
        return self
   
    
    def insideSet(self, prop: bool):
        self.inside = prop
        return self
   
    
    def overflowSet(self, prop: str):
        self.overflow = prop
        return self
    
    def softConnectorSet(self, prop: bool):
        self.softConnector = prop
        return self
    
    def connectorColorSet(self, prop: str):
        self.connectorColor = prop
        return self
   
    
    def connectorPaddingSet(self, prop: float):
        self.connectorPadding = prop
        return self
   
    
    def connectorShapeSet(self, prop: str):
        self.connectorShape = prop
        return self
   
    
    def connectorWidthSet(self, prop: float):
        self.connectorWidth = prop
        return self
   
    
    def crookDistanceSet(self, prop: str):
        self.crookDistance = prop
        return self
   
    
    def alignToSet(self, prop: str):
        self.alignTo = prop
        return self

    def filterSet(self, prop: AAFilter):
        self.filter = prop
        return self

    def textPathSet(self, prop: map):
        self.textPath = prop
        return self

    def linkTextPathSet(self, prop: AATextPath):
        self.linkTextPath = prop
        return self

    def paddingSet(self, prop: float):
        self.padding = prop
        return self

    def nodeFormatSet(self, prop: str):
        self.nodeFormat = prop
        return self
  
 

 