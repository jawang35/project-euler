import Control.Exception
import Test.HUnit
import Problem1
import Problem2
import Problem3
import Problem4
import Problem6
import Problem7
import Problem8
import Problem9
import Problem11
import Problem12
import Problem13
import Problem14
import Problem15
import Problem16
import Problem17
import Problem18
import Problem67

problem1 = TestCase $ assertEqual "Answer" 233168 Problem1.answer
problem2 = TestCase $ assertEqual "Answer" 4613732 Problem2.answer
problem3 = TestCase $ assertEqual "Answer" 6857 Problem3.answer
problem4 = TestCase $ assertEqual "Answer" 906609 Problem4.answer
problem6 = TestCase $ assertEqual "Answer" 25164150 Problem6.answer
problem7 = TestCase $ assertEqual "Answer" 104743 Problem7.answer
problem8 = TestCase (do answer <- Problem8.answer
                        assertEqual "Answer" 23514624000 answer)
problem9 = TestCase $ assertEqual "Answer" 31875000 Problem9.answer
problem11 = TestCase (do answer <- Problem11.answer
                         assertEqual "Answer" 70600674 answer)
problem12 = TestCase $ assertEqual "Answer" 76576500 Problem12.answer
problem13 = TestCase (do answer <- Problem13.answer
                         assertEqual "Answer" 5537376230 answer)
problem14 = TestCase $ assertEqual "Answer" 837799 Problem14.answer
problem15 = TestCase $ assertEqual "Answer" 137846528820 Problem15.answer
problem16 = TestCase $ assertEqual "Answer" 1366 Problem16.answer
problem17 = TestCase $ assertEqual "Answer" 21124 Problem17.answer
problem18 = TestCase (do answer <- Problem18.answer
                         assertEqual "Answer" 1074 answer)
problem67 = TestCase (do answer <- Problem67.answer
                         assertEqual "Answer" 7273 answer)

tests = TestList
    [ TestLabel "Problem 1" problem1
    , TestLabel "Problem 2" problem2
    , TestLabel "Problem 3" problem3
    , TestLabel "Problem 4" problem4
    , TestLabel "Problem 6" problem6
    , TestLabel "Problem 7" problem7
    , TestLabel "Problem 8" problem8
    , TestLabel "Problem 9" problem9
    , TestLabel "Problem 11" problem11
    , TestLabel "Problem 12" problem12
    , TestLabel "Problem 13" problem13
    , TestLabel "Problem 14" problem14
    , TestLabel "Problem 15" problem15
    , TestLabel "Problem 16" problem16
    , TestLabel "Problem 17" problem17
    , TestLabel "Problem 18" problem18
    , TestLabel "Problem 67" problem67
    ]

main :: IO Counts
main = do
    counts <- runTestTT tests
    if (errors counts) + (failures counts) > 0
        then error "Test errors or failures found!"
        else putStrLn "All tests passed!"
    return counts
