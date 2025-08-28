from ayon_applications import PreLaunchHook
import logging

log = logging.getLogger(__name__)

class PrelaunchNukeAssistHook(PreLaunchHook):

    def execute(self):
        log.info("Prelaunch hook executed")