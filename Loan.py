class Loan:
    'Base class for all loans.'
    LoanCount = 0
    def __init__(self, m,  y, v, r, score, term):
        LoanCount += 1
        self.PolicyNumber = LoanCount
        self.OriginMonth = m
        self.OriginYear = y
        self.OriginValue = v
        self.PrincipalValue = v
        self.Balance = v
        self.APR = r
        self.CreditScore = score
        self.Term = term
        self.TermsPassed = 0
        self.ScheduledPayment =(self.OriginValue/((((1+(self.APR/100/12))^self.Term)-1)/((self.APR/100/12)*(1+(self.APR/100/12))^self.Term)))
        self.MissedPayments = 0

    def TakePayment():
        if self.ScheduledPayment > self.Balance:
            self.ScheduledPayment = self.Balance
        self.Balance -= self.ScheduledPayment

    def ApplyInterest():
        self.Balance += (self.Balalnce * (self.APR / 12))

    def Term():
        ApplyInterest()
        TakePayment()
        TermsPassed += 1
