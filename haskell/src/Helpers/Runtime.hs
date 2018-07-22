module Helpers.Runtime
( printAnswerAndElapsedTime
) where

import Control.Exception
import System.CPUTime
import Text.Printf

printAnswerAndElapsedTime :: (Show a) => a -> IO ()
printAnswerAndElapsedTime a = do
    start <- getCPUTime
    value <- evaluate a
    end <- getCPUTime
    let elapsed = fromIntegral (end - start) / (10^9)
    printf "Answer: %s\n" (show value)
    printf "Elapsed time: %fms\n" (elapsed :: Double)
