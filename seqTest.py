from fractions import Fraction as fract

class zNzSequence():
    def __init__(self,):

        self.verbosity = 0

    def Pz(self,Base):
        if Base is 0:
            return 0.
        if Base is 1:
            return 1.
        pBase = 1/float(Base)
        pSum = pBase
        for i in range(2,Base):
            pSum=pSum+(1/float(i))
            #print 'pSum: {0}'.format(pSum)
        pZero=(1/float(Base-1)) * pSum
        return pZero

    def isPrime(self,N):
        if N > 1:
            for i in range(2,N):
                if (N%i)==0:
                    if self.verbosity > 0: print "{0} is not prime. {1} is a factor".format(N,i)
                    return False
            else:
                if self.verbosity > 0: print '{0} is prime!'.format(N)
                return True
        else:
            if self.verbosity > 0: print 'N={0} is less than or equal to 1'.format(N)
            return False
    
    def findTwins(self,seq):
        tp=[]
        for p in seq:
            p2=p+2
            for i in seq:
                if i == p2:
                    if (p,i) not in tp:
                      tp.append((p,i))
        return tp

    def run(self,lb,ub):
        self.PzSeq=[]
        self.PzPrimes=[]
        self.nPzPrimes=[]
        self.numSeq=[]
        self.tpSeq=[]
        self.lBound=lb
        self.uBound=ub
        self.size = self.uBound - self.lBound
        for i in range(self.lBound,self.uBound):
            PzTmp=self.Pz(i)
            self.PzSeq.append((fract(PzTmp).limit_denominator(),fract(1-PzTmp).limit_denominator()))
        
        for (Pz,nPz) in self.PzSeq:
            if self.verbosity > 0: print '--------------------'
            if self.verbosity > 0: print '{0}, {1}'.format(Pz,nPz)
            # check if numerator prime
            if self.isPrime(Pz.numerator):
                self.PzPrimes.append(Pz.numerator)
                self.numSeq.append(Pz.numerator)
            if self.isPrime(nPz.numerator):
                self.nPzPrimes.append(nPz.numerator)
                self.numSeq.append(nPz.numerator)
            if self.verbosity > 0: print '--------------------'
        
        self.tpSeq=self.findTwins(self.numSeq)
        print '--------------------'
        print self.numSeq
        print '--------------------'
        return {'PzPrimes':self.PzPrimes,'nPzPrimes':self.nPzPrimes,'numSeq':self.numSeq}

