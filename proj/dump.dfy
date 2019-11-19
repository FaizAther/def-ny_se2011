
datatype BLOOD = PACK(key: string, value)
class Blood
{
  var bloodList: array<BLOOD>;
  var amount: int;
  var isVerified: bool;

  predicate Valid()
  read this;
  { }
}
