## Input to Neural Network
[
    0, 1, 0,     # This is the danger state
    0, 0, 1, 0,  # Current direction
    0, 1, 0, 1   # Food position
]


## Output from Neural Network
We will create an action that is a list with three values.

[1, 0, 0] -> Forward

[0, 1, 0] -> Right

[0, 0, 1] -> Left


What we will get from the neural network is something like this

[0.12376362, 0.583929, 0.081917]

Find the position of the largest value, in this case it is 1

        .
    <- .O.xxxxx
        .