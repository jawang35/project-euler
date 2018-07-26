module Helpers.Runtime
( printAnswerAndElapsedTime
) where

import Control.Exception (evaluate)
import System.CPUTime (getCPUTime)
import Text.Printf (printf)

printAnswerAndElapsedTime :: (Show a) => a -> IO ()
printAnswerAndElapsedTime answer = do
    start <- getCPUTime
    value <- evaluate answer
    end <- getCPUTime
    printf "Answer: %s\n" $ show value
    printf "Elapsed time: %fms\n" $ fromIntegral (end - start) / (10 ^ 9)
