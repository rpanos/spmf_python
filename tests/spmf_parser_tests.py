
import unittest
# from spmf_python.spmf_parser.spmf_parser import SPMFResultSet
from spmf_python.spmf_parser.spmf_parser import SPMFResultSet

class TestSPMFResultSet(unittest.TestCase):
    def setUp(self):
        self.spmf_result_set = SPMFResultSet()

        self.example_output = ["348,807 ==> 254 #SUP: 10 #CONF: 0.008888888888888889 #LIFT: 0.4936752136752136",
            "348,821 ==> 254 #SUP: 16 #CONF: 0.02059202059202059 #LIFT: 1.1436491436491436",
            "348,823 ==> 254 #SUP: 49 #CONF: 0.059322033898305086 #LIFT: 3.2946544980443284",
            "348,824 ==> 254 #SUP: 16 #CONF: 0.012678288431061807 #LIFT: 0.704132634402048",
            "348,827 ==> 254 #SUP: 9 #CONF: 0.21951219512195122 #LIFT: 12.191369606003752",
            "348,843 ==> 254 #SUP: 10 #CONF: 0.05952380952380952 #LIFT: 3.3058608058608057",
            "254,255 ==> 349 #SUP: 22 #CONF: 0.4230769230769231 #LIFT: 2.036410256410256",
            "254,348 ==> 349 #SUP: 22 #CONF: 0.4230769230769231 #LIFT: 2.036410256410256"]

    def test_add_rule(self):

        temp_spmf_result_set = SPMFResultSet()
        temp_spmf_result_set.add_rule_from_str(
            "1,2 ==> 3 #SUP: 10 #CONF: 0.008888888888888889 #LIFT: 0.4936752136752136")
        self.assertEqual(len(temp_spmf_result_set.all_rules), 1)
        rules_with_1 = temp_spmf_result_set.give_rules_w_antcedants([1])
        self.assertEqual(len(rules_with_1), 1)
        self.assertEqual(rules_with_1[0].antcedants_int, [1, 2])
        self.assertEqual(rules_with_1[0].consequents_int, [3])

        for example_rule in self.example_output:
            self.spmf_result_set.add_rule_from_str(example_rule)

        self.assertEqual(len(self.spmf_result_set.all_rules), 8)

        rule_set_2 = self.spmf_result_set.give_rules_w_antcedants([348, 823, 348])
        self.assertEqual(len(rule_set_2), 7)

        rule_set_3 = self.spmf_result_set.give_rules_w_all_antcedants([348, 823, 348])
        self.assertEqual(len(rule_set_3), 1)

        print " rule_set_2: " + str(len(rule_set_2))
        print " rule_set_3: " + str(len(rule_set_3))

        # SPMFOutputRule([1,2], [3])

    def test_w_out_rule(self):
        temp_spmf_result_set = SPMFResultSet()
        temp_spmf_result_set.add_rules_str(self.example_output)
        rules_wo_254 = temp_spmf_result_set.give_rules_w_out_all_consequents([254])
        self.assertEqual(len(rules_wo_254), 2)

        temp_spmf_result_set_2 = SPMFResultSet()
        temp_spmf_result_set_2.add_rules_str(self.example_output)
        rules_wo_254 = temp_spmf_result_set_2.give_rules_w_out_all_antcedants([348])
        self.assertEqual(len(rules_wo_254), 1)



if __name__=='__main__':
    TestSPMFResultSet.test_add_rule()