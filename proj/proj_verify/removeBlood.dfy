method removeBlood(bloods: array<int> ,key: int)
requires key < bloods.Length;
requires key >= 0;
{
  var i := key;
  var n := bloods.Length;
  if( key == n-1)
  {
    bloods[..] := bloods[0 ..n-1];
  }
  while i <  n-1
  invariant 0 <= i <= n-1
  {
    bloods[i] := bloods[i+1];
    i := i+1;
  }
}
