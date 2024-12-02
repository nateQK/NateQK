#!/bin/bash

cd bot/utils/database

alembic revision --autogenerate
