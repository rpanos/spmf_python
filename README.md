# spmf_python 0.3
Support tools in Python for SPMF

The following python package contains tools that will enable a developer to utilize [SPMF](http://www.philippe-fournier-viger.com/spmf/) at a greater scale calling the Java based tool using Python.

In many scenarios, pattern mining involves managing large sets of association rules that themselves need to be managed, or mined, if you will.

Many of these tools are inspired by the years I was able to leverage this great open source tool to conduct thousands of pattern mining studies during my PhD dissertation at ASU.  This is very much an ongoing effort and suggestions on future features would be trmendously appreciated.

## Modules

### SPMF Results Parsers (beta)
This module is intended to make large SPMF result sets very managable.  The rule sets are stored as python objects that are available to developers but also provides a wrappers around largesets of rule sets.  These wrappers are intended to make the rule sets very searchable.

### SPMF Manager (very beta)

## Set Up

1. run: pip install requirements.txt
2. Set environment variable SPMF_HOME *or* place a copy of the SPMF.jar in the root of this packages directory

## Running Tests

1. from package root run: nosetests

## Warning
This module is ultimatley designed to be used as a dependancy but package 'SPMF Manager' and its ability to call SPMF.jar in different environments are very much in beta.  Pls start with SPMF Results Parsers first.
