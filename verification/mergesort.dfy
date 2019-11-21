//This program verifies the Mergesort algorithm as is used for the purpose of the Blood Bank system (misc/sort.py)


//Is true if whole array is sorted
predicate Sorted(a:array<int>)
  reads a;
  requires a != null; 
{
  forall m, n :: 0 <= m < n < a.Length ==> a[m] <= a[n]
}
  
//Is true if array is sorted between lo and hi
predicate SortedBetween(a:array<int>,lo:int,hi:int)
  reads a;
  requires a != null;
  requires 0 <= lo <= hi < a.Length;
{
  forall m, n :: lo <= m < n <= hi ==> a[m] <= a[n]
}

//MergeSort function. Returns a sorted array.
method MergeSort(u:array<int>) returns (a:array<int>)
  requires u != null && u.Length > 0;
  ensures a != null;
  ensures a.Length == u.Length;
  ensures Sorted(a);
{
  a := RecursiveMerge(u,0,u.Length-1);
  return;
}

//Is called recursively to Mergesort, with the lo and hi index to indicate what section is being sorted
method RecursiveMerge(u:array<int>,lo:int,hi:int) returns (a:array<int>)
  requires u != null && u.Length > 0;
  requires 0 <= lo <= hi < u.Length;
  decreases hi-lo;
  ensures a != null;
  ensures a.Length == u.Length;
  ensures SortedBetween(a,lo,hi);
  ensures forall i:: 0 <= i < lo ==> a[i] == u[i]; // havent changed values that aren't being worked on
  ensures forall i:: hi < i < a.Length ==> a[i] == u[i]; // havent changed values that aren't being worked on
{
  a := new int[u.Length];
  forall (k | 0 <= k < u.Length)  {a[k] := u[k];}
  
  if (lo >= hi)
  {
    return;
  }
  else
  {
    var mid:int := (lo+hi) / 2;
    a := RecursiveMerge(a,lo,mid);
    a := RecursiveMerge(a,mid+1,hi);
    a := Merge(a,lo,mid,hi);
    return;
  }
}

//Merges two arrays as necessary
method Merge(u:array<int>, lo:int, mid:int, hi:int) returns (a:array<int>)
requires u != null && u.Length > 0;
requires 0 <= lo <= mid <= hi < u.Length;
requires SortedBetween(u,lo,mid); // the array being merged is already sorted
requires hi <= mid || SortedBetween(u,mid+1,hi);

ensures a != null;
ensures a.Length == u.Length;
ensures SortedBetween(a,lo,hi);

ensures forall i:: 0 <= i < lo ==> a[i] == u[i] // havent changed values that aren't being worked on
ensures forall i:: hi < i < u.Length ==> a[i] == u[i] // havent changed values that aren't being worked on

decreases hi-lo; //array becomes smaller
{
  a := new int[u.Length];
  forall (k | 0 <= k < u.Length)  {a[k] := u[k];}
  var tmp := new int[hi-lo+1];
  var x:int := lo;
  var y:int := mid + 1;
  var i:int := 0;
  
  while (i < hi-lo+1)
    invariant forall k:: 0 <= k < u.Length ==> a[k] == u[k];
    invariant 0 <= i <= hi-lo+1; // i stays within tmp array
    invariant lo <= x <= mid+1; 
    invariant mid+1 <= y <= hi+1; 
    
    invariant (x-lo) + (y-(mid+1)) == i; // i is in the right place with respect to each 'arrays' position
    invariant i == 0 || SortedBetween(tmp,0,i-1); // tmp is always sorted
    invariant forall q, r:: 0 <= q < i && (x <= r <= mid || y <= r <= hi) ==> tmp[q] <= a[r]; //both arrays have been merged correctly
  {
    if (x > mid) //right array is completely merged
    {
      tmp[i] := a[y];
      y := y + 1;
    }
    else if (y > hi) //left array is completely merged
    {
      tmp[i] := a[x];
      x := x + 1;
    }
    else if (a[x] <= a[y]) //take from right array
    {
      tmp[i] := a[x];
      x := x + 1;
    }
    else
    {
      tmp[i] := a[y]; //take from left array
      y := y + 1;
    }
    i := i + 1;
  }

  i := 0;
  while (i < hi-lo+1)
    invariant 0 <= i <= hi-lo+1;
    invariant forall q  :: (0 <= q < lo || hi < q < u.Length) ==> a[q] == u[q]; // array hasn't changed
    
    invariant forall q:: forall r:: 0 <= q < r < hi-lo+1 ==>  tmp[q] <= tmp[r]; // tmp is sorted (ie hasnt changed)
    invariant forall q:: lo <= q < lo+i ==> tmp[q-lo] == a[q]; //tmp is copied to a
    invariant forall q:: forall r:: lo <= q < r < lo+i ==> a[q] <= a[r]; // a is sorted

  {
  	//copies array to tmp
    a[lo + i] := tmp[i];
    i := i + 1;
  }
}

//Main tests functionality
method Main() 
{
  var arr : array<int> := new int[5];
  arr[0],arr[1],arr[2],arr[3],arr[4] := 7,4,2,6,7;
  assert arr[0] == 7;
  assert arr[1] == 4;
  assert arr[2] == 2;
  assert arr[3] == 6;
  assert arr[4] == 7;
  arr := MergeSort(arr);
  assert Sorted(arr);
  print arr[..],"\n";

}