//Add Donor verification

//Predicate to check if id is not present in array a
predicate isNotIn(a:array<int> , id : int) 
reads a 
{
    forall k :: 0<=k<a.Length ==> a[k] != id
}


//This method interprets each donor record as a list with a unique donor_id for each row
// array 'a' represents a list of donor_id
// int 'id' represents new donor_id

method addDonor(a: array<int>, id: int)  returns (res: array<int>)
requires a != null
//Pre-Conditions:
//      - Array length has 0 or more elements
//      - New donor (id) does not already exist in array
requires a.Length >= 0
requires isNotIn(a,id)
//Post-Conditions:
//      - The last appended value in array is id
//      - New array length = old (a.Length) + 1
ensures forall i :: 0<=i<a.Length && res.Length >= a.Length ==> a[i] == res[i] && res[res.Length-1] == id
ensures res.Length == a.Length + 1
ensures a.Length == 0 && res.Length == 1 ==> res[0] == id
{   
    var newArr : array<int> := new int[a.Length+1];

    if(a.Length == 0)
    {   
        newArr[0] := id;
        res := newArr;
    }
    else{
        forall (i | 0<=i<a.Length){
            newArr[i]:=a[i];
        }
        newArr[newArr.Length-1] := id;
        res := newArr;
    }
   
}

method Main()
{
    var arr: array<int>:= new int[3];
    arr[0],arr[1], arr[2] := 1,2,3;
    assert arr[0] == 1;
    assert arr[1] == 2;
    assert arr[2] == 3;
    
    var newArr1 := addDonor(arr,4);
    assert newArr1[0] == 1;
    assert newArr1[1] == 2;
    assert newArr1[2] == 3;
    assert newArr1[3] == 4;

    var emptyArr : array<int> := new int[0];
    var newArr2 := addDonor(emptyArr,1);
    assert newArr2[0] == 1;  
}
