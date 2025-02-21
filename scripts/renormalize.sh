#!/bin/bash

# Dev container uses a Linux container but windows and Linux
# have different ways of storing files (LF, CRLF) so it ends
# up thinking the files "changed" when it didn't
# This prevents that

git config --global core.autocrlf input
git add --renormalize .