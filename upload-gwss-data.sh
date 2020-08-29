#!/bin/bash

set -xeu

gsutil -m rsync -ru data/gwss/ gs://ag1000g-release/phase2.selection.20200828/gwss/
