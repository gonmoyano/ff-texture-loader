import os

from .addon import TextureLoaderAddon
from .version import __version__

AYON_TEXTURE_LOADER_ROOT = os.path.dirname(os.path.abspath(__file__))

__all__ = (
    "TextureLoaderAddon",
    "AYON_TEXTURE_LOADER_ROOT",
    "__version__"
)
