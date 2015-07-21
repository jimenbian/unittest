# -*- coding: UTF-8 -*-
'''
Created on 2015年7月21日

@author: aohai.lb
'''
import TestClass
import unittest

class test(unittest.TestCase):
    ## 初始化
    def setUp(self):
        self.myclass=TestClass.TestClass()
        pass
    
    def testsum(self):
        ##如果sum函数输出错误，系那是test sum fail
        self.assertEqual(self.myclass.sum(1,2),3,'test sum fail')
    
    def testsub(self):
        self.assertEqual(self.myclass.sub(),8,'test sub fail ')
        
    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()
        