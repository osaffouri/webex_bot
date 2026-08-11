import logging

log = logging.getLogger(__name__)

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    APSCHEDULER_AVAILABLE = True
except ImportError:
    APSCHEDULER_AVAILABLE = False
    BackgroundScheduler = None


class BotScheduler:
    def __init__(self, bot):
        if not APSCHEDULER_AVAILABLE:
            raise ImportError(
                "APScheduler is required to use bot scheduling features. "
                "Install it with `pip install webex_bot[scheduler]`"
            )
        self.bot = bot
        self.scheduler = BackgroundScheduler()
        
    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()

    def stop(self):
        if self.scheduler.running:
            self.scheduler.shutdown()

    def __getattr__(self, name):
        '''Delegate to the underlying BackgroundScheduler.'''
        return getattr(self.scheduler, name)