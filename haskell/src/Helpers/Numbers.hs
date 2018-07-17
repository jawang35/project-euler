module Helpers.Numbers
( isInteger
, properDivisors
, fibs
, isTriangular
, isPentagonal
) where

import Data.Fixed (mod')
import Data.List (nub)
import Data.List.Ordered (minus, union, unionAll)
import Data.Set (Set)
import qualified Data.Set as Set
import Math.NumberTheory.ArithmeticFunctions (divisors)
import Math.NumberTheory.UniqueFactorisation (UniqueFactorisation)

isInteger :: (RealFrac a) => a -> Bool
isInteger number =
    number == (fromIntegral $ round number)

properDivisors :: (UniqueFactorisation a, Ord a, Num a) => a -> Set a
properDivisors n = Set.delete n $ divisors n

fibs :: (Integral a) => [a]
fibs = 1:1:(zipWith (+) fibs $ tail fibs)

isTriangular :: (Integral a) => a -> Bool
isTriangular number =
    (-1 + (sqrt . fromIntegral $ 1 - (4 * (-2 * number)))) `mod'` 2 == 0

isPentagonal :: (Integral a) => a -> Bool
isPentagonal number =
    (1 + (sqrt . fromIntegral $ 1 - 4 * 3 * (-2) * number)) `mod'` 6 == 0
