

from spmf_line_parsers import parse_line


class SPMFOutputRule(object):

    def __init__(self, antcedants_int, consequents_int, stats):
        self.antcedants_int = antcedants_int
        self.consequents_int = consequents_int
        self.stats = stats

    def __unicode__(self):
        return str(self.antcedants_int) + " ==> " + str(self.consequents_int)


class SPMFResultSet(object):

    def __init__(self):
        self.rules_by_antcedants = {}
        self.rules_by_consequents = {}
        self.all_rules = []

    def add_rule_from_str(self, spmf_output_line):

        spmf_rule = SPMFOutputRule(*parse_line(spmf_output_line))
        self.add_rule(spmf_rule)

    def add_rules(self, spmf_rule_ls):
        for spmf_rule in spmf_rule_ls:
            self.add_rule(spmf_rule)

    def add_rules_str(self, spmf_rule_ls):
        for spmf_rule in spmf_rule_ls:
            self.add_rule_from_str(spmf_rule)

    def add_rule(self, spmf_rule):
        self.all_rules.append(spmf_rule)
        for ant_event in spmf_rule.antcedants_int:
            if ant_event in self.rules_by_antcedants:
                self.rules_by_antcedants[ant_event].append(spmf_rule)
            else:
                self.rules_by_antcedants[ant_event] = [spmf_rule]

        for cons_event in spmf_rule.consequents_int:
            if cons_event in self.rules_by_consequents:
                self.rules_by_consequents[cons_event].append(spmf_rule)
            else:
                self.rules_by_consequents[cons_event] = [spmf_rule]

    def load_result_set_from_file_handle(self, file_handle):
        with file_handle as f:
            for idx, line in enumerate(f):
                self.add_rule_from_str(line)

    def give_rules_w_antcedants(self, event_ls):
        rule_set = set()
        for event in event_ls:
            if event in self.rules_by_antcedants:
                rule_set.update(self.rules_by_antcedants[event])

        return list(rule_set)

    def give_rules_w_all_antcedants(self, event_ls):

        rule_set = set()
        for event in event_ls:
            if event not in self.rules_by_antcedants:
                continue
            if len(rule_set) == 0:
                rule_set = set(self.rules_by_antcedants[event])
            else:
                rule_set = rule_set.intersection(set(self.rules_by_antcedants[event]))
        return list(rule_set)

    def give_rules_w_out_all_antcedants(self, event_ls):
        rule_set = set(self.all_rules)
        for event in event_ls:
            rule_set = rule_set - set(self.rules_by_antcedants[event])
        return list(rule_set)

    def give_rules_w_consequents(self, event_ls):
        rule_set = set()
        for event in event_ls:
            if event in self.rules_by_consequents:
                rule_set.update(self.rules_by_consequents[event])

        return list(rule_set)

    def give_rules_w_all_consequents(self, event_ls):

        rule_set = set()
        for event in event_ls:
            if event not in self.rules_by_consequents:
                continue
            if len(rule_set) == 0:
                rule_set = set(self.rules_by_consequents[event])
            else:
                rule_set = rule_set.intersection(set(self.rules_by_consequents[event]))
        return list(rule_set)

    def give_rules_w_out_all_consequents(self, event_ls):
        rule_set = set(self.all_rules)
        for event in event_ls:
            rule_set = rule_set - set(self.rules_by_consequents[event])
        return list(rule_set)

