# -*- coding: utf-8 -*-
#
# Copyright 2012 Julie Smith.  All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


url_discussion_group = "groups.google.com/group/tasks-backup"

email_discussion_group = "tasks-backup@googlegroups.com"

url_issues_page = "github.com/Google-Tasks-Backup/tasks-backup/issues"

url_source_code = "github.com/Google-Tasks-Backup/tasks-backup"

# Must match name in queue.yaml
PROCESS_TASKS_REQUEST_QUEUE_NAME = 'process-tasks-request'

# The string used used with the params dictionary argument to the taskqueue, 
# used as the key to retrieve the value from the task queue
TASKS_QUEUE_KEY_NAME = 'user_email'

WELCOME_PAGE_URL = '/'

MAIN_PAGE_URL = '/main'

START_BACKUP_URL = '/startbackup'

PROGRESS_URL = '/progress'

RESULTS_URL = '/results'

WORKER_URL = '/worker'

DB_KEY_TASKS_BACKUP_DATA = 'tasks_backup_data'

# The number of seconds to wait before a URL fetch times out.
# The deault timeout is 5 seconds, but that results in significant numbers
# of DeadlineExceededError, especially when retrieving credentials.
# Hopefully, increasing the timeout will reduce the number of DeadlineExceededError
#   Used as a parameter to fetch_with_deadline()
URL_FETCH_TIMEOUT = 12

# Number of times to try server actions
# Exceptions are usually due to DeadlineExceededError on individual API calls
# The first (NUM_API_TRIES - 2) retries are immediate. The app sleeps for 
# WORKER_API_RETRY_SLEEP_DURATION or FRONTEND_API_RETRY_SLEEP_DURATION seconds 
# before trying the 2nd last and last retries.
NUM_API_TRIES = 4

# Number of seconds for worker to sleep for the last 2 API retries
# This affects how often the job progress is updated, so MAX_JOB_PROGRESS_INTERVAL
# must be greater than all possible retry and sleep durations combined
WORKER_API_RETRY_SLEEP_DURATION = 45


# Number of seconds for frontend to sleep for the last API retries
# The total amount of time allowed for a page response is 60 seconds. 
# An API call times out after 5 seconds, so 4 API tries is up to 20 seconds
# The API_RETRY_SLEEP_DURATION should be less than 
# (60 - (NUM_API_TRIES - 2) * 5 - (2 * (5 + FRONTEND_API_RETRY_SLEEP_DURATION)))
# i.e., if NUM_API_TRIES = 4, FRONTEND_API_RETRY_SLEEP_DURATION should be LESS than 20 sec
FRONTEND_API_RETRY_SLEEP_DURATION = 18

# Number of seconds to allow for job to start
# Log and display an error if job has not started after this number of seconds.
# Must be less than 3600*24 (the number of seconds in one day)
MAX_TIME_ALLOWED_FOR_JOB_TO_START = 900


# If the job hasn't been updated in MAX_JOB_PROGRESS_INTERVAL seconds, assume that the job has stalled, 
# and display error message and stop refreshing progress.html
# Longest observed time between job added to taskqueue, and worker starting, is 94.5 seconds
# Note that WORKER_API_RETRY_SLEEP_DURATION affects how long between job progress updates, 
# so MAX_JOB_PROGRESS_INTERVAL must be greater than all possible retry and sleep durations combined
MAX_JOB_PROGRESS_INTERVAL = 125

# Every time that the worker starts a particular backup job, the number_of_job_starts counter is incremented.
# To prevent infinite loop of a 'bad' backup job, we only allow the job to be started MAX_NUM_JOB_STARTS times.
MAX_NUM_JOB_STARTS = 3

# Update number of tasks in tasklist every TASK_COUNT_UPDATE_INTERVAL seconds
# This prevents excessive Datastore Write Operations which can exceed quota
TASK_COUNT_UPDATE_INTERVAL = 5

# Refresh progress page every PROGRESS_PAGE_REFRESH_INTERVAL seconds
PROGRESS_PAGE_REFRESH_INTERVAL = 6

# Number of pixels for each depth level for sub-tasks
# e.g., for a 3rd level subtask, indent would be 3 * TASK_INDENT
TASK_INDENT = 40


# If the user has more than this number of tasks, display a warning message that
# displaying as an HTML page may fail
LARGE_LIST_HTML_WARNING_LIMIT = 20000



# ###############################################
#                  Debug settings
# ###############################################

# Extra detailed and/or personal details may be logged when user is one of the test accounts
# These are also the only accounts allowed to access LIMITED_ACCESS_SERVERS
TEST_ACCOUNTS = ["Test1@gmail.com", "Test2@gmail.com", "Test3@gmail.com"]


# List of hostname(s) of the production server(s). Used to identify if app is running on production server.
# The first in the list is used as the URL to direct user to production server.
# This is primarily used when testing GTI on a non-production server, but we want to see what it
# would look like on the production server. It is also used when using a subdomain of the main server,
# e.g. test1.import-tasks.appspot.com
PRODUCTION_SERVERS = ['tasks-backup.appspot.com', 'test-gtb-0-9-dot-tasks-backup.appspot.com', 'localhost']

# If True, and app is not running on one of the PRODUCTION_SERVERS, display message to user which includes
# link to the production server. Do not display any active content to the user.
DISPLAY_LINK_TO_PRODUCTION_SERVER = True

# Display log menu option on the Progress page if user is in SHOW_LOG_OPTION_USERS
SHOW_LOG_OPTION_USERS = ["Test.User@gmail.com", "another.user@gmail.com"]

# Logs dumps of raw data for test users when True
DUMP_DATA = False


