import unittest
from pool_table_assignment import PoolTable
import datetime

class Pooltabletest(unittest.TestCase):

  def setUp(self):
    self.pool_table_test = PoolTable(1)

  def test_check_out(self):
    self.pool_table_test.check_out()
    self.assertFalse(self.pool_table_test.is_available)
    self.assertIsNotNone(self.pool_table_test.start_time)

  def test_check_in(self):
    self.pool_table_test.check_in()
    self.assertEqual(self.pool_table_test.is_available, True)
    self.assertIsNotNone(self.pool_table_test.end_time)

  def test_calculate_total(self):
      self.pool_table_test.check_out()
      self.pool_table_test.check_in()
      self.pool_table_test.calculate_total()
      self.assertIsNotNone(self.pool_table_test.total_cost)

unittest.main()
