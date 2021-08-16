from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_User_get_temperature(self):
        res=self.client.get(self.locationUrl)
        

        self.assertEqual(res.status_code,200)