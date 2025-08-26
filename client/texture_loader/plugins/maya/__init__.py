"""Maya integration for the Texture Loader addon."""

from maya import cmds, mel


def install() -> None:
    """Create Fireframe menu with Texture Loader item in Maya."""
    main_window = mel.eval("$tmp=$gMainWindow")
    if cmds.menu("fireframeMenu", exists=True):
        cmds.deleteUI("fireframeMenu")
    fireframe_menu = cmds.menu(
        "fireframeMenu", label="Fireframe", parent=main_window
    )
    cmds.menuItem(
        label="Texture Loader",
        parent=fireframe_menu,
        command=lambda *_: cmds.confirmDialog(
            title="Texture Loader",
            message="Texture Loader Addon loaded successfully",
            button=["OK"],
        ),
    )
