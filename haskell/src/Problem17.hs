{- |
Problem 17 - Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
-}

module Problem17
( answer
, numberLetterCount
) where

import qualified Data.Map as Map
import Helpers.Runtime (printAnswerAndElapsedTime)

ones = Map.fromList
    [ ("1", 3) -- one
    , ("2", 3) -- two
    , ("3", 5) -- three
    , ("4", 4) -- four
    , ("5", 4) -- five
    , ("6", 3) -- six
    , ("7", 5) -- seven
    , ("8", 5) -- eight
    , ("9", 4) -- nine
    ]

tens = Map.fromList
    [ ("1", 3) -- ten
    , ("2", 6) -- twenty
    , ("3", 6) -- thirty
    , ("4", 5) -- forty
    , ("5", 5) -- fifty
    , ("6", 5) -- sixty
    , ("7", 7) -- seventy
    , ("8", 6) -- eighty
    , ("9", 6) -- ninety
    ]

teens = Map.fromList
    [ ("11", 6) -- eleven
    , ("12", 6) -- twelve
    , ("13", 8) -- thirteen
    , ("14", 8) -- fourteen
    , ("15", 7) -- fifteen
    , ("16", 7) -- sixteen
    , ("17", 9) -- seventeen
    , ("18", 8) -- eighteen
    , ("19", 8) -- nineteen
    ]

numberLetterCount :: Int -> Int
numberLetterCount n
    | n > 999   = ones Map.! (take 1 (show n)) + 8 + (let rest = n `mod` 1000 in (if 0 < rest && rest < 100 then 3 + numberLetterCount rest else numberLetterCount rest))
    | n > 99    = ones Map.! (take 1 (show n)) + 7 + (let rest = n `mod` 100 in (if rest > 0 then 3 + numberLetterCount rest else 0))
    | n > 19    = tens Map.! (take 1 (show n)) + (numberLetterCount $ n `mod` 10)
    | n > 10    = teens Map.! (show n)
    | n == 10   = tens Map.! "1"
    | n > 0     = ones Map.! (show n)
    | otherwise = 0

answer :: Int
answer = sum $ map numberLetterCount [1..1000]

main = printAnswerAndElapsedTime answer
