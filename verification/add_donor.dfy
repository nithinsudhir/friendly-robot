
method Main()
{
    var a1: array<int> := new int[7];
    a1[0], a1[1], a1[2], a1[3], a1[4], a1[5], a1[6] := 0, 10, 20, 30, 40, 50, 60;
    var a2: array<int> := new int[7];
    a2[0], a2[1], a2[2], a2[3], a2[4], a2[5], a2[6] := 1, 11, 23, 31, 41, 51, 61;
    var a3: array<int> := new int[7];
    a3[0], a3[1], a3[2], a3[3], a3[4], a3[5], a3[6] := 2, 11, 22, 32, 42, 52, 62;
    
    var donors: array<array> := new array[4];
    donors[0], donors[1], donors[2] := a1, a2, a3;

    var a4: array<int> := new int[7];
    a4[0], a4[1], a4[2], a4[3], a4[4], a4[5], a4[6] := 3, 11, 23, 33, 43, 53, 63;

    var s: seq<array<int>> := addDonor(donors, a4);

    var j : int := 0;
    while (j < |s|) {
    var k : int := 0;
        while (k < s[j].Length) {
        print s[j][k];
        print ' ';
        k := k + 1;
    }
    print '\n';
    j := j + 1;
  }

}

//This method interprets donor records as an array of arrays 'a'
//Array l is the new donor record to be added to a
method addDonor(a: array<array<int>>, l : array<int>)  returns (res: seq <array<int>>)

requires a != null
requires a.Length >= 0
requires forall r :: 0 <= r < a.Length ==> a[r] != l 
requires l.Length == 7

ensures forall r : int:: (0 <= r < a.Length ==> (a[r] in res && l in res))
{   
    var i := 0;
    while(i < a.Length)
    invariant 0 <= i <= a.Length 
    invariant forall k : int :: (0 <= k < i ==> a[k] in res)
    {
        res := res + [a[i]];
        i := i + 1;
    }
    res := res + [l];   
   
}

