{- |
Problem 22 - Name Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
-}

module Problem22
( answer
, nameScore
, totalNameScores
) where

import System.IO (readFile)
import Data.Char (ord)
import Data.List (sort)
import Data.List.Split (splitOn)
import Config (assetsPath)
import Helpers.Runtime (printAnswerAndElapsedTime)

scoreA :: Int
scoreA = ord 'A' - 1

letterScore :: Char -> Int
letterScore x = ord x - scoreA

nameScore :: String -> Int
nameScore = sum . map letterScore

totalNameScores :: [String] -> Int
totalNameScores = sum . zipWith (*) [1..] . map nameScore . sort

answer :: IO Int
answer = do
    contents <- readFile $ assetsPath ++ "/problem22/names.txt"
    let names = map (filter (/= '"')) $ splitOn "," contents
    return $ totalNameScores names

main = do
    value <- answer
    printAnswerAndElapsedTime value
