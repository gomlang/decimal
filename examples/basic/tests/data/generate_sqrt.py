# Optional fixture regeneration; test execution requires no Python.
from decimal import *
import random
from pathlib import Path
r=random.Random(20261022)
modes=['HalfEven','HalfUp','HalfDown','Up','Down','Ceiling','Floor']
rounds=[ROUND_HALF_EVEN,ROUND_HALF_UP,ROUND_HALF_DOWN,ROUND_UP,ROUND_DOWN,ROUND_CEILING,ROUND_FLOOR]
values=['0','1','4.00','1.0000','2','0.1','10','100','6.25','2.25','99.999','0.000625','1e-99','1e99','2.249999999999999999999999999999999999','2.250000000000000000000000000000000001']
values += [str(Decimal(r.randrange(1,10**18)).scaleb(r.randrange(-40,40))) for _ in range(30)]
rows=[]
for v in values:
 for p in [1,2,9,28]:
  for mode,rounding in zip(modes,rounds):
   x=Decimal(v)
   with localcontext() as c:
    c.prec=250
    root=x.sqrt()
    quantum=Decimal(1).scaleb(root.adjusted()-p+1) if root else Decimal(1)
    y=root.quantize(quantum,rounding=rounding)
    inex=y*y!=x
   with localcontext() as c:
    c.prec=p
    c.clear_flags()
    exact_or_even=c.sqrt(x)
    rounded=bool(c.flags[Rounded])
   if not inex: y=exact_or_even
   rows.append('\t'.join([v,str(p),mode,str(y),str(inex).lower(),str(rounded).lower()]))
Path(__file__).with_name('sqrt.tsv').write_text('\n'.join(rows)+'\n')
