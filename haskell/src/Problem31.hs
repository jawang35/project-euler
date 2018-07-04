{- |
Problem 31 - Coin Sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
-}

module Problem31
( answer
, coinCombinations
) where

import Helpers.Runtime (printAnswerAndElapsedTime)

coinCombinations :: [Int] -> Int -> [[Int]]
coinCombinations _ 0          = [[]]
coinCombinations coins amount =
    concat $ map (\c -> zipWith (:) (repeat c) (remainingCoinCombinations c)) usableCoins
    where usableCoins                 = filter (<= amount) coins
          remainingCoinCombinations c = coinCombinations (filter (<= c) coins) (amount - c)

answer :: Int
answer = length $ coinCombinations [1, 2, 5, 10, 20, 50, 100, 200] 200

main = printAnswerAndElapsedTime answer
