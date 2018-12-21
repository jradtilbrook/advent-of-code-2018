import Data.List
import Data.Maybe

-- calculated manually, then length of each string
idSize = 26

{-
 - read all lines from stdin
 - sort them with Data.List.sort
 - iterate over them, using the head and 2nd to compare difference
 -}
-- main = interact (unlines . id . lines)
main = do
    all <- getContents
    let all2 = lines all
    print $ g all2


-- what letters are common between the two strings that only differ by one character?
f :: String -> String -> String
f [] [] = []
f (x:xs) (y:ys) = if x == y then [x] ++ f xs ys else f xs ys

-- takes all lines of input, runs it through f to find the string that is idSize - 1 long
g :: [String] -> String
g [] = []
g (x:[]) = x
-- this feels like a poor implementation but hopefully ill get better
g (x:xs) = if isJust found then fromJust found else g xs
    where
        found = find (\a -> length a == idSize - 1) $ m xs
        m = map (f x)
        common = f x $ head xs
