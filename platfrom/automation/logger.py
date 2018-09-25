# -*- coding: utf-8 -*-
import io
import logging.handlers

from platfrom.automation import setting


class AutoLogger:
    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "i"
    log_file = "result/auto_log.log"
    log_max_byte = 10 * 1024 * 1024;
    log_backup_count = 5

    @staticmethod
    def getLogger():
        if AutoLogger.logger is not None:
            return AutoLogger.logger

        AutoLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=AutoLogger.log_file, \
                                                           maxBytes=AutoLogger.log_max_byte, \
                                                           backupCount=AutoLogger.log_backup_count, encoding='utf-8')

        console = logging.StreamHandler(setting.log_capture_string)

        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s] %(message)s")
        log_handler.setFormatter(log_fmt)
        console.setFormatter(log_fmt)
        AutoLogger.logger.addHandler(log_handler)
        AutoLogger.logger.addHandler(console)
        AutoLogger.logger.setLevel(AutoLogger.levels.get(AutoLogger.log_level))
        return AutoLogger.logger
