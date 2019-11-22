// Insertion sort
// Sorts the blood score - descending order

predicate Sorted(a: array<int>, low:int, high:int)
	requires a != null
	requires 0<=low<=high<=a.Length
	reads a
{
	forall j,k:: low<=j<k<high ==> a[j]>=a[k]
}
 
 
//bList - List of wanted blood

method sortByScore(bList: array<int>)
	requires bList != null
	requires bList.Length > 1
	ensures Sorted(bList, 0, bList.Length);
	ensures multiset(bList[..]) == multiset(old(bList[..]));
	modifies bList;
{
	var i:=1;

	while (i < bList.Length)
		invariant 1 <= i <= bList.Length;
		invariant Sorted(bList, 0, i);
		invariant multiset(bList[..]) == multiset(old(bList[..]));
	{
		var j := i;

		while (j >= 1 && bList[j-1] < bList[j])
			invariant 0 <= j <= i;
			invariant forall x,y:: (0<=x<y<=i && y!=j) ==> bList[x]>=bList[y];
			invariant multiset(bList[..]) == multiset(old(bList[..]));
		{
			bList[j-1], bList[j] := bList[j], bList[j-1];
			j:=j-1;
		}
		i:=i+1;
	}
}
