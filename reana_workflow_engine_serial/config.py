# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA Workflow Engine Serial config."""

import logging
import os

SHARED_VOLUME_PATH = os.getenv('SHARED_VOLUME_PATH', '/var/reana')
"""Path to the mounted REANA shared volume."""

BROKER_URL = os.getenv('RABBIT_MQ_URL',
                       'message-broker.default.svc.cluster.local')

BROKER_USER = os.getenv('RABBIT_MQ_USER', 'test')

BROKER_PASS = os.getenv('RABBIT_MQ_PASS', '1234')

BROKER_PORT = os.getenv('RABBIT_MQ_PORT', 5672)

BROKER = os.getenv('RABBIT_MQ', 'amqp://{0}:{1}@{2}//'.format(BROKER_USER,
                                                              BROKER_PASS,
                                                              BROKER_URL))

MOUNT_CVMFS = os.getenv('REANA_MOUNT_CVMFS', 'false')

JOB_STATUS_POLLING_INTERVAL = os.getenv('POLLING_INTERVAL', 3)
"""Polling interval in seconds for status of running jobs."""

CACHE_ENABLED = False
"""Determines if jobs caching is enabled."""
