"""
X
Description: Holds the scripts to load and save

"""
from __future__ import annotations
import lightning as L
import torch.nn.functional as F


class AbAffinityPredictionModel(L.LightningModule):
    def __init__(self, affinity_model):
        super().__init__()
        self.model = affinity_model

    def _generate_loss(self, batch, batch_idx):
        x, y = batch
        y_pred = self.affinity_model(x)
        loss = F.mse_loss(y_pred, y)
        return loss

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        loss = self._generate_loss(batch, batch_idx)
        return loss

    def validation_step(self, batch, batch_idx):
        # this is the validation loop
        val_loss = self._generate_loss(batch, batch_idx)
        self.log("val_loss", val_loss)

    def test_step(self, batch, batch_idx):
        # training_step defines the train loop.
        test_loss = self._generate_loss(batch, batch_idx)
        self.log("test_loss", test_loss)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        # optimizer = SAM()
        return optimizer
