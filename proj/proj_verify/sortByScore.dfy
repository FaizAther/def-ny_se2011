// Use insertion sort algorithm

predicate Sorted(a: array<int>, low:int, high:int)
 requires a != null // 1.9.7
 requires 0<=low<=high<=a.Length
 reads a
 { forall j,k:: low<=j<k<high ==> a[j]<=a[k] }
 
 
method InsertionSortSwap(a: array<int>)
requires a != null // 1.9.7
requires a.Length > 1
ensures Sorted(a, 0, a.Length);
ensures multiset(a[..]) == multiset(old(a[..]));
modifies a;
{
 var up:=1;
 while (up < a.Length)
 invariant 1 <= up <= a.Length;
 invariant Sorted(a, 0, up);
 invariant multiset(a[..]) == multiset(old(a[..]));
 {
 var down := up; // the next unordered element
 while (down >= 1 && a[down-1] > a[down])
 invariant 0 <= down <= up;
 invariant forall i,j:: (0<=i<j<=up && j!=down) ==> a[i]<=a[j];
 invariant multiset(a[..]) == multiset(old(a[..]));
 {
 a[down-1], a[down] := a[down], a[down-1];
 down:=down-1;
 }
 up:=up+1;
 }
}
