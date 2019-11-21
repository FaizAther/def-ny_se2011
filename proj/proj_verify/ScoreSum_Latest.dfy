predicate bloodZero(bloods: array?<int>)
    reads bloods
    requires bloods != null
{
    forall b :: 0 <= b < bloods.Length ==> bloods[b] == 0
}

// calculate score from given parameter
function method calcScore(value:real , min:real , max:real, weight:real ) : real
  //requires max != 0.0
{   
  if max == 0.0 then 0.0
  else
    if weight > 0.0
      then weight *( 1.0- ((value-min) / max) )
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

// find minimum value for the given array of criteria value
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

method scoreSum(a:array?<real>, weight:real, score:array?<real>)
modifies score
requires a != null
requires score != null
requires (score.Length == a.Length);
{
  var n:int := a.Length;
  var min := findMin(a);
  var max := findMax(a);
  var i:int := 0;
  var temp:real;
  while i < n
    invariant 0 <= i <= score.Length
    invariant 0 <= i <= a.Length
  {
    score[i] := score[i] + calcScore(a[i], min, max, weight);
    i := i + 1;
  }
}

//method Main()
//{
//  var weightage: array<real> := new real[4];
//  weightage[0],weightage[1],weightage[2],weightage[3] := 0.52, 0.27, -0.15, 0.06;
//
////  var expiry: array<real> := new real[4];
////  expiry[0],expiry[1],expiry[2],expiry[3] := 10.0 ,21.0, 8.0, 1.0;
////
////  var quantity: array<real> := new real[4];
////  quantity[0],quantity[1],quantity[2],quantity[3] := 10.0 ,0.0, 20.0, 70.0;
////
////  var rank: array<real> := new real[4];
////  rank[0],rank[1],rank[2],rank[3] := 8.0, 5.0, 2.0, 1.0;
////
////  var totalQ: array<real> := new real[4];
////  totalQ[0],totalQ[1],totalQ[2],totalQ[3] := 330.0 ,800.0, 1000.0, 800.0;
////
////  var score: array<real> := new real[4];
////  assert (score.Length == expiry.Length);
////  score[0],score[1],score[2],score[3] := 0.0, 0.0, 0.0, 0.0;
//
//  var expiry: array<real> := new real[2];
//  expiry[0],expiry[1] := 10.0 ,21.0;
//
//  var quantity: array<real> := new real[2];
//  quantity[0],quantity[1] := 10.0 ,0.0;
//
//  var totalQ: array<real> := new real[2];
//  totalQ[0],totalQ[1] := 330.0 ,800.0;
//  
//  var rank: array<real> := new real[2];
//  rank[0],rank[1] := 8.0, 5.0;
//  
//  var score: array<real> := new real[2];
//  assert (score.Length == expiry.Length);
//  score[0],score[1] := 0.0, 0.0;
//  
//  scoreSum(expiry, weightage[0], score);
//  scoreSum(quantity, weightage[1], score);
//  scoreSum(totalQ, weightage[2], score);
//  scoreSum(rank, weightage[3], score);
//
//  //print(score[..]);
//}
