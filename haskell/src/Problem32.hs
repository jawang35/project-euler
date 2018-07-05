{- |
Problem 32 - Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
-}

module Problem32
( answer
, pandigitalProducts
) where

import Data.Char (intToDigit)
import Data.List (nubBy, permutations)
import qualified Data.Set as Set
import Helpers.Runtime (printAnswerAndElapsedTime)

digitsToInt :: [Int] -> Int
digitsToInt = read . map intToDigit

insertOperator :: Int -> [Int] -> [([Int], [Int])]
insertOperator rightPosition digits =
    map (flip splitAt digits) positions
    where positions = take (length digits - rightPosition) [1..]

productIdentities :: [Int] -> [(Int, Int, Int)]
productIdentities digits =
    concat $ zipWith3 (\mr md p -> zip3 (repeat mr) md p) multipliers multiplicands products
    where multiplierSplit = insertOperator 7 digits
          equalSplit      = map ((insertOperator 4) . snd) multiplierSplit
          multipliers     = map (digitsToInt . fst) multiplierSplit
          multiplicands   = map (map $ digitsToInt . fst) equalSplit
          products        = map (map $ digitsToInt . snd) equalSplit

validProduct :: (Int, Int, Int) -> Bool
validProduct (mr, md, p) = mr * md == p

pandigitalProducts :: [(Int, Int, Int)]
pandigitalProducts =
    nubBy (\(_, _, p1) (_, _, p2) -> p1 == p2)
        $ filter validProduct
        $ concat
        $ map productIdentities
        $ permutations [1..9]

answer :: Int
answer = sum $ map (\(_, _, p) -> p) pandigitalProducts

main = printAnswerAndElapsedTime answer
