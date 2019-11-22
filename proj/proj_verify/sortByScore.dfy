// Insertion sort
// Sorts the blood score - descending order


class Blood {
	var score :real;
  
	constructor(s :real)
		modifies this
		ensures score == s
	{
		score := s;
	}
}


predicate Sorted(a: seq<Blood>, low:int, high:int)
	//requires a != null
	requires 0<=low<=high<=|a|//.Length
	reads a
{
	forall j,k:: low<=j<k<high ==> a[j].score>=a[k].score
}
 
 
//bList - List of wanted blood

method sortByScore(bList: array<Blood>) returns (sorted :seq<Blood>)
	requires bList != null
	requires bList.Length > 1
	ensures Sorted(bList[..], 0, |bList[..]|)
  ensures multiset(old(bList)[..]) == multiset(sorted)
  ensures multiset(bList[..]) == multiset(sorted)
	modifies bList
{
	var i:=1;

  var u :seq<Blood> := bList[..];
  assert u == old(bList)[..];
  assert u == bList[..];
  assert multiset(u) == multiset(u);
  assert multiset(bList[..]) == multiset(u);
  assert multiset(u) == multiset(old(bList)[..]);
  
	while (i < bList.Length)
		invariant 1 <= i <= bList.Length;
		invariant Sorted(bList[..], 0, i);
		invariant multiset(bList[..]) == multiset(u);
	{
		var j := i;
		while (j >= 1 && bList[j-1].score < bList[j].score)
			invariant 0 <= j <= i;
			invariant forall x,y:: (0<=x<y<=i && y!=j) ==> bList[x].score>=bList[y].score;
			invariant multiset(bList[..]) == multiset(u);
		{
			bList[j-1], bList[j] := bList[j], bList[j-1];
			j:=j-1;
		}
		i:=i+1;
	}
  sorted := bList[..];
}
