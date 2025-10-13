import threading
from binaryninja import Logger
from binaryninjaui import UIContext

class UIManagerRegistry(object):
    def __init__(self):
        self._managers = {}
        self._lock = threading.RLock()

    def get_or_create(self, session_id):
        if session_id is None:
            return None

        with self._lock:
            if session_id not in self._managers:
                from .ui.ui_manager import UIManager
                self._managers[session_id] = UIManager()
            return self._managers[session_id]

    def get(self, session_id):
        if session_id is None:
            return None
        with self._lock:
            return self._managers.get(session_id)

    def remove(self, session_id):
        if session_id is None:
            return
        with self._lock:
            if session_id in self._managers:
                del self._managers[session_id]

    def get_active(self):
        ctx = UIContext.activeContext()
        if ctx is None:
            return None
        view_frame = ctx.getCurrentViewFrame()
        if view_frame is None:
            return None
        view_interface = view_frame.getCurrentViewInterface()
        if view_interface is None:
            return None
        bv = view_interface.getData()
        if bv is None or bv.file is None:
            return None

        session_id = bv.file.session_id
        return self.get_or_create(session_id)

uimanager_registry = UIManagerRegistry()

# Global logger instance
logger = Logger(0, "SENinja")