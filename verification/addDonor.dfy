
method Main()
{
    //a1,a2 and a3 each represent an individual donor record
    var a1: array<int> := new int[7];
    a1[0], a1[1], a1[2], a1[3], a1[4], a1[5], a1[6] := 0, 10, 20, 30, 40, 50, 60;
    var a2: array<int> := new int[7];
    a2[0], a2[1], a2[2], a2[3], a2[4], a2[5], a2[6] := 1, 11, 23, 31, 41, 51, 61;
    var a3: array<int> := new int[7];
    a3[0], a3[1], a3[2], a3[3], a3[4], a3[5], a3[6] := 2, 11, 22, 32, 42, 52, 62;
    
    //Donors is a 2D array of donor records a1, a2 and a3
    var donors: array<array> := new array[3];
    donors[0], donors[1], donors[2] := a1, a2, a3;

    //a4 is the donor record to be added to donors
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


method addDonor(donors: array<array<int>>, newDonor : array<int>)  returns (updated: seq <array<int>>)
// Pre Conditions
//  - Donors array is not null
//  - Donors array length is 0 or more
//  - The newDonor record does not already exist in donors array
//  - Each sub-array in donors has 7 elements (corresponding to donor id, firstname, lastname, age, blood type, email, allergens)
//  - newDonor to be inserted has 7 elements (corresponding to donor id, firstname, lastname, age, blood type, email, allergens)
requires donors != null;
requires newDonor != null;
requires donors.Length >= 0;
requires forall r : int :: (0 <= r < donors.Length ==> donors[r] != null);
requires forall r : int :: (0 <= r < donors.Length ==> donors[r] != newDonor);
requires forall r : int :: (0 <= r < donors.Length ==> donors[r].Length == 7);
requires newDonor.Length == 7;

//Post Condition
//  - Updated sequence contains all records taht exist= in donors array + the newDonor record
//  - All records in the updated sequence are not null
ensures forall r : int :: (0 <= r < donors.Length ==> (donors[r] in updated && newDonor in updated));
ensures forall k : int :: (0 <= k < |updated|  ==> (updated[k] != null));
{   
    var i := 0;
    updated := [];
    while(i < donors.Length)
    invariant 0 <= i <= donors.Length
    invariant forall k : int :: (0 <= k < i ==> donors[k] in updated)
    invariant forall k : int :: (0 <= k < |updated|  ==> (updated[k] != null))
    {
        updated := updated + [donors[i]];
        i := i + 1;
    }
    updated := updated + [newDonor];   
   
}
