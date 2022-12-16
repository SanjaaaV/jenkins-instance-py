import unittest
import jenkinsadmin2

class TestJenkinsServer(unittest.TestCase):
    def test_server_stop(self): 
        result =jenkinsadmin2.stopserver()
        self.assertEqual(result, 'down')

    def test_server_start(self):
        result = jenkinsadmin2.startserver()
        self.assertEqual(result, 'up')
    
    def start_server():
        jenkinsadmin2.startserver()

    def test_server_backup(self):
        result = jenkinsadmin2.backupserver("try", "9ae6f859ec58")
        rstr = str(result)
        exists = "<Image: 'try:latest'>"
        self.assertEqual(rstr, exists)

    def rm_image():
        jenkinsadmin2.client.images.remove("try")
    

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