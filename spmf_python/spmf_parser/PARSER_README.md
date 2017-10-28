# SPMF Output Parsers

## SPMFOutputRule

Root class of the out put parser.  For the algorithms based on integer representations of events.
Members include:

- antcedants_int: list of antcedant ints
- consequents_int: list of consequents ints
- stats: dict of rule stats


## SPMFResultSet

Rules are stored in three ways.  In a python dict based on the events in the antcedants and a python dict based on the events in the consequents.

### Methods for adding rules to a SPMFResultSet
