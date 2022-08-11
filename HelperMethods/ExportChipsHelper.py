import pandas as pd
import ee
from pathlib import Path
from py_linq import Enumerable

def createFineGrid(gridElement):
    grid = gridElement.geometry().coveringGrid(proj=gridElement.geometry().projection(), scale=32*500)

    return grid.map(lambda subGridElement:subGridElement\
        .set('within', subGridElement.centroid(maxError=1).containedIn(gridElement.geometry())))\
        .filter(ee.Filter.eq('within', True))

def getFileList(folder):
    Path.lsTif = lambda x: Enumerable(x.iterdir()).where(lambda p: p.suffix == '.tif').to_list()
    return [path.stem for path in folder.lsTif()]