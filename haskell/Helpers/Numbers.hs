module Helpers.Numbers
( primeDivisors
) where

primeDivisors :: Integer -> [Integer]
primeDivisors number =
    case factors of
        [] -> [number]
        _ -> factors ++ (primeDivisors $ quot number $ head factors)
    where maximum = 1 + (floor $ sqrt $ fromIntegral number)
          factors = take 1 $ filter (\n -> number `mod` n == 0) [2..maximum]
