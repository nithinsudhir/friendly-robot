// This recursive function partially verifies the sum of a sequence of arrays at the last value
function partialSum( a:seq<array<int>>, n:int ) : int
  // Pre-Conditions:
  //    - Sequence 'a' is not null and each entry contains the volume at the last index (index 4)
  requires 0 <= n <= |a|;
  requires forall k :: 0 <= k < |a| ==> a[k] != null && a[k].Length == 5;
  decreases n;
  reads a;
{
  if (n == 0) then 0 else partialSum(a, n-1) + a[n-1][4]
}

// This method compute the sum volume for a sequence of blood deposit entries
method sum_volume( a:seq<array<int>> ) returns (sum: int)
  // Pre-Conditions:
  //    - Sequence 'a' is not null and each entry contains the volume at the last index (index 4)
  requires forall k :: 0 <= k < |a| ==> a[k] != null && a[k].Length == 5;
  // Post-Conditions:
  //    - sum is equal to the partial sum of the entire sequency of arrays
  ensures sum == partialSum(a, |a|);
{
  var i := 0;
  sum := 0;
  while (i < |a|)
    invariant 0 <= i <= |a|;
    invariant sum == partialSum(a, i);
    decreases |a| - i;
  {
    sum := sum + a[i][4];
    i := i + 1;
  }
}

// The filter method is verified in 'filter.dy' and is used in the count_volume function aswell
method filter(a:array<array<int>>, attribute: int, value: int) returns (filtered: seq<array<int>>)
  requires a != null && a.Length > 0;
  requires forall k :: 0 <= k < a.Length ==> a[k] != null && a[k].Length == 5;
  requires 0 <= attribute < 5;

  ensures forall k: int :: (0 <= k < a.Length ==> ((a[k][attribute] == value) ==> a[k] in filtered));
  ensures forall k: int :: (0 <= k < |filtered| ==> (filtered[k] != null && filtered[k].Length == 5));
  ensures forall k: int :: (0 <= k < |filtered| ==> filtered[k] in multiset(a[..]));
{
  var i : int := 0;
  filtered := [];
  while (i < a.Length)
    invariant 0 <= i <= a.Length;
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

// This method combines the filter method and the sum methods
// to give us the total volume of blood for a given type
method count_volume(deposits:array<array<int>>, value: int) returns (volume: int)
  requires deposits != null && deposits.Length > 0;
  requires forall k :: 0 <= k < deposits.Length ==> deposits[k] != null && deposits[k].Length == 5;
{
  // Note that the blood_type will always be at the 2nd index of each deposit (index == 1)
  var filtered: seq<array<int>> := filter(deposits,1,value);
  volume := sum_volume(filtered);
  return volume;
}
method Main() {

  var a1: array<int> := new int[5];
  a1[0], a1[1], a1[2], a1[3], a1[4] := 0, 0, 20, 30, 540;
  var a2: array<int> := new int[5];
  a2[0], a2[1], a2[2], a2[3], a2[4] := 1, 1, 23, 31, 241;
  var a3: array<int> := new int[5];
  a3[0], a3[1], a3[2], a3[3], a3[4] := 2, 2, 22, 32, 542;
  var a4: array<int> := new int[5];
  a4[0], a4[1], a4[2], a4[3], a4[4] := 3, 3, 23, 33, 343;
  var a5: array<int> := new int[5];
  a5[0], a5[1], a5[2], a5[3], a5[4] := 4, 0, 20, 30, 401;
  var a6: array<int> := new int[5];
  a6[0], a6[1], a6[2], a6[3], a6[4] := 5, 1, 23, 31, 512;
  var a7: array<int> := new int[5];
  a7[0], a7[1], a7[2], a7[3], a7[4] := 6, 2, 22, 32, 452;
  var a8: array<int> := new int[5];
  a8[0], a8[1], a8[2], a8[3], a8[4] := 7, 3, 23, 33, 423;
  var deposits: array<array> := new array[8];
  deposits[0], deposits[1], deposits[2], deposits[3] := a1, a2, a3, a4;
  deposits[4], deposits[5], deposits[6], deposits[7] := a5, a6, a7, a8;

  var filtered: seq<array<int>> := filter(deposits,1,2);
  var j : int := 0;
  while (j < |filtered|) {
    var k : int := 0;
    while (k < filtered[j].Length) {
      print filtered[j][k];
      print ' ';
      k := k + 1;
    }
    print '\n';
    j := j + 1;
  }
  
  var volume := sum_volume(filtered);
  print "\nVolume: ",volume,'\n';
  
}