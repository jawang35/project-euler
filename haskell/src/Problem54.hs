{- |
Problem 54 - Poker Hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
-}

module Problem54
( answer
) where

import System.IO (readFile)
import Data.Function (on)
import Data.List (group, nub, sort, sortBy)
import Config (assetsPath)
import Helpers.Runtime (printAnswerAndElapsedTime)

data Value =
    Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King | Ace
    deriving (Enum, Eq, Ord, Show)

parseValue :: String -> Value
parseValue value =
    case value of
        "2" -> Two
        "3" -> Three
        "4" -> Four
        "5" -> Five
        "6" -> Six
        "7" -> Seven
        "8" -> Eight
        "9" -> Nine
        "T" -> Ten
        "J" -> Jack
        "Q" -> Queen
        "K" -> King
        "A" -> Ace

data Suit =
    Club | Diamond | Heart | Spade
    deriving (Eq, Show)

parseSuit :: String -> Suit
parseSuit suit =
    case suit of
        "C" -> Club
        "D" -> Diamond
        "H" -> Heart
        "S" -> Spade

data Card =
    Card { value :: Value
         , suit :: Suit
         }
    deriving (Show)

instance Eq Card where
    (==) = (==) `on` value

instance Ord Card where
    compare x y = compare (value x) (value y)

parseCard :: String -> Card
parseCard card =
    Card { value = parseValue value
         , suit = parseSuit suit
         }
    where (value, suit) = splitAt 1 card

data Hand = HighCard [Value]
          | Pair Value [Value]
          | TwoPair Value Value Value
          | ThreeOfAKind Value
          | Straight [Value]
          | Flush [Value]
          | FullHouse Value
          | FourOfAKind Value
          | StraightFlush [Value]
          deriving (Eq, Ord, Show)

parseHand :: [Card] -> Hand
parseHand cards
    | isStraight && isFlush = StraightFlush $ concat valueGroups
    | isFlush               = Flush $ concat valueGroups
    | isStraight            = Straight $ concat valueGroups
    | groupCount == 2       = if length (head valueGroups) == 4
                              then FourOfAKind $ head $ head valueGroups
                              else FullHouse $ head $ head valueGroups
    | groupCount == 3       = if length (head valueGroups) == 3
                              then ThreeOfAKind $ head $ head valueGroups
                              else TwoPair (head $ head valueGroups) (head $ valueGroups !! 1) (head $ last valueGroups)
    | groupCount == 4       = Pair (head $ head valueGroups) (concat $ tail valueGroups)
    | otherwise             = HighCard $ concat valueGroups
    where valueGroups = sortBy (flip (\x y -> compare (length x, head x) (length y, head y))) . group . sort $ map value cards
          groupCount  = length valueGroups
          isStraight  = let values = concat valueGroups in
                        values == [Ace, Five, Four, Three, Two] || values == reverse [(minimum values)..(maximum values)]
          isFlush     = let suits = map suit cards in
                        length (nub suits) == 1

answer :: IO Int
answer = do
    contents <- readFile $ assetsPath ++ "/problem54/poker.txt"
    let handsPlayed = map (splitAt 5 . map parseCard . words) $ lines contents
    return $ length $ filter (\(x, y) -> parseHand x > parseHand y) handsPlayed

main = do
    value <- answer
    printAnswerAndElapsedTime value
