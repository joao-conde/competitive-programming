# Hash Code 2020 - Qualification Round

## Problem Description

The problem description can be found [here](https://storage.googleapis.com/coding-competitions.appspot.com/HC/2020/hashcode_2020_online_qualification_round.pdf) or together with the input files at hash code's [archive](https://codingcompetitions.withgoogle.com/hashcode/archive).

## Solution implemented

Assumes input files are named `a.txt`, `b.txt`, `c.txt`, `d.txt` and `e.txt` and inside ```input/```.

The idea was to **rate the libraries** by taking into account **signup time** and the **average score a library can process per day**. We assume the **average score** a library can process per day is the total score of the books it holds divided by the number of books (average score per book) times the number of books it is able to process per day, hence the average score a library can process per day. We obviously penalized for large signup times and encourage bigger average scores.

At the end we tried to normalize the values, because both "features" being used were of completely different scales and simply being summed, making one feature weight less then we thought of. Later analysis made us realize we were dumb and should had just divided both features, making the scales indifferent.

Then we define weights for both features, sort the libraries by scores and start printing books in order from each library. We keep track of books that were already printed so we skip them in the future.

## The team

I joined forces with:
- [@aquelemiguel](https://github.com/aquelemiguel)
- [@edramos-97](https://github.com/edramos-97)
- [@luisnmartins](https://github.com/luisnmartins)

## Ranking

[Global ranking #2837](https://codingcompetitions.withgoogle.com/hashcode/archive/2020)
