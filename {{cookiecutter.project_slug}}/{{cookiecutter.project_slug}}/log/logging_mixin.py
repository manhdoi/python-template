import logging


class LoggingMixin(object):
    """
    Logging class that should be extended by classes
    """
    _log: logging.Logger = None

    @property
    def log(self) -> logging.Logger:
        """
        Logger object

        :return: Logger object
        :rtype: logging.Logger
        """

        if not self._log:
            self._log = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)
        return self._log
