{- |
Problem 39 - Integer Right Triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
-}

module Problem39
( answer
, rightTriangles
) where

import Data.List (maximumBy)
import Helpers.Runtime (printAnswerAndElapsedTime)

rightTriangles :: Int -> [(Int, Int, Int)]
rightTriangles perimeter =
    filter (\(a, b, c) -> a^2 + b^2 == c^2 && a <= b) $ map triple $ take (perimeter `div` 3) [1..]
    where
        triple a =
            let b = (perimeter^2 - 2 * perimeter * a) `div` (2 * perimeter - 2 * a)
            in (a, b, perimeter - a - b)

answer :: Int
answer =
    fst $ maximumBy (\(_, x) (_, y) -> compare x y)
        $ zip [1..]
        $ map (length . rightTriangles) [1..1000]

main = printAnswerAndElapsedTime answer
