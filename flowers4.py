from pathlib import Path

from .easy_set import EasySet

FLOWER4_SPECS_DIR = Path("data/Flowers4")


class Flowers4(EasySet):
    def __init__(self, split: str, **kwargs):
        """
        Build the flowers dataset for the specific split.
        Args:
            split: one of the available split (typically train, val, test).
        Raises:
            ValueError: if the specified split cannot be associated with a JSON spec file
                from Flowers' specs directory
        """
        specs_file = FLOWER4_SPECS_DIR / f"{split}.json"
        if not specs_file.is_file():
            raise ValueError(
                f"Could not find specs file {specs_file.name} in {FLOWER4_SPECS_DIR}"
            )
        super().__init__(specs_file=specs_file, **kwargs)