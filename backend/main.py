from plugins import base_plugin


class Plugin(base_plugin.Plugin):
    def load(self) -> bool:
        return True

    def unload(self) -> bool:
        return True

    def health(self) -> bool:
        return True

    def image(self) -> str:
        return 'sample.svg'

    @property
    def name(self) -> str:
        return 'A-PluginTemplate'


def init() -> Plugin:
    return Plugin()
