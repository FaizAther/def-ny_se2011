
// predicate to make sure the blood weight are initialise to zero
// TODO change int to BLOOD datatype
predicate bloodZero(bloods: array?<int>)
  reads bloods
  requires bloods != null
{
  forall b :: 0 <= b < bloods.Length ==> bloods[b] == 0
}

// calculate score from given parameter
function calcScore(value:real , min:real , max:real, weight:real ) : real
requires max != 0.0
{
  if weight > 0.0
    then weight *( 1.0- (value-min) / max )
  else
    weight * (( value-min) / max )

}
