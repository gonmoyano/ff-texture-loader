"""Texture Loader addon entry point."""

import os
from typing import Any, Dict, List

from ayon_core.addon import AYONAddon, IPluginPaths
from ayon_core.lib import CacheItem

from .version import __version__


class TextureLoaderAddon(AYONAddon, IPluginPaths):
    """Addon providing texture loading tools for multiple hosts."""

    name = "texture_loader"
    version = __version__

    def initialize(self, studio_settings: Dict[str, Any]) -> None:
        """Initialize the addon."""
        self.log.info("Texture Loader Addon initialized successfully.")
        self._local_settings_cache = CacheItem(lifetime=60)

    @staticmethod
    def get_plugin_paths() -> Dict[str, List[str]]:
        """Return plug-in paths for supported DCC hosts."""
        base = os.path.dirname(__file__)
        return {
            "maya": [os.path.join(base, "plugins", "maya")],
            "houdini": [os.path.join(base, "plugins", "houdini")],
            "nuke": [os.path.join(base, "plugins", "nuke")],
        }

    def install(self) -> None:
        """Install host-specific menus."""
        host = os.environ.get("AYON_HOST")
        if host == "maya":
            try:
                from .plugins import maya as maya_plugins

                maya_plugins.install()
            except Exception:  # noqa: BLE001
                self.log.warning("Failed to install Maya menu", exc_info=True)
        elif host == "nuke":
            try:
                from .plugins import nuke as nuke_plugins

                nuke_plugins.install()
            except Exception:  # noqa: BLE001
                self.log.warning("Failed to install Nuke menu", exc_info=True)
        elif host == "houdini":
            # Menu defined in Houdini XML plugin
            pass
