"""
X
"""

from __future__ import annotations

from pathlib import Path
from Bio.PDB import MMCIFParser, PDBIO


class FileTypeConverter:
    """
    Util class meant to handle conversion of file names from
    one extension to another
    """

    def _load_cif(self, cif_path: Path):
        cif_parser = MMCIFParser(QUIET=True)
        structure = cif_parser.get_structure("structure_id", cif_path)
        return structure

    def _write_structure_to_pdb(self, structure, pdb_path) -> None:
        io = PDBIO()
        io.set_structure(structure)
        io.save(pdb_path)

    def cif_to_pdf(self, cif_path: Path, pdb_path: Path) -> None:
        """Graphein needs data to be in PDB format, so converting
        for the sake of proper inputs
        """
        structure = self._load_cif(cif_path)
        self._write_pdb(structure)
