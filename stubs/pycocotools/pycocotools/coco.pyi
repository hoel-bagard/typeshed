from _typeshed import Incomplete, Self
from pathlib import Path
from typing import Generic, TypeVar, overload
from typing_extensions import Literal, TypeAlias, TypedDict

from . import _EncodedRLE

# TODO: Use numpy types when #5768 is resolved.
# import numpy as np
# import numpy.typing as npt

PYTHON_VERSION: Incomplete
_NDArray: TypeAlias = Incomplete

class _Image(TypedDict):
    id: int
    width: int
    height: int
    file_name: str

_TPolygonSegmentation: TypeAlias = list[list[float]]

class _RLE(TypedDict):
    size: list[int]
    counts: list[int]

class _Annotation(TypedDict):
    id: int
    image_id: int
    category_id: int
    segmentation: _TPolygonSegmentation | _RLE | _EncodedRLE
    area: float
    bbox: list[float]
    iscrowd: int

_TSeg = TypeVar("_TSeg", _TPolygonSegmentation, _RLE, _EncodedRLE)

class _AnnotationG(TypedDict, Generic[_TSeg]):
    id: int
    image_id: int
    category_id: int
    segmentation: _TSeg
    area: float
    bbox: list[float]
    iscrowd: int

class _Category(TypedDict):
    id: int
    name: str
    supercategory: str

class _Dataset(TypedDict):
    images: list[_Image]
    annotations: list[_Annotation]
    categories: list[_Category]

class COCO:
    anns: dict[int, _Annotation]
    dataset: _Dataset
    cats: dict[int, _Category]
    imgs: dict[int, _Image]
    imgToAnns: dict[int, list[_Annotation]]
    catToImgs: dict[int, list[int]]
    def __init__(self, annotation_file: str | Path | None = ...) -> None: ...
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
    def loadRes(self: Self, resFile: str) -> Self: ...
    def download(self, tarDir: str | None = ..., imgIds: list[int] = ...) -> Literal[-1] | None: ...
    def loadNumpyAnnotations(self, data: _NDArray) -> list[_Annotation]: ...
    # def loadNumpyAnnotations(self, data: npt.NDArray[np.float64]) -> list[_Annotation]: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_RLE]) -> _RLE: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_EncodedRLE]) -> _EncodedRLE: ...
    @overload
    def annToRLE(self, ann: _AnnotationG[_TPolygonSegmentation]) -> _EncodedRLE: ...
    def annToMask(self, ann: _Annotation) -> _NDArray: ...
    # def annToMask(self, ann: _Annotation) -> npt.NDArray[np.uint8]: ...
