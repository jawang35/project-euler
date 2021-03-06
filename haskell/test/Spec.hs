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
import Problem10
import Problem11
import Problem12
import Problem13
import Problem14
import Problem15
import Problem16
import Problem17
import Problem18
import Problem19
import Problem20
import Problem21
import Problem22
import Problem23
import Problem24
import Problem25
import Problem26
import Problem27
import Problem28
import Problem29
import Problem30
import Problem31
import Problem32
import Problem33
import Problem34
import Problem35
import Problem36
import Problem37
import Problem38
import Problem39
import Problem40
import Problem41
import Problem42
import Problem43
import Problem44
import Problem45
import Problem46
import Problem47
import Problem48
import Problem49
import Problem50
import Problem52
import Problem53
import Problem54
import Problem55
import Problem56
import Problem57
import Problem58
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
problem10 = TestCase $ assertEqual "Answer" 142913828922 Problem10.answer
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
problem19 = TestCase $ assertEqual "Answer" 171 Problem19.answer
problem20 = TestCase $ assertEqual "Answer" 648 Problem20.answer
problem21 = TestCase $ assertEqual "Answer" 31626 Problem21.answer
problem22 = TestCase (do answer <- Problem22.answer
                         assertEqual "Answer" 871198282 answer)
problem23 = TestCase $ assertEqual "Answer" 4179871 Problem23.answer
problem24 = TestCase $ assertEqual "Answer" 2783915460 Problem24.answer
problem25 = TestCase $ assertEqual "Answer" 4782 Problem25.answer
problem26 = TestCase $ assertEqual "Answer" 983 Problem26.answer
problem27 = TestCase $ assertEqual "Answer" (-59231) Problem27.answer
problem28 = TestCase $ assertEqual "Answer" 669171001 Problem28.answer
problem29 = TestCase $ assertEqual "Answer" 9183 Problem29.answer
problem30 = TestCase $ assertEqual "Answer" 443839 Problem30.answer
problem31 = TestCase $ assertEqual "Answer" 73682 Problem31.answer
problem32 = TestCase $ assertEqual "Answer" 45228 Problem32.answer
problem33 = TestCase $ assertEqual "Answer" 100 Problem33.answer
problem34 = TestCase $ assertEqual "Answer" 40730 Problem34.answer
problem35 = TestCase $ assertEqual "Answer" 55 Problem35.answer
problem36 = TestCase $ assertEqual "Answer" 872187 Problem36.answer
problem37 = TestCase $ assertEqual "Answer" 748317 Problem37.answer
problem38 = TestCase $ assertEqual "Answer" 932718654 Problem38.answer
problem39 = TestCase $ assertEqual "Answer" 840 Problem39.answer
problem40 = TestCase $ assertEqual "Answer" 210 Problem40.answer
problem41 = TestCase $ assertEqual "Answer" 7652413 Problem41.answer
problem42 = TestCase (do answer <- Problem42.answer
                         assertEqual "Answer" 162 answer)
problem43 = TestCase $ assertEqual "Answer" 16695334890 Problem43.answer
problem44 = TestCase $ assertEqual "Answer" 5482660 Problem44.answer
problem45 = TestCase $ assertEqual "Answer" 1533776805 Problem45.answer
problem46 = TestCase $ assertEqual "Answer" 5777 Problem46.answer
problem47 = TestCase $ assertEqual "Answer" 134043 Problem47.answer
problem48 = TestCase $ assertEqual "Answer" 9110846700 Problem48.answer
problem49 = TestCase $ assertEqual "Answer" 296962999629 Problem49.answer
problem50 = TestCase $ assertEqual "Answer" 997651 Problem50.answer
problem52 = TestCase $ assertEqual "Answer" 142857 Problem52.answer
problem53 = TestCase $ assertEqual "Answer" 4075 Problem53.answer
problem54 = TestCase (do answer <- Problem54.answer
                         assertEqual "Answer" 376 answer)
problem55 = TestCase $ assertEqual "Answer" 249 Problem55.answer
problem56 = TestCase $ assertEqual "Answer" 972 Problem56.answer
problem57 = TestCase $ assertEqual "Answer" 153 Problem57.answer
problem58 = TestCase $ assertEqual "Answer" 26241 Problem58.answer
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
    , TestLabel "Problem 10" problem10
    , TestLabel "Problem 11" problem11
    , TestLabel "Problem 12" problem12
    , TestLabel "Problem 13" problem13
    , TestLabel "Problem 14" problem14
    , TestLabel "Problem 15" problem15
    , TestLabel "Problem 16" problem16
    , TestLabel "Problem 17" problem17
    , TestLabel "Problem 18" problem18
    , TestLabel "Problem 19" problem19
    , TestLabel "Problem 20" problem20
    , TestLabel "Problem 21" problem21
    , TestLabel "Problem 22" problem22
    , TestLabel "Problem 23" problem23
    , TestLabel "Problem 24" problem24
    , TestLabel "Problem 25" problem25
    , TestLabel "Problem 26" problem26
    , TestLabel "Problem 27" problem27
    , TestLabel "Problem 28" problem28
    , TestLabel "Problem 29" problem29
    , TestLabel "Problem 30" problem30
    , TestLabel "Problem 31" problem31
    , TestLabel "Problem 32" problem32
    , TestLabel "Problem 33" problem33
    , TestLabel "Problem 34" problem34
    , TestLabel "Problem 35" problem35
    , TestLabel "Problem 36" problem36
    , TestLabel "Problem 37" problem37
    , TestLabel "Problem 38" problem38
    , TestLabel "Problem 39" problem39
    , TestLabel "Problem 40" problem40
    , TestLabel "Problem 41" problem41
    , TestLabel "Problem 42" problem42
    , TestLabel "Problem 43" problem43
    , TestLabel "Problem 44" problem44
    , TestLabel "Problem 45" problem45
    , TestLabel "Problem 46" problem46
    , TestLabel "Problem 47" problem47
    , TestLabel "Problem 48" problem48
    , TestLabel "Problem 49" problem49
    , TestLabel "Problem 50" problem50
    , TestLabel "Problem 52" problem52
    , TestLabel "Problem 53" problem53
    , TestLabel "Problem 54" problem54
    , TestLabel "Problem 55" problem55
    , TestLabel "Problem 56" problem56
    , TestLabel "Problem 57" problem57
    , TestLabel "Problem 58" problem58
    , TestLabel "Problem 67" problem67
    ]

main :: IO Counts
main = do
    counts <- runTestTT tests
    if (errors counts) + (failures counts) > 0
        then error "Test errors or failures found!"
        else putStrLn "All tests passed!"
    return counts
