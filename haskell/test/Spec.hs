import Test.HUnit
import Problem1
import Problem2
import Problem3
import Problem4
import Problem6

problem1 = TestCase $ assertEqual "Answer" 233168 Problem1.answer
problem2 = TestCase $ assertEqual "Answer" 4613732 Problem2.answer
problem3 = TestCase $ assertEqual "Answer" 6857 Problem3.answer
problem4 = TestCase $ assertEqual "Answer" 906609 Problem4.answer
problem6 = TestCase $ assertEqual "Answer" 25164150 Problem6.answer

tests = TestList
    [ TestLabel "Problem1" problem1
    , TestLabel "Problem2" problem2
    , TestLabel "Problem3" problem3
    , TestLabel "Problem4" problem4
    , TestLabel "Problem6" problem6
    ]

main :: IO Counts
main = runTestTT tests
