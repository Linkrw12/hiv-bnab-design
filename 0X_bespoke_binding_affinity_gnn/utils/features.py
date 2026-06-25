"""
X
Description: Holds functions to transform protein structures into GNN-compatable features

"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
import inspect
from typing import Callable

import torch
from torch_geometric.data import Data

# Do I need to make a DatasetGraphAnnotator?? Add graph values to x?


class AbstractDatasetAnnotator(ABC):
    """
    Contains common class dicts that are required by both
    node and edge annotators
    """

    @property
    def handler(self) -> dict[str, Callable]:
        class_transformation_fncs = inspect.getmembers(
            self.__class__, predicate=inspect.isfunction
        )
        handler = {
            f"{fnc_name.removeprefix("_")}": transform_fnc
            for (fnc_name, transform_fnc) in class_transformation_fncs
            if fnc_name.startswith("_")
        }
        return handler


@dataclass
class DatasetNodeAnnotator(AbstractDatasetAnnotator):
    features: list[str]

    def _meiler_embedding(self, data: Data) -> torch.Tensor:
        return data.meiler.float()

    def set_node_x(self, data: Data) -> None:
        data.x = torch.concat(
            [self.handler[feature](self, data) for feature in self.features]
        )
        return data


@dataclass
class DatasetEdgeAnnotator(AbstractDatasetAnnotator):
    features: list[str]

    def _distance_to_edges(self, data: Data) -> torch.Tensor:
        return data.distance.reshape(-1, 1)

    def set_edge_attr(self, data: Data) -> None:
        data.edge_attr = torch.concat(
            [self.handler[feature](self, data) for feature in self.features]
        )
        return data
