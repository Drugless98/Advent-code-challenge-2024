b'\n\n\n\n

# [Advent of Code](/)

  * [[About]](/2024/about)
  * [[Events]](/2024/events)
  * [[Shop]](https://cottonbureau.com/people/advent-of-code)
  * [[Settings]](/2024/settings)
  * [[Log Out]](/2024/auth/logout)

Andreas Mads N\xc3\xb8hr 17*

#    0x0000|[2024](/2024)

  * [[Calendar]](/2024)
  * [[AoC++]](/2024/support)
  * [[Sponsors]](/2024/sponsors)
  * [[Leaderboard]](/2024/leaderboard)
  * [[Stats]](/2024/stats)

\n\n

\n

Our [sponsors](/2024/sponsors) help make Advent of Code possible:

[Boot.dev](/2024/sponsors/redirect?url=https%3A%2F%2Fwww%2Eboot%2Edev%3Fpromo%3DADVENTOFCODE)
\- Do Adventers-of-Code make the best backend devs? We think so! If you want
to master backend development in Python, SQL, and Go, then try our hands-on
courses on Boot.dev! Get 25% off first payment w/promo ADVENTOFCODE

\n

\n\n\n

## \--- Day 1: Historian Hysteria ---

The _Chief Historian_ is always present for the big Christmas sleigh launch,
but nobody has seen him in months! Last anyone heard, he was visiting
locations that are historically significant to the North Pole; a group of
Senior Historians has asked you to accompany them as they check the places
they think he was most likely to visit.

\n

As each location is checked, they will mark it on their list with a _star_.
They figure the Chief Historian _must_ be in one of the first fifty places
they\'ll look, so in order to save Christmas, you need to help them get _fifty
stars_ on their list before Santa takes off on December 25th.

\n

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants _one star_. Good luck!

\n

You haven\'t even left yet and the group of Elvish Senior Historians has
already hit a problem: their list of locations to check is currently _empty_.
Eventually, someone decides that the best place to check first would be the
Chief Historian\'s office.

\n

Upon pouring into the office, everyone confirms that the Chief Historian is
indeed nowhere to be found. Instead, the Elves discover an assortment of notes
and lists of historically significant locations! This seems to be the planning
the Chief Historian was doing before he left. Perhaps these notes can be used
to determine which locations to search?

\n

Throughout the Chief\'s office, the historically significant locations are
listed not by name but by a unique number called the _location ID_. To make
sure they don\'t miss anything, The Historians split into two groups, each
searching the office and trying to create their own complete list of location
IDs.

\n

There\'s just one problem: by holding the two lists up _side by side_ (your
puzzle input), it quickly becomes clear that the lists aren\'t very similar.
Maybe you can help The Historians reconcile their lists?

\n

For example:

\n

    
    
    3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n

\n

Maybe the lists are only off by a small amount! To find out, pair up the
numbers and measure how far apart they are. Pair up the _smallest number in
the left list_ with the _smallest number in the right list_ , then the
_second-smallest left number_ with the _second-smallest right number_ , and so
on.

\n

Within each pair, figure out _how far apart_ the two numbers are; you\'ll need
to _add up all of those distances_. For example, if you pair up a `3` from the
left list with a `7` from the right list, the distance apart is `4`; if you
pair up a `9` with a `3`, the distance apart is `6`.

\n

In the example list above, the pairs and distances would be as follows:

\n

\n

  * The smallest number in the left list is `1`, and the smallest number in the right list is `3`. The distance between them is `_2_`.
\n

  * The second-smallest number in the left list is `2`, and the second-smallest number in the right list is another `3`. The distance between them is `_1_`.
\n

  * The third-smallest number in both lists is `3`, so the distance between them is `_0_`.
\n

  * The next numbers to pair up are `3` and `4`, a distance of `_1_`.
\n

  * The fifth-smallest numbers in each list are `3` and `5`, a distance of `_2_`.
\n

  * Finally, the largest number in the left list is `4`, while the largest number in the right list is `9`; these are a distance `_5_` apart.
\n

\n

To find the _total distance_ between the left list and the right list, add up
the distances between all of the pairs you found. In the example above, this
is `2 + 1 + 0 + 1 + 2 + 5`, a total distance of `_11_`!

\n

Your actual left and right lists contain many location IDs. _What is the total
distance between your lists?_

\n\n

Your puzzle answer was `2580760`.

## \--- Part Two ---

Your analysis only confirmed what everyone feared: the two lists of location
IDs are indeed very different.

\n

Or are they?

\n

The Historians can\'t agree on which group made the mistakes _or_ how to read
most of the Chief\'s handwriting, but in the commotion you notice an
interesting detail: a lot of location IDs appear in both lists! Maybe the
other numbers aren\'t location IDs at all but rather misinterpreted
handwriting.

\n

This time, you\'ll need to figure out exactly how often each number from the
left list appears in the right list. Calculate a total _similarity score_ by
adding up each number in the left list after multiplying it by the number of
times that number appears in the right list.

\n

Here are the same example lists again:

\n

    
    
    3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n

\n

For these example lists, here is the process of finding the similarity score:

\n

\n

  * The first number in the left list is `3`. It appears in the right list three times, so the similarity score increases by `3 * 3 = _9_`.
\n

  * The second number in the left list is `4`. It appears in the right list once, so the similarity score increases by `4 * 1 = _4_`.
\n

  * The third number in the left list is `2`. It does not appear in the right list, so the similarity score does not increase (`2 * 0 = 0`).
\n

  * The fourth number, `1`, also does not appear in the right list.
\n

  * The fifth number, `3`, appears in the right list three times; the similarity score increases by `_9_`.
\n

  * The last number, `3`, appears in the right list three times; the similarity score again increases by `_9_`.
\n

\n

So, for these example lists, the similarity score at the end of this process
is `_31_` (`9 + 4 + 0 + 0 + 9 + 9`).

\n

Once again consider your left and right lists. _What is their similarity
score?_

\n\n

Your puzzle answer was `25358365`.

Both parts of this puzzle are complete! They provide two gold stars: **

\n

At this point, you should [return to your Advent calendar](/2024) and try
another puzzle.

\n

If you still want to see it, you can [get your puzzle input](1/input).

\n

You can also [Shareon\n
[Bluesky](https://bsky.app/intent/compose?text=I%27ve+completed+%22Historian+Hysteria%22+%2D+Day+1+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F1)\n
[Twitter](https://twitter.com/intent/tweet?text=I%27ve+completed+%22Historian+Hysteria%22+%2D+Day+1+%2D+Advent+of+Code+2024&url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F1&related=ericwastl&hashtags=AdventOfCode)\n
[Mastodon] this puzzle.\n\n\n\n\n\n\n'

