import os
import subprocess
import typing
from typing import Optional, List, Dict, Any, Tuple

import requests
import ayon_api

from ayon_core.addon import AYONAddon, IPluginPaths
from ayon_core.lib import CacheItem

from .version import __version__

class TextureLoaderAddon(AYONAddon, IPluginPaths):
    name = "texture_loader"
    version = __version__

    def initialize(self, studio_settings):
        self.log.info((
            "Texture Loader Addon initialized successfully."
        ))
        self._local_settings_cache = CacheItem(lifetime=60)