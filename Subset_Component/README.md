# Hard - Problem solving (Advanced)

## Problem

You are given an array with 64-bit integers: d[0], d[1], ..., d[n-1].

BIT(x, i) = (x >> i) & 1, where is the i^{th} lower bit of x in binary form. If we regard every bit as a vertex of a
graph G, there is an undirected edge between vertices i and j if there is a value k such that BIT(d[k], i) == 1 && BIT(
d[k], j) == 1.

For every subset of the input array, how many connected-components are there in that graph?

A connected component in a graph is a set of nodes which are accessible to each other via a path of edges. There may be
multiple connected components in a graph.

## Example

In the real challenge, there will be 64 nodes associated with each integer in d represented as a 64 bit binary value.
For clarity, only 4 bits will be shown in the example but all 64 will be considered in the calculations.

    Decimal  Binary Edges   Node ends
    d[0] = 1   0001   0
    d[1] = 2   0010   0
    d[2] = 3   0011   1       0 and 1
    d[3] = 5   0101   1       0 and 2

Consider all subsets:

                 Edges
    Subset   Count  Nodes  Connected components
    {1}         0           64
    {2}         0           64
    {3}         1   0-1     63
    {5}         1   0-2     63
    {1,2}       0           64
    {1,3}       1   0-1     63
    {1,5}       1   0-2     63
    {2,3}       1   0-1     63
    {2,5}       1   0-2     63
    {3,5}       2   0-1-2   62
    {1,2,3}     1   0-1     63
    {1,2,5}     1   0-2     63
    {1,3,5}     2   0-1-2   62
    {2,3,5}     2   0-1-2   62
    {1,2,3,5}   2   0-1-2   62
    Sum                    944

The values 3 and 5 have 2 bits set, so they have 1 edge each. If a subset contains only a 3 or 5, there will be one
connected component with 2 nodes, and 62 components with 1 node for a total of 63.

If both 3 and 5 are in a subset, 1 component with nodes 0,1 and 2 is formed since node 0 is one end of each edge
described. The other 61 nodes are solitary, so there are 62 connected components total.

All other values have only 1 bit set, so they have no edges. They have 64 components with 1 node each.

## Function Description

Complete the findConnectedComponents function in the editor below.

findConnectedComponents has the following parameters:

int d[n]: an array of integers

#### Returns

int: the sum of the number of connected components for all subsets of d

#### Input Format

The first row contains the integer n, the size of d[].
The next row has n space-separated integers, d[i].

#### Constraints

1 <= n <= 20

0 <= d[i] <= 2^{63} - 1

### Sample Input

3
2 5 9

### Sample Output

504

### Explanation

There are 8 subset of {2,5,9}.

{}
=> We don't have any number in this subset => no edge in the graph => Every node is a component by itself => Number of
connected-components = 64.

{2}
=> The Binary Representation of 2 is 00000010. There is a bit at only one position. => So there is no edge in the graph,
every node is a connected-component by itself => Number of connected-components = 64.

{5}
=> The Binary Representation of 5 is 00000101. There is a bit at the 0th and 2nd position. => So there is an edge: (0,2)
in the graph => There is one component with a pair of nodes (0,2) in the graph. Apart from that, all remaining 62
vertices are indepenent components of one node each (1,3,4,5,6...63) => Number of connected-components = 63.

{9}
=> The Binary Representation of 9 is 00001001. => There is a 1-bit at the 0th and 3rd position in this binary
representation. => edge: (0, 3) in the graph => Number of components = 63

{2, 5}
=> This will contain the edge (0, 2) in the graph which will form one component
=> Other nodes are all independent components
=> Number of connected-component = 63

{2, 9}
=> This has edge (0,3) in the graph
=> Similar to examples above, this has 63 connected components

{5, 9}
=> This has edges (0, 2) and (0, 3) in the graph
=> Similar to examples above, this has 62 connected components

{2, 5, 9}
=> This has edges(0, 2) (0, 3) in the graph. All three vertices (0,2,3) make one component => Other 61 vertices are all
independent components
=> Number of connected-components = 62

S = 64 + 64 + 63 + 63 + 63 + 63 + 62 + 62 = 504

### URL

https://www.hackerrank.com/challenges/subset-component/

## Some explanation in proposed solution (Spoilers)

Number of connected components is the number of vertices if, in binary, there is no 1s or only one 1. In other words,
when there is no edge.

Else, it is the number of vertices - (number of 1s in binary - 1).

(number of 1s - 1) because it is the number of edges ONLY for the outline/contour, without closing.

```
Example: 15 (in binary 1111) has (number of vertices - 3) components (61).
Edges:
  (0,1), (0,2), (0,3),
         (1,2), (1,3),
                (2,3).
However, there are edges that are not impacting the connected components, as they were connected before adding it.
Thus, the only important edges are the ones of the outline/contour. Thus:
Outline edges:
  (0,1), (1,2), (2,3), (3,0).
For example. However, the "closing edge", that is the last one, isn't impacting the connected components.
Thus, we can remove it.
Outline edges without closing:
  (0,1), (1,2), (2,3).
We can see there are as many outline edges without closing as (number of 1s in binary - 1).
And for each one of this outline edges without closing, two components are being connected to one component.
```

For a subset of several numbers, same discussion as before, but now the binary representation is the OR of all the
binary reprs.,
except the representations with only one 1 (again, no edges, but with OR can create a new undesirable edge).

```
Example:
  {2,5} should give the same components as {5}; as 2 in binary doesn't have any edges.
  However, if we do 2 OR 5, we get 7. And {7} and {5} have different amount of components.
  Thus, we need to remove cases with zero 1s or one 1 before doing OR.
```

It is the OR of all numbers in binary because it is the number of edges ONLY for the outline. If they were
separated, they are together due to definition of the problem, so no need to subtract any more 1s. If
they touch, it's again simply calculating the number of edges of the outline/contour (without closing).

       Example:
            {3,21}.
              3 -> (0,1). Components: 64 - 1 = 63. (Two 1s in binary).
              21 -> (0,2), (2,4), (0,4). For components, last one didn't matter. So, without closing,
                    (0,2), (2,4). Components: 64 - 2 = 62. (Three 1s in binary).
              [3,21] can be seen as -> (0,1), (0,2), (2,4). (3 | 21 = 25. Four 1s in binary).
                                     Components: 64 - 3 = 61.
            
       Another example:
            {Upwards triangle, downwards triangle}.
              Joint: They touch only in one point (height point of each).
              Connected components: Calculate the edges of the outline of the joint is the same as calculating the edges
              of the outline of the uppercase greek letter Sigma. And we can get Sigma representation calculating the
              OR of the triangles.