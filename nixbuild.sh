#! /usr/bin/env bash
nix-shell -p python312 python312Packages.markdown --command ./build.sh
