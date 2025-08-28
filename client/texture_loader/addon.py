"""Texture Loader addon entry point."""

import os,logging
from typing import Any, ClassVar,Dict, List

from ayon_core.addon import AYONAddon, IHostAddon,IPluginPaths
from ayon_core.lib import CacheItem

from .version import __version__

AYON_TEXTURE_LOADER_ROOT = os.path.dirname(os.path.abspath(__file__))

class TextureLoaderAddon(AYONAddon,IHostAddon,IPluginPaths):
    """Addon providing texture loading tools for multiple hosts."""

    name = "texture_loader"
    version = __version__
    host_name = "nuke"  # This can be "maya", "houdini", or "nuke"

    def initialize(self, studio_settings: Dict[str, Any]) -> None:
        """Initialize the addon."""
        super().initialize(studio_settings)
        #AYONAddon.__init__(self, studio_settings)
        self.log.info("Texture Loader Addon initialized successfully.")
        self.log.info("Tis modifed by me")
        #self._local_settings_cache = CacheItem(lifetime=60)

        #self.enabled = True

    @staticmethod
    def get_plugin_paths() -> Dict[str, List[str]]:
        """Return plug-in paths for supported DCC hosts."""
        base = os.path.dirname(__file__)

        plugins_dict={
            "maya": [os.path.join(base, "plugins", "maya")],
            "houdini": [os.path.join(base, "plugins", "houdini")],
            "nuke": [os.path.join(base, "plugins", "nuke")],
        }

        log = logging.getLogger(__name__)

        message = f"GET PLUGIN PATHS: {plugins_dict}"

        log.info(message)
        return plugins_dict

    def get_launch_hook_paths(self, app):

        self.log.info("GET LAUNCH HOOK PATHS", app.host_name)

        return [
            os.path.join(AYON_TEXTURE_LOADER_ROOT, "plugins\nuke\hooks")
        ]


    def on_host_install(self, host, host_name, project_name) -> None:

        self.log.info("Texture Loader install hook triggered")
        #host = os.environ.get("AYON_HOST")
        self.log.info(f"Detected host: {host}")

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
                self.log.info("Nuke menu installed")
            except Exception:  # noqa: BLE001
                self.log.warning("Failed to install Nuke menu", exc_info=True)
        elif host == "houdini":
            # Menu defined in Houdini XML plugin
            pass
