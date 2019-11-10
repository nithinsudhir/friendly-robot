// predicate isNotIn(a:array<int> , id : int) 
// reads a 
// {
//     forall k :: 0<=k<a.Length ==> a[k] != id
// }


// method addDonor(a: array<array<int>>, id: int)  returns (res: array <array<int>>)
// requires a != null
// //Pre-Conditions:
// //      - Array length has 0 or more elements
// //      - New donor (id) does not already exist in array
// requires a.Length >= 0
// requires forall r :: 0 <= r < a.Length ==> a[r].Length == 7
// requires forall r :: 0 <= r < a.Length ==> isNotIn(a[r],id)
// //Post-Conditions:
// //      - The last appended value in array is id
// //      - New array length = old (a.Length) + 1
// ensures forall r :: 0 <= r < a.Length && res.Length >= a.Length ==> a[r] == res[r] && res[res.Length - 1][0] == id
// ensures res.Length == a.Length + 1
// ensures a.Length == 0 && res.Length == 1 ==> res[0][0] == id
// {   

//     //var newArr : array<array<int>> := new int[a.Length+1];

//     if(a.Length == 0)
//     {   
//         res[0][0] := id;
//     }
//     else{
//         forall (i | 0 <= i < a.Length){
//             res[i]:=a[i];
//         }
//         //FIX THIS
//         res[a.Length + 1][0] := id;
//     }
   
// }