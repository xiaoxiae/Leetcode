import qualified Data.Map as Map

main :: IO ()
main = do
    putStr $ show (recursive Map.empty [1, 2, 3] 4 0)

fromJust :: Maybe a -> a
fromJust (Just x) = x
fromJust Nothing  = error "This should not have happened."

recursive :: (Num b, Ord b) => Map.Map b b -> [b] -> b -> b -> (b, b)
resursive _ [] _ _       = (-1, -1)
recursive dic (x:xs) t d
  | Map.member (t - x) dic = (fromJust (Map.lookup (t - x) dic), d)
  | otherwise              = recursive (Map.insert x d dic) xs t (d + 1)
