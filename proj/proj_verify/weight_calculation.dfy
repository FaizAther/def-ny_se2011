
// predicate to make sure the blood weight are initialise to zero
// TODO change int to BLOOD datatype
predicate bloodZero(bloods: array?<int>)
  reads bloods
  requires bloods != null
{
  forall b :: 0 <= b < bloods.Length ==> bloods[b] == 0
}

// calculate score from given parameter
function method calcScore(value:real , min:real , max:real, weight:real ) : real
requires max != 0.0
{
  if weight > 0.0
    then weight *( 1.0- (value-min) / max )
  else
    weight * (( value-min) / max )

}

// find maximum value for the given array of criteria value
method findMax(a:array?<real>) returns(max:real)
 requires a!=null;
 ensures (forall j :int :: (j >= 0 && j < a.Length ==> max >= a[j]));
 ensures (a.Length > 0)==>(exists j : int :: j>=0 && j < a.Length && max==a[j]);
{
  if (a.Length == 0)
  {
    max := 0.0;
  }
  else
  {
    max:=a[0];
    var i:int :=1;

    while(i < a.Length)
    invariant (i<=a.Length)
    invariant (forall j:int :: j>=0 && j<i ==> max >= a[j]);
    invariant (exists j:int :: j>=0 && j<i && max==a[j]);
    decreases (a.Length-i);
    {

     if(a[i] > max)
     {
       max := a[i];
     }

     i := i + 1;

    }
  }

}


method findMin(a:array?<real>) returns(min:real)
 requires a!=null;
 ensures (forall j :int :: (j >= 0 && j < a.Length ==> min <= a[j]));
 ensures (a.Length > 0)==>(exists j : int :: j>=0 && j < a.Length && min==a[j]);
{
  if (a.Length == 0)
  {
    min := 0.0;
  }
  else
  {
    min:=a[0];
    var i:int :=1;

    while(i < a.Length)
    invariant (i<=a.Length)
    invariant (forall j:int :: j>=0 && j<i ==> min <= a[j]);
    invariant (exists j:int :: j>=0 && j<i && min==a[j]);
    decreases (a.Length-i);
    {

     if(a[i] < min)
     {
       min := a[i];
     }

     i := i + 1;

    }
  }

}

method Main() returns (sums array<int>)
ensure forall i:: 0 <= i < bloods.length sums[i] == calc
{

  var bloods: array<real> := new real[5];
  bloods[0],bloods[1],bloods[2],bloods[3],bloods[4] := 10.0 ,8.0, 15.0, 17.0, 7.0;

  var min := findMin(bloods);
//  //print(min);
  assert (bloods[4] < bloods[1] < bloods[0] < bloods[2] < bloods[3]);
  assert min == 7.0;
//  var max := findMax(bloods);
//  //print(max);
//  //assert max == 17.0;

  var weightage: array<real> := new real[4];
  weightage[0],weightage[1],weightage[2],weightage[3] := 0.52, 0.27, -0.15, 0.06;

  var expiry: array<real> := new real[4];
  expiry[0],expiry[1],expiry[2],expiry[3] := 3.0 ,5.0, 8.0, 1.0;

  var minE := findMin(expiry);
  var maxE := findMax(expiry);

  var quantity: array<real> := new real[4];
  quantity[0],quantity[1],quantity[2],quantity[3] := 50.0 ,60.0, 20.0, 70.0;

  var minQ := findMin(quantity);
  var maxQ := findMax(quantity);

  var rank: array<real> := new real[4];
  rank[0],rank[1],rank[2],rank[3] := 7.0, 5.0, 2.0, 1.0;

  var minR := findMin(rank);
  var maxR := findMax(rank);

  var totalQ: array<real> := new real[4];
  totalQ[0],totalQ[1],totalQ[2],totalQ[3] := 800.0 ,750.0, 1000.0, 800.0;

  var minT := findMin(totalQ);
  var maxT := findMax(totalQ);

  var scores: array<real> := new real[expiry.Length];
  assert (scores.Length == expiry.Length);

  var i := 0;
  while i < scores.Length
  invariant 0 <= i <= scores.Length
  {
    scores[i] := scores[i] + calcScore(expiry[i], minE, maxE, weightage[0]);
    i := i + 1;
  }
  /////////////////////////////////

  i := 0;
  while i < scores.Length
  invariant 0 <= i <= scores.Length
  {
    scores[i] := scores[i] + calcScore(quantity[i], minQ, maxQ, weightage[1]);
    i := i + 1;
  }
  /////////////////////////////////
  i := 0;
  while i < scores.Length
  invariant 0 <= i <= scores.Length
  {
    scores[i] := scores[i] + calcScore(rank[i], minR, maxR, weightage[2]);
    i := i + 1;
  }
  /////////////////////////////////

  i := 0;
  while i < scores.Length
  invariant 0 <= i <= scores.Length
  {
    scores[i] := scores[i] + calcScore(totalQ[i], minT, maxT, weightage[3]);
    i := i + 1;
  }
  /////////////////////////////////

  //print(scores[..]);
}
https://rise4fun.com/Dafny/JOOTh


//method scoreSum() //returns (sums: array<real>)
////ensures forall i :: 0 <= i < bloods.Length ==> sums[i] == calc
//{
// scores
//}
//  var bloods: array<real> := new real[5];
//  bloods[0],bloods[1],bloods[2],bloods[3],bloods[4] := 10.0 ,8.0, 15.0, 17.0, 7.0;
//
//  var min := findMin(bloods);
//  assert (bloods[4] < bloods[1] < bloods[0] < bloods[2] < bloods[3]);
//  assert min == 7.0;
//  var max := findMax(bloods);
//  assert (bloods[3] > bloods[2] > bloods[0] > bloods[1] > bloods[4]);
//  assert max == 17.0;
//
//  var weightage: array<real> := new real[4];
//  weightage[0],weightage[1],weightage[2],weightage[3] := 0.52, 0.27, -0.15, 0.06;
//
//  var expiry: array<real> := new real[4];
//  expiry[0],expiry[1],expiry[2],expiry[3] := 3.0 ,5.0, 8.0, 1.0;
//
//calScore(expiry, w[0])
//  var minE := findMin(expiry);
//  var maxE := findMax(expiry);
//
//  var quantity: array<real> := new real[4];
//  quantity[0],quantity[1],quantity[2],quantity[3] := 50.0 ,60.0, 20.0, 70.0;
//
//  var minQ := findMin(quantity);
//  var maxQ := findMax(quantity);
//
//  var rank: array<real> := new real[4];
//  rank[0],rank[1],rank[2],rank[3] := 7.0, 5.0, 2.0, 1.0;
//
//  var minR := findMin(rank);
//  var maxR := findMax(rank);
//
//  var totalQ: array<real> := new real[4];
//  totalQ[0],totalQ[1],totalQ[2],totalQ[3] := 800.0 ,750.0, 1000.0, 800.0;
//
//  var minT := findMin(totalQ);
//  var maxT := findMax(totalQ);
//
//  var scores: array<real> := new real[expiry.Length];
//  assert (scores.Length == expiry.Length);
//
//  var i := 0;
//  while i < scores.Length
//  invariant 0 <= i <= scores.Length
//  {
//    scores[i] := scores[i] + calcScore(expiry[i], minE, maxE, weightage[0]);
//    i := i + 1;
//  }
//  /////////////////////////////////
//
//  i := 0;
//  while i < scores.Length
//  invariant 0 <= i <= scores.Length
//  {
//    scores[i] := scores[i] + calcScore(quantity[i], minQ, maxQ, weightage[1]);
//    i := i + 1;
//  }
//  /////////////////////////////////
//
//  i := 0;
//  while i < scores.Length
//  invariant 0 <= i <= scores.Length
//  {
//    scores[i] := scores[i] + calcScore(rank[i], minR, maxR, weightage[2]);
//    i := i + 1;
//  }
//  /////////////////////////////////
//
//  i := 0;
//  while i < scores.Length
//  invariant 0 <= i <= scores.Length
//  {
//    scores[i] := scores[i] + calcScore(totalQ[i], minT, maxT, weightage[3]);
//    i := i + 1;
//  }
//  /////////////////////////////////
//
//  //print(scores[..]);
//}

// predicate to make sure the blood weight are initialise to zero
// TODO change int to BLOOD datatype
predicate bloodZero(bloods: array?<int>)
  reads bloods
  requires bloods != null
{
  forall b :: 0 <= b < bloods.Length ==> bloods[b] == 0
}

// calculate score from given parameter
function method calcScore(value:real , min:real , max:real, weight:real ) : real
requires max != 0.0
{
  if weight > 0.0
    then weight *( 1.0- (value-min) / max )
  else
    weight * (( value-min) / max )
}
// find maximum value for the given array of criteria value
method findMax(a:array?<real>) returns(max:real)
 requires a!=null;
 ensures (forall j :int :: (j >= 0 && j < a.Length ==> max >= a[j]));
 ensures (a.Length > 0)==>(exists j : int :: j>=0 && j < a.Length && max==a[j]);
{
  if (a.Length == 0)
  {
    max := 0.0;
  }
  else
  {
    max:=a[0];
    var i:int :=1;

    while(i < a.Length)
    invariant (i<=a.Length)
    invariant (forall j:int :: j>=0 && j<i ==> max >= a[j]);
    invariant (exists j:int :: j>=0 && j<i && max==a[j]);
    decreases (a.Length-i);
    {

     if(a[i] > max)
     {
       max := a[i];
     }

     i := i + 1;

    }
  }

}


method findMin(a:array?<real>) returns(min:real)
 requires a!=null;
 ensures (forall j :int :: (j >= 0 && j < a.Length ==> min <= a[j]));
 ensures (a.Length > 0)==>(exists j : int :: j>=0 && j < a.Length && min==a[j]);
{
  if (a.Length == 0)
  {
    min := 0.0;
  }
  else
  {
    min:=a[0];
    var i:int :=1;

    while(i < a.Length)
    invariant (i<=a.Length)
    invariant (forall j:int :: j>=0 && j<i ==> min <= a[j]);
    invariant (exists j:int :: j>=0 && j<i && min==a[j]);
    decreases (a.Length-i);
    {

     if(a[i] < min)
     {
       min := a[i];
     }

     i := i + 1;

    }
  }

}

method calcScoreForEachCriteria(criteria: array<real>, w:real) returns (scores: array<real>)
//ensures
//requires criteria.Length == scores.Length
{
//  var totalQ: array<real> := new real[4];
//  totalQ[0],totalQ[1],totalQ[2],totalQ[3] := 800.0 ,750.0, 1000.0, 800.0;
  scores := new real[criteria.Length];
  var min := findMin(criteria);
  var max := findMax(criteria);

//  var scores: array<real> := new real[expiry.Length];
//  assert (scores.Length == expiry.Length);

  var i := 0;
  while i < criteria.Length
  invariant 0 <= i <= criteria.Length
  {
    scores[i] := scores[i] + calcScore(criteria[i], min, max, w);
    i := i + 1;
  }

}
