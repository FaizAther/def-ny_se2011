class Blood {
  var expiry :nat;
  
  constructor(e :nat)
  modifies this
  ensures expiry == e
  {
    expiry := e;
  }
  
  function method isExpired() :bool
  reads this
  {
    expiry >= 42
  }
}

method filterExpired(blood :array<Blood>) returns (notExpired :seq<Blood>, expired :seq<Blood>)
requires blood != null
modifies blood
ensures forall i :: 0 <= i < |notExpired| ==> !notExpired[i].isExpired()
ensures forall i :: 0 <= i < |expired| ==> expired[i].isExpired()
ensures multiset(blood[..]) == multiset(expired) + multiset(notExpired)
{
  var i := 0;
  expired := [];
  notExpired := [];
  
  while i < blood.Length 
  invariant i <= blood.Length
  invariant forall j :: 0 <= j < |notExpired| ==> !notExpired[j].isExpired()
  invariant forall j :: 0 <= j < |expired| ==> expired[j].isExpired()
  invariant multiset(blood[..i]) == multiset(expired) + multiset(notExpired)
  {
    if blood[i].isExpired() {
      expired := expired + [blood[i]];
    } else {
      notExpired := notExpired + [blood[i]];
    }
    i := i + 1;
  }
  assert blood[..] == blood[..blood.Length];
}

