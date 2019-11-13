//Returns true if whole array is sorted
predicate Sorted(attribute:int,a:array<array<int>>)
  reads a;
  reads set b | 0 <= b < a.Length :: a[b];

  requires a != null;
  requires forall b:: 0 <= b < a.Length ==> a[b] != null;
  requires forall b:: 0 <= b < a.Length ==> a[b].Length == 5;
  requires 0 <= attribute < 5;
{
  forall m, n :: 0 <= m < n < a.Length ==> a[m][attribute] <= a[n][attribute]
}
  
//Returns true if array is sorted between lo and hi
predicate SortedBetween(attribute:int,a:array<array<int>>,lo:int,hi:int)
  reads a;
  reads set b | 0 <= b < a.Length :: a[b];


  requires a != null;
  requires 0 <= lo <= hi < a.Length;

  requires forall b:: 0 <= b < a.Length ==> a[b] != null;
  requires forall b:: 0 <= b < a.Length ==> a[b].Length == 5;
  requires 0 <= attribute < 5;

{
  forall m, n :: lo <= m < n <= hi ==> a[m][attribute] <= a[n][attribute]
}

//MergeSort function
method MergeSort(attribute:int,u:array<array<int>>) returns (a:array<array<int>>)
  modifies u;
  modifies set b | 0 <= b < u.Length :: u[b];

  requires u != null && u.Length > 0;
  requires forall b:: 0 <= b < u.Length ==> u[b] != null;
  requires forall b:: 0 <= b < u.Length ==> u[b].Length == 5;
  requires 0 <= attribute < 5;


  ensures a != null;
  ensures forall b:: 0 <= b < a.Length ==> a[b] != null;
  ensures forall b:: 0 <= b < a.Length ==> a[b].Length == 5;
  ensures a.Length == u.Length;
  ensures Sorted(attribute,a);
{
  a := RecursiveMerge(attribute,u,0,u.Length-1);
  return;
}

//Is called recursively to Mergesort, with the lo and hi index to indicate what section is being sorted
method RecursiveMerge(attribute:int,u:array<array<int>>,lo:int,hi:int) returns (a:array<array<int>>)
  modifies u;
  modifies set b | 0 <= b < u.Length :: u[b];

  requires u != null && u.Length > 0;
  requires 0 <= lo <= hi < u.Length;
  requires forall b:: 0 <= b < u.Length ==> u[b] != null;
  requires forall b:: 0 <= b < u.Length ==>  u[b].Length == 5;
  requires 0 <= attribute < 5;

  decreases hi-lo;
  ensures a != null;
  ensures a.Length == u.Length;
  ensures SortedBetween(attribute,a,lo,hi);
  ensures forall i:: 0 <= i < lo ==> a[i] == u[i]; // havent changed values that aren't being worked on
  ensures forall i:: hi < i < a.Length ==> a[i] == u[i]; // havent changed values that aren't being worked on
{
  a := new array[u.Length];
  forall (k | 0 <= k < u.Length)  {a[k] := u[k];}
  
  if (lo >= hi)
  {
    return;
  }
  else
  {
    var mid:int := (lo+hi) / 2;
    a := RecursiveMerge(attribute,a,lo,mid);
    a := RecursiveMerge(attribute,a,mid+1,hi);
    a := Merge(attribute,a,lo,mid,hi);
    return;
  }
}

//Merges two arrays as necessary
method Merge(attribute:int, u:array<array<int>>, lo:int, mid:int, hi:int) returns (a:array<array<int>>)
modifies u;
modifies set b | 0 <= b < u.Length :: u[b];

requires u != null && u.Length > 0;
requires 0 <= lo <= mid <= hi < u.Length;
requires SortedBetween(attribute,u,lo,mid);
requires hi <= mid || SortedBetween(attribute,u,mid+1,hi);

requires forall b:: 0 <= b < u.Length ==> u[b] != null;
requires forall b:: 0 <= b < u.Length ==> u[b].Length == 5;
requires 0 <= attribute < 5;

ensures a != null;
ensures a.Length == u.Length;
ensures SortedBetween(attribute,a,lo,hi);

ensures forall i:: 0 <= i < lo ==> a[i] == u[i] // havent changed values that aren't being worked on
ensures forall i:: hi < i < u.Length ==> a[i] == u[i] // havent changed values that aren't being worked on

decreases hi-lo; //array becomes smaller
{
  a := new array[u.Length];
  forall (k | 0 <= k < u.Length)  {a[k] := u[k];}
  var tmp : array<array> := new array[hi-lo+1];
  
  var x:int := lo;
  var y:int := mid + 1;
  var i:int := 0;
  
  while (i < hi-lo+1)
    invariant forall k:: 0 <= k < u.Length ==> a[k] == u[k];
    invariant 0 <= i <= hi-lo+1; // i stays within tmp array
    invariant lo <= x <= mid+1; 
    invariant mid+1 <= y <= hi+1; 
    
    invariant (x-lo) + (y-(mid+1)) == i; // i is in right place
    invariant i == 0 || SortedBetween(attribute,tmp,0,i-1); // tmp is always sorted

    invariant forall b:: 0 <= b <= i ==> tmp[b] != null;
    invariant forall b:: 0 <= b <= i ==> tmp[b].Length == 5;
    invariant forall q, r:: 0 <= q < i && (x <= r <= mid || y <= r <= hi) ==> tmp[q][attribute] <= a[r][attribute]; //both arrays have been merged correctly
  {
    if (x > mid) //right array is completely merged
    {
      tmp[i] := new int[a[y].Length];
      forall (k | 0 <= k < a[y].Length)  {tmp[i][k] := a[y][k];}
      y := y + 1;
    }
    else if (y > hi) //left array is completely merged
    {
      tmp[i] := new int[a[x].Length];
      forall (k | 0 <= k < a[x].Length)  {tmp[i][k] := a[x][k];}
      x := x + 1;
    }
    else if (a[x][attribute] <= a[y][attribute]) //take from right array
    {
      tmp[i] := new int[a[x].Length];
      forall (k | 0 <= k < a[x].Length)  {tmp[i][k] := a[x][k];}
      x := x + 1;
    }
    else
    {
      tmp[i] := new int[a[y].Length];
      forall (k | 0 <= k < a[y].Length)  {tmp[i][k] := a[y][k];}
      //take from left array
      y := y + 1;
    }
    i := i + 1;
  }

  i := 0;
  while (i < hi-lo+1)
    invariant 0 <= i <= hi-lo+1;
    invariant forall q  :: (0 <= q < lo || hi < q < u.Length) ==> a[q] == u[q]; // array hasn't changed
    
    invariant forall q:: forall r:: 0 <= q < r < hi-lo+1 ==>  tmp[q][attribute] <= tmp[r][attribute]; // tmp is sorted (ie hasnt changed)
    invariant forall q:: lo <= q < lo+i ==> tmp[q-lo] == a[q]; //tmp is copied to a
    invariant forall q:: forall r:: lo <= q < r < lo+i ==> a[q][attribute] <= a[r][attribute]; // a is sorted

  {
    //copies array to tmp
    a[lo + i] := tmp[i];
    i := i + 1;
  }
}

//Main tests functionality
method Main() 
{
  var a1: array<int> := new int[5];
  a1[0], a1[1], a1[2], a1[3], a1[4] := 0, 10, 20, 30, 40;
  var a2: array<int> := new int[5];
  a2[0], a2[1], a2[2], a2[3], a2[4] := 1, 11, 23, 31, 41;
  var a3: array<int> := new int[5];
  a3[0], a3[1], a3[2], a3[3], a3[4] := 2, 11, 22, 32, 42;
  var a4: array<int> := new int[5];
  a4[0], a4[1], a4[2], a4[3], a4[4] := 3, 11, 23, 33, 43;
  var deposits: array<array> := new array[4];
  deposits[0], deposits[1], deposits[2], deposits[3] := a1, a2, a3, a4;

  var arr: array<array<int>> := MergeSort(2,deposits);

  print arr;

  print arr[..];

}