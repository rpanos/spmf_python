# spmf_python 0.3
Support tools in Python for SPMF

The following python package contains tools that will enable a developer to utilize [SPMF](http://www.philippe-fournier-viger.com/spmf/) at a greater scale calling the Java based tool using Python.

In many scenarios, pattern mining involves managing large sets of association rules that themselves need to be managed, or mined, if you will.  Many of these tools are inspired by the years I was able to leverage this great open source tool to conduct thousands of pattern mining studies during my PhD dissertation at ASU.  This is very much an ongoing effort and suggestions on future features would be tremendously appreciated.

## Modules

### SPMF Results Parsers (beta)
This module is intended to make large SPMF result sets very managable.  Each rule is stored as python objects that are available to developers but also provides a wrappers around largesets of rule sets.  These wrappers are intended to make the rule sets very searchable.  [SPMF Results Parsers Details](/spmf_python/spmf_parser/PARSER_README.md)

### SPMF Manager (very beta)
This is to allow a developer, after configuring the location of SPMF.jar on their system using the environemnt variable SPMF_HOME, to call SPMF using python.  An example might be:

```python
spmf_manager = SPMFManager()
spmf_config_obj = SPMFconfigObjects("RuleGrowth", .5, .6)
spmf_manager.call_spmf(spmf_config_obj, in_file=in_file, out_file=out_file, over_write_ouput=True)
```
So far this also involves resuable SPMFconfigObjects that will manage valid calls to the algorithms.  Only a few algorithms are supported so far.

## Set Up

1. run: pip install requirements.txt
2. Set environment variable SPMF_HOME *or* place a copy of the SPMF.jar in the root of this packages directory

## Running Tests

1. from package root run: nosetests

## Warning
This package is ultimatley designed to be used as a dependancy in another Python repo but the package 'SPMF Manager' and its ability to call SPMF.jar in different environments are very much in beta.  If you decide to use it as a pip installed dependancy, pls try using SPMF Results Parsers first and use SPMF Manager at your own risk.  If you are able to set the SPMF_HOME env variable then it should work in theory but it has not been properly tested in other environments yet.
