method Main() {

  var a1: array<int> := new int[5];
  a1[0], a1[1], a1[2], a1[3], a1[4] := 0, 10, 20, 30, 40;
  var a2: array<int> := new int[5];
  a2[0], a2[1], a2[2], a2[3], a2[4] := 1, 11, 21, 31, 41;
  var a3: array<int> := new int[5];
  a3[0], a3[1], a3[2], a3[3], a3[4] := 2, 12, 22, 32, 42;
  var a4: array<int> := new int[5];
  a4[0], a4[1], a4[2], a4[3], a4[4] := 3, 13, 23, 33, 43;
  var deposits: array<array> := new array[4];
  deposits[0], deposits[1], deposits[2], deposits[3] := a1, a2, a3, a4;
  print deposits[0][0];
  var res: array<array>, n: nat := filter(deposits,2);
}

predicate containsType(a: array<int>, x: int)
reads a
{ a[2] == x }

method copyArray(a: array<int>) returns (b: array<int>)
  ensures a.Length == b.Length
  ensures forall j :: 0 <= j < a.Length ==> a[j] == b[j]
  ensures b == a
{
  var i := 0;
  b := new int[a.Length];
  assert b.Length == a.Length;
  while (i < a.Length) 
    invariant 0 <= i <= a.Length
    invariant forall k :: 0 <= k < i ==> a[k] == b[k]
  {
    b[i] := a[i];
    i := i + 1;
  }
  assert i == a.Length && b.Length == a.Length;
}
method filter(a:array<array<int>>, x: int) returns (b:array<array<int>>, n:nat)
  ensures n <= a.Length;
  ensures b.Length == a.Length;
  
  // the elements of b[0..n] contain x
  ensures forall k :: 0 <= k < n ==> containsType(b[k],x);
  
  // the elements of b[0..n] come from a
  ensures forall j :: 0 <= j < n ==> b[j] in a[..] ;      
  
  // every matched element of a is in b[0..n]
  ensures (forall k:: 0 <= k < a.Length && containsType(a[k],x)) ==> 
            (exists j:: 0 <= j < n && containsType(b[j],x));    
{
  var i: nat := 0;
  n := 0;
  b := new array[a.Length];
  // copies in b all and only the positive elements of a
  while (i < a.Length)
    invariant n <= i <= a.Length;
    invariant n <= b.Length;
    
    // all the elements in b[0..n] match x
    invariant forall k :: 0 <= k < n ==> containsType(b[k],x);

    // every element in b[0..n] occurs in a[0..i]
    invariant forall j:: 0 <= j < n ==> b[j] in a[0..i] ;
    
    // every matched element of a[0..i] occurrs in b[0..n]
    invariant (forall k:: 0 <= k < i && containsType(a[k],x)) ==> 
            (exists j:: 0 <= j < n && containsType(b[j],x));   
  {
    if (containsType(a[i],x)) 
    { 
      b[n] := new int[5];
      b[n] := a[i];
      n := n + 1;
    }
    i := i + 1;
  }
}

