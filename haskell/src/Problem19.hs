{- |
Problem 19 - Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
- April, June and November.
- All the rest have thirty-one,
- Saving February alone,
- Which has twenty-eight, rain or shine.
- And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
-}

module Problem19
( answer
) where

import Data.Time.Calendar (Day, fromGregorian, toGregorian)
import Data.Time.Calendar.WeekDate (toWeekDate)
import Helpers.Runtime (printAnswerAndElapsedTime)

isFirstOfMonth :: Day -> Bool
isFirstOfMonth day = dayOfMonth == 1
    where (_, _, dayOfMonth) = toGregorian day

isSunday :: Day -> Bool
isSunday day = dayOfWeek == 7
    where (_, _, dayOfWeek) = toWeekDate day

firstSundays :: [Day] -> Int
firstSundays = length . filter (\d -> isSunday d && isFirstOfMonth d)

answer :: Int
answer = firstSundays [start..end]
    where start = fromGregorian 1901 1 1
          end   = fromGregorian 2000 12 31

main = printAnswerAndElapsedTime answer
