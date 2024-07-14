import logging

from plombery.logger.formatter import JsonFormatter
from plombery.logger.web_socket_handler import WebSocketHandler
from logging import StreamHandler
from plombery.orchestrator.data_storage import get_logs_filename
from plombery.pipeline.context import task_context, run_context, pipeline_context


def get_logger() -> logging.Logger:
    """Get a logger for a task or pipeline. This function uses contexts
    so it must be called within a task function or within the internal
    functions that run a pipeline.

    Returns:
        Logger: a logger instance
    """

    pipeline = pipeline_context.get()
    task = task_context.get(None)
    pipeline_run = run_context.get()

    filename = get_logs_filename(pipeline_run.id)

    json_formatter = JsonFormatter(pipeline=pipeline.id, task=task.id if task else None)

    streamhandler = StreamHandler()
    streamhandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger_name = f"plombery.{pipeline_run.id}"

    if task:
        logger_name += f"-{task.id}"

    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        logger.addHandler(streamhandler)

    return logger
