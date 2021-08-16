from rest_framework.test import APITestCase



class TestSetup(APITestCase):
    def setUp(self):
        city="London",
        days="1"
        self.locationUrl=f"/api/location/{city}?days={days}"
      
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()