"""Settings for the addon."""
from typing import Any

from ayon_server.settings import BaseSettingsModel, SettingsField

DEFAULT_VALUES: dict[str, Any] = {}

class GeneralSettingsModel(BaseSettingsModel):
    add_self_publish_button: bool = SettingsField(
        False,
        title="A random test button"
    )

DEFAULT_GENERAL_SETTINGS = {
    "random_test_button": False,
}

class TextureLoaderSettings(BaseSettingsModel):
    general: GeneralSettingsModel = SettingsField(
        default_factory=GeneralSettingsModel,
        title="General"
    )

DEFAULT_VALUES = {
    "general": DEFAULT_GENERAL_SETTINGS
}
