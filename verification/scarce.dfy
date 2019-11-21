// This method takes in an array of tuples containing every blood type and their respective total 
// volume in the blood bank and loops through each tuple, returning only the blood types and their amounts
// who are lower than a provided limit.
// The method returns a sequence of tuples that fall below the given limit
method findScarce(a:seq<array<int>>, limit: int) returns (scarce: seq<array<int>>)
  // Pre-Conditions:
  //    - Array 'a' has at least 1 entry and is not empty
  //    - Every smaller array has length 2 (is a tuple)
  requires a != [] && |a| > 0;
  requires forall k :: 0 <= k < |a| ==> a[k] != null;
  requires forall k :: 0 <= k < |a| ==> a[k].Length == 2;

  // Post-Condition: 
  //    - Every entry that is below the given limit is recorded in 'scarce'
  //    - Every entry in 'scarce' is not null
  ensures forall k: int :: (0 <= k < |a| ==> ((a[k][1] <= limit) ==> a[k] in scarce));
  ensures forall k: int :: (0 <= k < |scarce| ==> (scarce[k] != null && scarce[k] in multiset(a[..])));
{
  var i : int := 0;
  scarce := [];
  while (i < |a|)
    invariant 0 <= i <= |a|;
    invariant forall k: int :: (0 <= k < i ==> ((a[k][1] <= limit) ==> a[k] in scarce));
    invariant forall k: int :: (0 <= k < |scarce| ==> (scarce[k] != null && scarce[k] in multiset(a[..])));
  {
    if (a[i][1] <= limit) 
    { 
      scarce := scarce + [a[i]];
    }
    i := i + 1;
  }
}

method Main() {

  var a1: array<int> := new int[2];
  a1[0], a1[1] := 0, 1000;
  var a2: array<int> := new int[2];
  a2[0], a2[1] := 1, 2000;
  var a3: array<int> := new int[2];
  a3[0], a3[1] := 2, 3000;
  var a4: array<int> := new int[2];
  a4[0], a4[1] := 3, 4000;
  var deposits: seq<array<int>> := [];
  deposits := deposits + [a1] + [a2] + [a3] + [a4];

  var i: seq<array<int>> := findScarce(deposits,3000);
  var j : int := 0;
  while (j < |i|) {
    var k : int := 0;
    while (k < i[j].Length) {
      print i[j][k];
      print ' ';
      k := k + 1;
    }
    print '\n';
    j := j + 1;
  }
}



