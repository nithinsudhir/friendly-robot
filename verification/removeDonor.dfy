
method Main()
{
    //a1, a2, a3 are individual donor records with donor id 0,1,2 respectively
    var a1: array<int> := new int[7];
    a1[0], a1[1], a1[2], a1[3], a1[4], a1[5], a1[6] := 0, 10, 20, 30, 40, 50, 60;
    var a2: array<int> := new int[7];
    a2[0], a2[1], a2[2], a2[3], a2[4], a2[5], a2[6] := 1, 11, 23, 31, 41, 51, 61;
    var a3: array<int> := new int[7];
    a3[0], a3[1], a3[2], a3[3], a3[4], a3[5], a3[6] := 2, 11, 22, 32, 42, 52, 62;
    
    //donors is a 2D array of donor records a1,a2 and a3
    var donors: seq <array> := [];
    donors := donors + [a1] + [a2] + [a3];

    assert donors[0] == a1;
    assert donors[1] == a2;
    assert donors[2] == a3;

    var s: seq<array<int>> := removeDonor(donors, 1);

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



method removeDonor(donors: seq <array<int>>, v: int) returns (updated : seq<array<int>>)
//Pre-Conditions
//  - Donors array is not null
//  - Length of donors array is 0 or more
//  - Each sub-array in donors has 7 elements (corresponding to donor id, firstname, lastname, age, blood type, email, allergens)
//  - Donor id to be removed must exist in the donors array 
requires donors != []
requires |donors| > 0
requires forall r : int :: (0 <= r < |donors|  ==> donors[r] != null);
requires forall k : int :: (0 <= k < |donors|  ==> donors[k].Length == 7) 
requires exists k : int :: 0 <= k < |donors|  && donors[k][0] == v 

//Post Conditions
//  - The donor with the donor id to be removed does not exist in updated sequence
//  - All records in the updated sequence are not null
ensures forall k : int :: ( 0 <= k < |donors|   ==> ((donors[k][0] != v) ==> (donors[k] in updated)))
ensures forall k : int :: (0 <= k < |updated|  ==> (updated[k] != null));
{
    var i : int := 0;
    updated := [];
    while (i < |donors| )
    decreases |donors|  - i
    invariant 0 <= i <= |donors| 
    invariant forall j : int :: (0 <= j < i ==> (donors[j][0] != v) ==> (donors[j] in updated))
    invariant forall j : int :: (0 <= j < |updated| ==> (updated[j] != null))
    {
       if(donors[i][0] != v){
           updated := updated + [donors[i]];
       }
        i := i + 1;
    }
}
