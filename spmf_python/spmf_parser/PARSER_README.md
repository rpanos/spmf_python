# SPMF Output Parsers

## SPMFOutputRule objects

Root class of the out put parser.  For the algorithms based on integer representations of events.
Members include:

- antcedants_int: list of antcedant ints
- consequents_int: list of consequents ints
- stats: dict of rule stats


## SPMFResultSet objects

Rules are stored in three ways.  In a python dict based on the events in the antcedants, a python dict based on the events in the consequents, and simply an unordered list.  To leverage this code, first utilize the many ways to add rules to a SPMFResultSet using the following functions and then search for specific rules using the subsequent search functions.

### Methods for adding rules to a SPMFResultSet

- add_rule_from_str(spmf_output_line)
  * accepts one line of an SPMF ouput
- add_rules(spmf_rule_ls)
  * accepts a list of SPMFOutputRule objects
- add_rules_str(spmf_rule_ls)
  * accepts a list of SPMF ouput strings
- add_rule(spmf_rule)
  * accepts a SPMFOutputRule objects
- load_result_set_from_file_handle(file_handle)
  * accepts a python filehhandle to an SPMF output file.

    This might be used like this:
```python
      spmf_output_example1 = os.path.join(os.path.abspath('spmf_data'), 'spmf_output_example1.txt')
      file_handle = open(spmf_output_example1)
      spmf_result_set = SPMFResultSet()
      spmf_result_set.load_result_set_from_file_handle(file_handle)
```

### Methods for search rules within a SPMFResultSet

Search Function | Aurguments | Purpose
--- | --- | ---
give_rules_w_antcedants | event list (ints) | all rules that have at least one these events as antecedants (union)
give_rules_w_all_antcedants | event list (ints) | all rules that have all these events as antecedants (intersection)
give_rules_w_out_all_antcedants | event list (ints) | all rules that do not have any of these events as antecedants 
give_rules_w_consequents | event list (ints) | all rules that have at least one these events as consequents (union)
give_rules_w_all_consequents | event list (ints) | all rules that have all these events as consequents (intersection)
give_rules_w_out_all_consequents | event list (ints) | all rules that do not have any of these events as consequents
