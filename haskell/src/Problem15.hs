{- |
Problem 15 - Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
-}

module Problem15
( answer
, latticePaths
) where

import Helpers.Runtime (printAnswerAndElapsedTime)

memoize :: (Int -> a) -> (Int -> a)
memoize f = (map f [0..] !!)

latticePaths :: Int -> Int -> Int
latticePaths = memoize latticePaths'
    where
        latticePaths' 0 = \_ -> 1
        latticePaths' x = memoize $ latticePaths'' x
            where
                latticePaths'' _ 0 = 1
                latticePaths'' x y = latticePaths (x - 1) y + latticePaths x (y - 1)

answer = latticePaths 20 20

main = printAnswerAndElapsedTime answer
