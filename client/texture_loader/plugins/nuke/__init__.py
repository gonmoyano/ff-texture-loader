"""Nuke integration for the Texture Loader addon."""

import nuke


def install() -> None:
    """Create Fireframe menu with Texture Loader item in Nuke."""

    self.log.info("INSTALL FOR NUKE EXECUTED SUCCESSFULLY")

    toolbar = nuke.menu("Nuke")
    fireframe_menu = toolbar.findItem("Fireframe")
    if fireframe_menu is None:
        fireframe_menu = toolbar.addMenu("Fireframe")
    fireframe_menu.addCommand(
        "Texture Loader",
        lambda: nuke.message("Texture Loader Addon loaded successfully"),
    )
