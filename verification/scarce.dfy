method Main() {

  var a1: array<int> := new int[2];
  a1[0], a1[1] := 0, 1000;
  var a2: array<int> := new int[2];
  a2[0], a2[1] := 1, 2000;
  var a3: array<int> := new int[2];
  a3[0], a3[1] := 2, 3000;
  var a4: array<int> := new int[2];
  a4[0], a4[1] := 3, 4000;
  var deposits: array<array> := new array[4];
  deposits[0], deposits[1], deposits[2], deposits[3] := a1, a2, a3, a4;

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

method findScarce(a:array<array<int>>, limit: int) returns (scarce: seq<array<int>>)
  requires a.Length > 0;
  requires forall k :: 0 <= k < a.Length ==> a[k].Length == 2;

  ensures forall k: int :: (0 <= k < a.Length ==> ((a[k][1] <= limit) ==> a[k] in scarce));
{
  var i : int := 0;
  while (i < a.Length)
    invariant 0 <= i <= a.Length;
    invariant forall k: int :: (0 <= k < i ==> ((a[k][1] <= limit) ==> a[k] in scarce));
  {
    if (a[i][1] <= limit) 
    { 
      scarce := scarce + [a[i]];
    }
    i := i + 1;
  }
}


