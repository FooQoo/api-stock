#!/usr/bin/env bash

# shellcheck source=env.conf
. "$1"

heroku config:add SECRET_KEY="${SECRET_KEY}"
heroku config:add NAME="${NAME}"
heroku config:add HOST="${HOST}"
heroku config:add USER="${USER}"
heroku config:add PORT="${PORT}"
heroku config:add PASSWORD="${PASSWORD}"
