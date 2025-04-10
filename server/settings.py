"""Settings for the addon."""
from typing import Any, Dict

from ayon_server.settings import BaseSettingsModel

DEFAULT_VALUES: Dict[str, Any] = {}


class MySettings(BaseSettingsModel):
    """Settings for the addon."""
