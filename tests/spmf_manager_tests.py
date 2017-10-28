
import unittest, os
from spmf_python.spmf_manager.spmf_run import SPMFManager, SPMFconfigObjects

class TestSPMFManager(unittest.TestCase):

    def setUp(self):
        self.spmf_config_obj = SPMFconfigObjects("RuleGrowth", .5, .6)

    def test_spmf_configs(self):
        spmf_config_obj = SPMFconfigObjects("RuleGrowth", .5, .6)
        self.assertIsNotNone(spmf_config_obj)


    '''
        In order for this test to pass, you need to set the environment variable SPMF_HOME

        export SPMF_HOME=/path/to/SPMF.java

    '''
    def test_managers(self):
        # dir_path = os.path.dirname(os.path.realpath(__file__))

        path_data_dir = os.path.abspath('spmf_data')

        spmf_home = None
        try:
            spmf_home = os.environ['SPMF_HOME']
        except Exception as e:
            # Todo add logs!
            print " SPMF_HOME env variable not set - assuming SPMF.jar is in package root dir"

        if not spmf_home:
            spmf = open(os.path.join(path_data_dir, 'SPMF.jar'))  # TEMP path_data_dir
        else:
            spmf = open(spmf_home)

        spmf_manager = SPMFManager(spmf)
        self.assertIsNotNone(spmf_manager)

        in_file = os.path.join(path_data_dir, 'in_file.spmf')
        out_file = os.path.join(path_data_dir, 'out3.txt')

        spmf_manager.call_spmf(self.spmf_config_obj, in_file=in_file, out_file=out_file, over_write_ouput=True)