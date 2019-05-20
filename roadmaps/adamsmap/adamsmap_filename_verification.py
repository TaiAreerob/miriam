#!/usr/bin/env python3
import re

BASE_NAME =".*\/[a-z]_[0-9]+_[0-9]+\."
RESULT_FILE = re.compile(BASE_NAME + "pkl")
EVAL_FILE = re.compile(BASE_NAME + "pkl.eval")


def is_result_file(fname):
    return bool(RESULT_FILE.match(fname))


def is_eval_file(fname):
    return bool(RESULT_FILE.match(fname))


def resolve(fname):
    return fname.split("/")[-1].split(".")[0].split("_")


def resolve_mapname(fname):
    return "maps/" + resolve(fname)[0] + ".png"


def resolve_number_of_nodes(fname):
    return int(resolve(fname)[1])


def resolve_number_of_iterations(fname):
    return int(resolve(fname)[2])
