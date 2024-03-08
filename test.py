import unittest
import generatorModule as gen
class testClass(unittest.TestCase):
        

        def test_random_number_within_range_age(self):
            for _ in range(1000):  
                result = gen.randomAge()
                self.assertTrue(17 <= result[0] <= 39)


        def test_random_number_within_range_id(self):
            for _ in range(1000):  
                result = gen.randomId()
                self.assertTrue(10000000 <= result <= 99999999)

        def test_value_in_list_Foot(self):
            foot = ['RIGHT', 'LEFT']
            for _ in range(100):  
                selected_value = gen.randomFoot()
                self.assertIn(selected_value[0], foot)


        def test_value_in_list_Foot(self):
            pos =  {
        'GOALKEEPER': ['GOALKEEPER'],
        'DEFENDER': ['CENTRAL', 'SIDE'],
        'MIDFIELDER': ['DEFENSIVE', 'CENTRAL MIDFIELDER', 'ATTACKING MIDFIELDER', 'LEFT WINGER', 'RIGHT WINGER'],
        'FORWARD': ['STRIKER', 'SECOND STRIKER', 'WINGER']
        }
            for _ in range(100): 
                position, subPosition = gen.randomPosition()
                self.assertIn(position, pos.keys())
                self.assertIn(subPosition, pos[position])

        
        


if __name__ == '__main__':
    unittest.main()