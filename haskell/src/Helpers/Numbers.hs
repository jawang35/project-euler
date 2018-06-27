module Helpers.Numbers
( isPrime
, primeDivisors
, divisors
, properDivisors
, fibs
) where

import Data.List (nub)

isPrime :: (Integral a) => a -> Bool
isPrime 2 = True
isPrime number
    | number < 2 = False
    | otherwise  = not $ any (\n -> number `mod` n == 0) [2..maxFactor]
    where maxFactor = 1 + (floor $ sqrt $ fromIntegral number)

primeDivisors :: (Integral a) => a -> [a]
primeDivisors number =
    case factors of
        [] -> [number]
        _ -> factors ++ (primeDivisors $ quot number $ head factors)
    where maxFactor = 1 + (floor $ sqrt $ fromIntegral number)
          factors   = take 1 $ filter (\n -> number `mod` n == 0) [2..maxFactor]

divisors :: (Integral a) => a -> [a]
divisors number = nub $ concat divisorPairs
    where range        = [1..(floor $ sqrt $ fromIntegral number)]
          isDivisor    = (==0) . (number `rem`)
          divisorPairs = map (\x -> [x, number `div` x]) $ filter isDivisor $ range

properDivisors :: (Integral a) => a -> [a]
properDivisors number = filter (\d -> d /= number) $ divisors number

fibs :: (Integral a) => [a]
fibs = 1:1:(zipWith (+) fibs $ tail fibs)
