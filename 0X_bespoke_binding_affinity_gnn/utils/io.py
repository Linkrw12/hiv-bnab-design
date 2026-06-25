"""
X
Description: Holds the scripts to load and save

"""

from pathlib import Path
import pandas as pd
import torch
from .models import AbAffinityPredictionModel
import glob


class InteractionIO:
    """
    X
    """

    def load_interaction_samplesheet(self, path: Path) -> pd.DataFrame:
        df = pd.read_csv(path)
        return df

    # main input loading script
    def load_data(self, inpath: Path):
        pass

    # Main script
    def save_output(self, df: pd.DataFrame, outpath: Path) -> None:
        df.to_csv(outpath, index=False)


def load_interaction_model(checkpoint_path: Path) -> AbAffinityPredictionModel:
    model = AbAffinityPredictionModel.load_from_checkpoint(checkpoint_path)
    return model
