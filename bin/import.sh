#!/usr/bin/env bash

this_script=$(readlink -e "$0")
this_script_dir=$(realpath $(dirname "${this_script}"))
toplevel_dir="$(realpath ${this_script_dir}/..)"

export PATH="${PATH}:${this_script_dir}"

rm -rf "${toplevel_dir}/content"
mv "$1/content" "${toplevel_dir}"
