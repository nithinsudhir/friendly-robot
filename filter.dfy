method Main() {
  var a: array<string> := new string[8];
  a[0], a[1], a[2], a[3]:= "47","23","23","17";
  a[4], a[5], a[6], a[7]:= "47","23","23","17";
  print a.Length,'\n';
  var x: array<string>, n: nat := filter(a,"23");
  var i:= 0;
  while i < x.Length {
      print x[i],",";
    
    i := i + 1;
  }
  
}


method filter(a:array<string>, x: string) returns (b:array<string>, n:nat)
  ensures n <= a.Length;
  ensures b.Length == a.Length;
  
  // the elements of b[0..n] equal x
  ensures forall k :: 0 <= k < n ==> b[k] == x ;  
  
  // the elements of b[0..n] come from a
  ensures forall j :: 0 <= j < n ==> b[j] in a[0..] ;      
  
  // every matched element of a is in b[0..n]
  ensures forall k:: 0 <= k < a.Length && a[k] == x ==> 
            exists j:: 0 <= j < n && b[j] == a[k] ;    
{
  var i: nat := 0;
  n := 0;
  b := new string[a.Length];

  // copies in b all and only the positive elements of a
  while (i < a.Length)
    invariant n <= i <= a.Length;
    invariant n <= b.Length;
    
    // all the elements in b[0..n] are positive
    invariant forall k :: 0 <= k < n ==> b[k] == x ;
    // every element in b[0..n] occurs in a[0..i]
    //invariant forall j:: 0 <= j < n ==> exists k :: 0 <= k < i && b[j] == a[k] ;  
    // Alternatively:
    invariant forall j:: 0 <= j < n ==> b[j] in a[0..i] ;
    
    // every positive element of a[0..i] occurrs in b[0..n]
    invariant forall k :: 0 <= k < i && a[k] == x ==> exists j:: 0 <= j < n && b[j] == a[k] ;  
    // Alternatively: 
    //invariant forall k :: 0 <= k < i && a[k] > 0 ==> a[k] in b[0..n] ;  
  {
    if (a[i] == x) 
    { 
      b[n] := a[i];
    n := n + 1;
    }
    i := i + 1;
  }
}
