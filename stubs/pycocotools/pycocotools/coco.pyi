from _typeshed import Incomplete
from pathlib import Path
from typing import overload
from typing_extensions import Literal, Self, TypeAlias

# import numpy as np
# import numpy.typing as npt

from .coco_types import _RLE, _Annotation, _AnnotationG, _Category, _Dataset, _EncodedRLE, _Image, _TPolygonSegmentation

PYTHON_VERSION: Incomplete
_NDArray: TypeAlias = Incomplete

class COCO:
    anns: dict[int, _Annotation]
    dataset: _Dataset
    cats: dict[int, _Category]
    imgs: dict[int, _Image]
    imgToAnns: dict[int, list[_Annotation]]
    catToImgs: dict[int, list[int]]
    def __init__(self, annotation_file: str | Path = ...) -> None: ...
    def createIndex(self) -> None: ...
    def info(self) -> None: ...
    def getAnnIds(
        self, imgIds: list[int] | int = ..., catIds: list[int] | int = ..., areaRng: list[float] = ..., iscrowd: bool | None = ...
    ) -> list[int]: ...
    def getCatIds(
        self, catNms: list[str] | str = ..., supNms: list[str] | str = ..., catIds: list[int] | int = ...
    ) -> list[int]: ...
    def getImgIds(self, imgIds: list[int] | int = ..., catIds: list[int] | int = ...) -> list[int]: ...
    def loadAnns(self, ids: list[int] | int = ...) -> list[_Annotation]: ...
    def loadCats(self, ids: list[int] | int = ...) -> list[_Category]: ...
    def loadImgs(self, ids: list[int] | int = ...) -> list[_Image]: ...
    def showAnns(self, anns: list[_Annotation], draw_bbox: bool = ...) -> None: ...
    def loadRes(self, resFile: str) -> Self: ...
    def download(self, tarDir: str | None = ..., imgIds: list[int] = ...) -> Literal[-1] | None: ...
    def loadNumpyAnnotations(self, data: _NDArray) -> list[_Annotation]: ...
    # def loadNumpyAnnotations(self, data: npt._NDArray[np.float64]) -> list[_Annotation]: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_RLE]) -> _RLE: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_EncodedRLE]) -> _EncodedRLE: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_TPolygonSegmentation]) -> _EncodedRLE: ...
    def annToMask(self, ann: _Annotation) -> _NDArray: ...
    # def annToMask(self, ann: _Annotation) -> npt._NDArray[np.uint8]: ...
