import unittest
import jenkinsadmin2

class TestJenkinsServer(unittest.TestCase):
    def test_server_stop(self): 
        result =jenkinsadmin2.stopserver()
        jenkinsadmin2.startserver()
        self.assertEqual(result, 'down')


    def test_server_start(self):
        result = jenkinsadmin2.startserver()
        self.assertEqual(result, 'down')

    

    
    

class TestJenkinsJobs(unittest.TestCase):

    def test_job_build(self):
        r = jenkinsadmin2.startserver
        if r == 'up':
            result = jenkinsadmin2.job_action('maven2','build')
            self.assertEqual(result, 'True')


    def test_job_stop(self):
        r = jenkinsadmin2.startserver
        if r == 'up':
            job_action('maven2','build')
            result = jenkinsadmin2.job_action('maven2','stop')
            self.assertEqual(result, 'False')
            
        

if __name__ == '__main__':
    unittest.main()
