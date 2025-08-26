from typing import Type, Any

from ayon_server.addons import BaseServerAddon

from .settings import (
    TextureLoaderSettings,
    DEFAULT_VALUES,
)


class TextureLoader(BaseServerAddon):
    settings_model: Type[TextureLoaderSettings] = TextureLoaderSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)