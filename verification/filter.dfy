// This method interprets the record of blood deposits as an list of arrays
// We denote the list representing the record of deposits as 'a' whose entries are smaller arrays
// We note that these smaller arrays represent each individual entry 
// The method returns a sequence of deposit entries matching the conditions required
method filter(a:seq<array<int>>, attribute: int, value: int) returns (filtered: seq<array<int>>)
  // Pre-Conditions:
  //    - Array (a) has at least 1 entry and is not empty
  //    - Every blood deposit (smaller array) has length 5
  //    - The attribute index falls within the bounds of the smaller array
  requires a != [] && |a| > 0;
  requires forall k :: 0 <= k < |a| ==> a[k] != null && a[k].Length == 5;
  requires 0 <= attribute < 5;

  // Post-Condition: 
  //    - Every entry that matches the given value at the given attribute is recorded in 'filtered'
  //    - Every entry in filtered is not null and is of length 5
  //    - Every entry in filtered came from the original array of deposits
  ensures forall k: int :: (0 <= k < |a| ==> ((a[k][attribute] == value) ==> a[k] in filtered));
  ensures forall k: int :: (0 <= k < |filtered| ==> (filtered[k] != null && filtered[k].Length == 5));
  ensures forall k: int :: (0 <= k < |filtered| ==> filtered[k] in multiset(a[..]));
{
  var i : int := 0;
  filtered := [];
  while (i < |a|)
    invariant 0 <= i <= |a|;
    invariant forall k: int :: (0 <= k < i ==> ((a[k][attribute] == value) ==> a[k] in filtered));
    invariant forall k: int :: (0 <= k < |filtered| ==> (filtered[k] != null && filtered[k].Length == 5));
    invariant forall k: int :: (0 <= k < |filtered| ==> filtered[k] in multiset(a[..]));
  {
    if (a[i][attribute] == value) 
    { 
      filtered := filtered + [a[i]];
    }
    i := i + 1;
  }
}

method Main() {

  var a1: array<int> := new int[5];
  a1[0], a1[1], a1[2], a1[3], a1[4] := 0, 10, 20, 30, 40;
  var a2: array<int> := new int[5];
  a2[0], a2[1], a2[2], a2[3], a2[4] := 1, 11, 23, 31, 41;
  var a3: array<int> := new int[5];
  a3[0], a3[1], a3[2], a3[3], a3[4] := 2, 11, 22, 32, 42;
  var a4: array<int> := new int[5];
  a4[0], a4[1], a4[2], a4[3], a4[4] := 3, 11, 23, 33, 43;
  var deposits: seq<array<int>> := [];
  deposits := deposits + [a1] + [a2] + [a3] + [a4];

  var i: seq<array<int>> := filter(deposits,1,11);
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
