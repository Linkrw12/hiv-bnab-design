"""X"""

import click
import torch
from pathlib import Path
import pandas as pd
import warnings
from utils import (
    FileTypeConverter,
    InteractionIO,
)
from loguru import logger
import glob

# from utils.processing import InteractionProcessor
# from utils.io import InteractionIO

@click.command()
@click.option("-i", "--input", "samplesheet", type=click.Path(), help="X")
@click.option("-o", "--output", type=click.Path(), help="X")
@click.option("-s", "--structure", type=click.Path(), help="Either directory containing structures OR individual structure. Can be used in tandem with --input to process both files")
@click.option("-c", "--structure-config", type=click.Path(), help="X")
def predict_affinity(samplesheet, output, structure_config, structure):
    """Predict binding affinity of structure"""
    print(samplesheet, type(samplesheet))
    print(output)
    print(structure_config)
    print(structure)
    print("---")

    # Sample sheet (Sample name, path)
    # Load data
    # loader = InteractionIO()
    # structures = []
    # if samplesheet:
    #     samplesheet_files = loader.load_interaction_samplesheet(samplesheet)
    #     outputs.extend(samplesheet_files)
    # if structure:
    #     pass
        

    # Process data
    processor = ''
    # Load model
    # Predict affinity
    # Save outputs (csv w/ sample name & affinity columns)


if __name__ == "__main__":
    predict_affinity()
