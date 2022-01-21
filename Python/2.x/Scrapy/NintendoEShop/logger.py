# coding: utf-8
import logging

logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s [%(filename)s:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
