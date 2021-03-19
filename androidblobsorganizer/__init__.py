from androidblobsorganizer.utils.section import register_sections
import os
from pathlib import Path

__version__ = "0.1.0"

module_path = Path(__file__).parent
sections_path = module_path / "sections"
current_path = Path(os.getcwd())

register_sections(sections_path)
