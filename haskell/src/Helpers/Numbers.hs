module Helpers.Numbers
( isPrime
, primeDivisors
) where

isPrime :: (Integral a) => a -> Bool
isPrime 2 = True
isPrime number
    | number < 2 = False
    | otherwise = not $ any (\n -> number `mod` n == 0) [2..maxFactor]
    where maxFactor = 1 + (floor $ sqrt $ fromIntegral number)

primeDivisors :: (Integral a) => a -> [a]
primeDivisors number =
    case factors of
        [] -> [number]
        _ -> factors ++ (primeDivisors $ quot number $ head factors)
    where maxFactor = 1 + (floor $ sqrt $ fromIntegral number)
          factors = take 1 $ filter (\n -> number `mod` n == 0) [2..maxFactor]
