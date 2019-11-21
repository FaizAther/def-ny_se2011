class Blood {
  var expiry: real;
  var quantity: real;
  var rank: real;
  var totalQuantity: real;
  var score: real;
  
  constructor(e :real , q: real , r: real , t: real )
  modifies this
  ensures expiry == e
  ensures quantity == q
  ensures rank == r
  ensures totalQuantity == t
  ensures score == 0.0
  {
    
    expiry := e;
    quantity := q;
    rank := r;
    totalQuantity := t;
    score := 0.0; 
  }
//   method setScore(s:real)
//   ensures this.score == s
//   {
//     this.score := score;
//   }

}

method scoreSum(bloods : array<Blood>)//, weights : array<real>)
requires bloods != null
//requires weights[0] != null
//requires bloods.Length == we
modifies bloods
//requires forall i :: 0 <= i < bloods.Length ==> bloods[i].score == 0.0
//ensures forall i :: 0 <= i <
{
    var weights := new real[4];
    weights[0],weights[1],weights[2],weights[3] := 0.52, 0.27, -0.15, 0.06;
    var eArr := new real[bloods.Length];
    var qArr := new real[bloods.Length];
    var rArr := new real[bloods.Length];
    var tArr := new real[bloods.Length];
    var i := 0;
    
    while i < bloods.Length
    invariant 0 <= i <= bloods.Length
    invariant 0 <= i <= eArr.Length
    invariant 0 <= i <= qArr.Length
    invariant 0 <= i <= rArr.Length
    invariant 0 <= i <= tArr.Length
    {
      eArr[i] := bloods[i].expiry; 
      qArr[i] := bloods[i].expiry; 
      rArr[i] := bloods[i].expiry; 
      tArr[i] := bloods[i].expiry; 
      i := i + 1;
    } 
    var minE := findMin(eArr);
    var maxE := findMax(eArr);
    var minQ := findMin(qArr);
    var maxQ := findMax(qArr);
    var minR := findMin(rArr);
    var maxR := findMax(rArr);
    var minT := findMin(tArr);
    var maxT := findMax(tArr);
    
    var b := 0;
    while b < bloods.Length 
    invariant 0 <= b <= bloods.Length
    //invariant 0 <= b <= expArr.Length
    modifies bloods[b]
    {
//      assert maxE != 0.0;
//      assert maxQ != 0.0;
//      assert maxR != 0.0;
//      assert maxT != 0.0;
      var e_score := calcScore(bloods[b].expiry, minE, maxE, weights[0]);
      var q_score := calcScore(bloods[b].quantity, minQ, maxQ, weights[1]);
      var r_score := calcScore(bloods[b].rank, minR, maxR, weights[2]);
      var t_score := calcScore(bloods[b].totalQuantity, minT, maxT, weights[3]);
      var k := e_score + q_score + r_score + t_score;
      //bloods[b].setScore(k) ;
      bloods[b].score := k;
      
      b := b + 1;
    }
  
}
// calculate score from given parameter
function method calcScore(value:real , min:real , max:real, weight:real ) : real
//requires 
{
  if max == 0.0 then 0.0
  else
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
 //ensures max != 0.0
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
