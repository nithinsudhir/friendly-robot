class Blood {
  var depositId :int;
  var donorId :int;
  var bloodType :int;
  var expiry :int;
  var amount :int;

  predicate Valid()
  reads this;
  {
    depositId > 0 && donorId > 0 && bloodType > 0 && expiry > 0 && amount > 0
  }

  constructor(deId:int, doId:int, bt:int, ex:int, am:int) modifies this
  requires deId > 0 && doId > 0 && bt > 0 && ex > 0 && am > 0;
  ensures Valid();
  {
    depositId := deId;
    donorId := doId;
    bloodType := bt;
    expiry := ex;
    amount := am;
  }
}

function method bloodGreaterThan(attribute:int, blood1:Blood, blood2:Blood) : bool
reads blood1;
reads blood2;
requires 1 <= attribute <= 5;
requires blood1 != null && blood2 != null;
{
  if attribute == 1 then (if blood1.depositId >= blood2.depositId then true else false) else if attribute == 2 then (if blood1.donorId >= blood2.donorId then true else false) else if attribute == 3 then (if blood1.bloodType >= blood2.bloodType then true else false) else if attribute == 4 then (if blood1.expiry >= blood2.expiry then true else false) else if attribute == 5 then (if blood1.amount >= blood2.amount then true else false) else false
}

method greaterThan(attribute:int, blood1:Blood, blood2:Blood) returns (res:bool)
requires 1 <= attribute <= 5
requires blood1 != null && blood2 != null
ensures res == bloodGreaterThan(attribute,blood1,blood2)
{
  if attribute == 1 {
    if (blood1.depositId >= blood2.depositId) {
      res := true;
    } else {
      res := false;
    }
  } else if attribute == 2 {
    if (blood1.donorId >= blood2.donorId) {
      res := true;
    } else {
      res := false;
    }
  } else if attribute == 3 {
    if (blood1.bloodType >= blood2.bloodType) {
      res := true;
    } else {
      res := false;
    }
  } else if attribute == 4 {
    if (blood1.expiry >= blood2.expiry) {
      res := true;
    } else {
      res := false;
    }
  } else if attribute == 5 {
    if (blood1.amount >= blood2.amount) {
      res := true;
    } else {
      res := false;
    }
  }
}


//Is true if whole array is sorted
predicate Sorted(attribute:int,a:array<Blood>)
  reads a;
  reads set b | 0 <= b < a.Length :: a[b];

  requires a != null; 
  requires forall b:: 0 <= b < a.Length ==> a[b] != null;
  requires 1<=attribute<=5;
{
  forall m, n :: 0 <= m < n < a.Length ==> bloodGreaterThan(attribute,a[n],a[m])
}
  
//Is true if array is sorted between lo and hi
predicate SortedBetween(attribute:int,a:array<Blood>,lo:int,hi:int)
  reads a;
  reads set b | 0 <= b < a.Length :: a[b];

  requires a != null;
  requires 0 <= lo <= hi < a.Length;
  requires 1<=attribute<=5;
  requires forall b:: 0 <= b <= hi ==> a[b] != null;

{
  forall m, n :: lo <= m < n <= hi ==> bloodGreaterThan(attribute,a[n],a[m])
}

//MergeSort function
method MergeSort(attribute:int,u:array<Blood>) returns (a:array<Blood>)
  requires u != null && u.Length > 0;
  requires 1<=attribute<=5;
  requires forall b:: 0 <= b < u.Length ==> u[b] != null;


  ensures a != null;
  ensures a.Length == u.Length;
  ensures forall b:: 0 <= b < a.Length ==> a[b] != null;

  ensures Sorted(attribute,a);


{
  a := RecursiveMerge(attribute,u,0,u.Length-1);
  return;
}

//Is called recursively to Mergesort, with the lo and hi index to indicate what section is being sorted
method RecursiveMerge(attribute:int,u:array<Blood>,lo:int,hi:int) returns (a:array<Blood>)
  requires u != null && u.Length > 0;
  requires 0 <= lo <= hi < u.Length;
  requires 1<=attribute<=5;
  requires forall b:: 0 <= b < u.Length ==> u[b] != null;


  decreases hi-lo;
  ensures a != null;
  ensures a.Length == u.Length;
  ensures forall b:: 0 <= b < a.Length ==> a[b] != null;

  ensures SortedBetween(attribute,a,lo,hi);
  ensures forall i:: 0 <= i < lo ==> a[i] == u[i]; // havent changed values that aren't being worked on
  ensures forall i:: hi < i < a.Length ==> a[i] == u[i]; // havent changed values that aren't being worked on
{
  a := new Blood[u.Length];
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
method Merge(attribute:int,u:array<Blood>, lo:int, mid:int, hi:int) returns (a:array<Blood>)
requires 1<=attribute<=5;

requires u != null && u.Length > 0;
requires 0 <= lo <= mid <= hi < u.Length;
requires forall b:: 0 <= b < u.Length ==> u[b] != null;

requires SortedBetween(attribute,u,lo,mid);
requires hi <= mid || SortedBetween(attribute,u,mid+1,hi);


requires forall b:: 0 <= b < u.Length ==> u[b] != null;



ensures a != null;
ensures a.Length == u.Length;
ensures forall b:: 0 <= b < a.Length ==> a[b] != null;

ensures SortedBetween(attribute,a,lo,hi);

ensures forall i:: 0 <= i < lo ==> a[i] == u[i] // havent changed values that aren't being worked on
ensures forall i:: hi < i < u.Length ==> a[i] == u[i] // havent changed values that aren't being worked on

decreases hi-lo; //array becomes smaller
{
  a := new Blood[u.Length];
  forall (k | 0 <= k < u.Length)  {a[k] := u[k];}
  var tmp := new Blood[hi-lo+1];
  var x:int := lo;
  var y:int := mid + 1;
  var i:int := 0;
  
  while (i < hi-lo+1)
    invariant forall k:: 0 <= k < u.Length ==> a[k] == u[k];
    invariant 0 <= i <= hi-lo+1; // i stays within tmp array
    invariant lo <= x <= mid+1; 
    invariant mid+1 <= y <= hi+1; 
    
    invariant (x-lo) + (y-(mid+1)) == i; // i aligns properly.

    invariant forall b:: 0 <= b <= i-1 ==> tmp[b] != null;

    invariant i == 0 || SortedBetween(attribute,tmp,0,i-1); // tmp is always sorted
    invariant forall q, r:: 0 <= q < i && (x <= r <= mid || y <= r <= hi) ==> bloodGreaterThan(attribute,a[r],a[q]); //both arrays have been merged correctly
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
    else if (bloodGreaterThan(attribute,a[y],a[x])) //take from right array
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
    
    invariant forall b:: 0 <= b < hi-lo+1 ==> tmp[b] != null;

    invariant forall q:: forall r:: 0 <= q < r < hi-lo+1 ==>  bloodGreaterThan(attribute,tmp[r],tmp[q]); // tmp is sorted (ie hasnt changed)
    invariant forall q:: lo <= q < lo+i ==> tmp[q-lo] == a[q]; //tmp is copied to a
    invariant forall q:: forall r:: lo <= q < r < lo+i ==> bloodGreaterThan(attribute,a[r],a[q]); // a is sorted

  {
    //copies array to tmp
    a[lo + i] := tmp[i];
    i := i + 1;
  }
}

//Main tests functionality
method Main() 
{
  var arr : array<Blood> := new Blood[5];
  var b1 := new Blood(5,5,6,3,4);
  var b2 := new Blood(2,3,7,3,3);
  var b3 := new Blood(5,5,1,3,5);
  var b4 := new Blood(53,6,3,3,1);
  var b5 := new Blood(3,5,7,5,6);

  arr[0],arr[1],arr[2],arr[3],arr[4] := b1,b2,b3,b4,b5;
  assert arr[0] == b1;
  assert arr[1] == b2;
  assert arr[2] == b3;
  assert arr[3] == b4;
  assert arr[4] == b5;
  arr := MergeSort(2,arr);
}