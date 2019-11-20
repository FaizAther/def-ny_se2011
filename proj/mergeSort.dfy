//Proving merge sort
//ISSUE: it be verified on local IDE,
//       but it times out while verifying on the website dafny
predicate permutation(a: seq<int>, b: seq<int>)
{
  a == b || multiset(a) == multiset(b)
}

// To make Dafny know the elements in 2 subseq of a sequence is the same as the elements in this whole sequnce
lemma  MutisetAddingLemma(a: array<int>,low:int, mid: int, upper:int)
  requires 0<=low<=mid<=upper<a.Length
  ensures multiset(a[low..mid]) + multiset(a[mid..upper+1]) == multiset(a[low..upper+1])
{
    assert a[low..mid] + a[mid..upper+1] == a[low..upper+1];
}

//array is sorted between start and end
predicate sortedBetween(a :array<int>, start : int, end : int)
  reads a;
  requires 0<= start < a.Length
  requires 0<= end < a.Length
{
  forall i,j:: start <= i < j <= end ==> a[i] <= a[j]
}

//whole array is sorted
predicate Sorted(a :array<int>)
  reads a;
{
  forall q,r:: 0 <= q < r < a.Length ==> a[q] <= a[r]
}

method MergeSort(a1:array<int>) returns (a:array<int>)
  requires a1.Length > 0;
  ensures Sorted(a);
  ensures permutation(a[..], old(a)[..]);
{
  a := mergesort(a1, 0, a1.Length-1);
}

//recursive merge sort function
method mergesort(a1:array<int>, low:int, upper:int) returns (a:array<int>)
  requires a1.Length > 0;
  requires 0 <= low <= upper < a1.Length;
  ensures a.Length == a1.Length;
  ensures sortedBetween(a,low,upper);
  ensures forall q:: (0 <= q < low || upper < q < a.Length) ==> a[q] == a1[q];
  ensures permutation(a[low..upper+1], a1[low..upper+1]);
  ensures a[0..low] == a1[0..low];
  ensures a[upper+1..] == a1[upper+1..];
  decreases upper-low;
{
  a := new int[a1.Length];
  copyArray(a1, a);
  if (low <  upper){
    var mid:int := (low + upper) / 2;
    a := mergesort(a1, low, mid);//sort the a[low..mid] part
    assert a[mid+1..upper+1] == a1[mid+1..upper+1];
    a := mergesort(a, mid+1, upper);//sort the a[mid+1..upper] part

    assert permutation(a[low..mid+1], a1[low..mid+1]);
    assert permutation(a[mid+1..upper+1],a1[mid+1..upper+1]);
    MutisetAddingLemma(a,low,mid+1,upper);
    MutisetAddingLemma(a1,low,mid+1,upper);
    assert multiset(a[low..upper+1]) == multiset(a1[low..upper+1]);

    a := merge(a, low, mid, upper);//at last merge two parts, and whole array become sorted
  }
}
//this method copy array from a into b
method copyArray(a: array<int>, b: array<int>)
  modifies b;
  requires a.Length  == b.Length
  ensures a.Length == b.Length
  ensures a[..] == b[..]
{
  var index:= 0;
  while (index < a.Length)
    decreases a.Length - index
    invariant 0 <= index <= a.Length
    invariant a[..] == old(a)[..]
    invariant b[..index] == a[..index]
    invariant b.Length == a.Length
  {
    b[index] := a[index];
    index := index + 1;
  }
}


//merge arrays a[low..mid+1] and a[mid+1..upper] into new array buf
method merge(a:array<int>, low:int, mid:int, upper:int) returns (buf:array<int>)
  requires a.Length > 0;
  requires 0 <= low <= mid < upper < a.Length;
  requires sortedBetween(a,low,mid);
  requires sortedBetween(a,mid+1,upper);
  ensures a.Length == buf.Length;
  ensures multiset(buf[low..upper+1]) == multiset(a[low..upper+1]);
  ensures sortedBetween(buf,low,upper);
  ensures forall i:: (0 <= i < low || upper < i < buf.Length) ==> buf[i] == a[i];
{
  buf := new int[a.Length];//buffer stores array that is merged
  copyArray(a, buf);


  var i:int := low;
  var j:int := mid + 1;
  var k:int := 0;
  while (k < upper-low+1)
    decreases upper-low+1 -k;
    invariant  forall k:: 0 <= k < a.Length ==> a[k] == a[k];

    // k is in this buffer index
    invariant 0 <= k <= upper-low+1;
    // j is in the right place
    invariant mid+1 <= j <= upper+1;
    // i is in the right place
    invariant low <= i <= mid+1;

    // k aligns properly.
    invariant (i-low) + (j-(mid+1)) == k;
    invariant buf.Length == a.Length;
    // elements maintain the same
    invariant multiset(buf[low..low+k]) == multiset(a[low..i]) + multiset(a[mid+1..j]);
    invariant buf[0..low] == a[0..low];
    invariant buf[upper+1..] == a[upper+1..];
    // buf is sorted in [low,k+low].
    invariant forall q,r:: low <= q < r <= k+low-1 ==>  buf[q] <= buf[r];
    invariant forall q,r:: low <= q < low+k && (i <= r <= mid || j <= r <= upper) ==> buf[q] <= a[r];
  {
    //when one part of array runs out of elements,
    //the rest spaces of the buffer should store elements from other part
    if (i > mid)
    {
      buf[low+k] := a[j];
      j := j + 1;
    }
    else if (j > upper)
    {
      buf[low+k] := a[i];
      i := i + 1;
    }
    //place the smaller element from 2 array parts into the buffer array first
    else if (a[i] <= a[j])
    {
      buf[low+k] := a[i];
      i := i + 1;
    }
    else
    {
      buf[low+k] := a[j];
      j := j + 1;
    }
    k := k + 1;
  }
  MutisetAddingLemma(buf,low,mid+1,upper);
  MutisetAddingLemma(a,low,mid+1,upper);
  assert  buf[..low] + buf[low..upper+1] + buf[upper+1..] == buf[..];
  assert  a[..low] + a[low..upper+1] + a[upper+1..] == a[..];
  assert multiset(buf[0..low]) + multiset(buf[low..upper+1]) + multiset(buf[upper+1..]) == multiset(buf[..]);
  assert multiset(a[0..low]) + multiset(a[low..upper+1]) + multiset(a[upper+1..]) == multiset(a[..]);
  //three parts of buffer array contain the same elements as a
  assert multiset(buf[upper+1..]) == multiset(a[upper+1..]);
  assert multiset(buf[0..low]) == multiset(a[0..low]);
  assert multiset(buf[low..upper+1]) == multiset(a[low..upper+1]);
  //so they are permutation
  assert multiset(buf[..]) == multiset(a[..]);
}


/// first version
method mergeSort(bloods: array?<int>)
modifies bloods;
requires bloods != null;
requires bloods.Length > 0;
//requires |bloods| > 0;
ensures sorted(bloods);
ensures bloods.Length > 0;
//requires |bloods| > 0;

{
  if bloods.Length > 1
  {
    var n := bloods.Length;
    var mid := n/2;
    var left := bloods[0..mid];
    var right := bloods[mid..n];
    ////////////////////////
    //mergeSort(left);
    left := mergeSort(left);
    right := mergeSort(right);

    var i := 0;
    var j := 0;
    var k := 0;

    var x := left.Length;
    var y := right.Length;

    while i < x && j < y
    invariant 0 <= i <= x;
    invariant 0 <= j <= y;

    {
      if left[i] > right[j]
      {
        bloods[k] := left[i];
        i := i + 1;

      } else
      {
        bloods[k] := right[j];
        j := j + 1;
      }

      k := k + 1;
    }

    while i < x
    invariant 0 <= i <= x;

    {
      bloods[k] := left[i];
      i := i+1;
      k := k+1;
    }

    while j < y
    invariant 0 <= j <= y;
    {
      bloods[k] := right[j];
      j := j + 1;
      k := k+1;
    }

  }

}

predicate sorted(a: array<int>)
   requires a != null
   reads a
{
   forall j, k :: 0 <= j < k < a.Length ==> a[j] >= a[k]
}


// not working also

method mergeSort(bloods: array?<int>)
modifies bloods;
requires bloods != null;
requires bloods.Length > 0;
ensures sorted(bloods);
ensures bloods.Length > 0;
//requires |bloods| > 0;

{
  if bloods.Length > 1
  {
    var n := bloods.Length;
    var mid := n/2;

    var left := new int[mid];
    var right := new int[n-mid];
    var l := 0;
    var r := mid;

    while l < mid
    decreases mid - l
    invariant 0 <= l <= mid;
    {
      left[l] := bloods[l];
      l := l + 1;
    }

    while r < n
    decreases n - r
    invariant mid <= r <= n;
    {
      right[r-mid] := bloods[r];
      r := r+1;
    }
    // Problem: we are pretty sure that everything up till(line 34) now is verified.

    // now the dafny complain about the loop is not terminated because of the recursion
    // we have tried to put a return statement but it doesnt works
    //Tried giving a decreases clause, but not sure on how to go about it
    mergeSort(left);
    mergeSort(right);

    //If we use this
    //Error: wrong numbe of method result arguments(got:1, expected:0)
    //left := mergeSort(left);
    //If we use this
    //Error: wrong numbe of method result arguments(got:0, expected:1)
    //right := mergeSort();

    //left := mergeSort(left);
    //right := mergeSort(right);


    var i := 0;
    var j := 0;
    var k := 0;

    var x := left.Length;
    var y := right.Length;

    while i < x && j < y
    invariant 0 <= i <= x;
    invariant 0 <= j <= y;
    invariant sorted(bloods);
    decreases n-k
    {
      if left[i] > right[j]
      {
        bloods[k] := left[i];
        i := i + 1;

      } else
      {
        bloods[k] := right[j];
        j := j + 1;
      }

      k := k + 1;
    }

    while i < x
    invariant 0 <= i <= x;

    {
      bloods[k] := left[i];
      i := i+1;
      k := k+1;
    }

    while j < y
    invariant 0 <= j <= y;
    {
      bloods[k] := right[j];
      j := j + 1;
      k := k+1;
    }


  }

    return;
}

predicate sorted(a: array?<int>)
   requires a != null
   reads a
{
   forall j, k :: 0 <= j < k < a.Length ==> a[j] >= a[k]
}
