import unittest
import jenkinsadmin2

class TestJenkinsServer(unittest.TestCase):
    def test_server_stop(self):
        result = jenkinsadmin2.stopserver()
        self.assertEqual(result, 'down')
    def test_server_start(self):
        result = jenkinsadmin2.startserver()
        self.assertEqual(result, 'up')
    

class TestJenkinsJobs(unittest.TestCase):

    def test_job_build(self):
        r = jenkinsadmin2.startserver
        if r == 'up':
            result = jenkinsadmin2.job_action('maven2','build')
            print(result)
            lastbuild = jenkinsadmin2.server.get_job('maven2').get_last_build()
            print(lastbuild)
            self.assertEqual(result, lastbuild)
        

if __name__ == '__main__':
    unittest.main()