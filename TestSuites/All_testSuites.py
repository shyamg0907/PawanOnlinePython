import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_signupTest import signupTest
from Package2.TC_PaymentTest import paymentTest
from Package2.TC_PaymentReturnTest import PaymentReturnTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(signupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

sanityTestSuite=unittest.TestSuite([tc1,tc2])
functionalTetstSuite=unittest.TestSuite([tc3,tc4])
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)